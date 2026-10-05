"""Genera il manuale in HTML dai capitoli markdown (una pagina per capitolo).

Uso: python3 build.py  -> crea la cartella html/ con index.html, un file per capitolo
e lo stile condiviso. Ogni pagina ha l'indice di navigazione e l'indice del capitolo.
"""

import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "html"

CSS = """
:root { --ink:#1f2933; --muted:#6b7480; --line:#e4e7eb; --accent:#c79b00; --code:#f5f7f9; }
* { box-sizing: border-box; }
body { margin:0; font:16px/1.6 system-ui, -apple-system, "Segoe UI", sans-serif; color:var(--ink); display:flex; min-height:100vh; }
nav.side { width:280px; flex-shrink:0; border-right:1px solid var(--line); padding:24px 18px; position:sticky; top:0; height:100vh; overflow-y:auto; background:#fafbfc; }
nav.side h1 { font-size:18px; margin:0 0 16px; }
nav.side ol { list-style:none; padding:0; margin:0; }
nav.side li { margin:4px 0; }
nav.side a { color:var(--ink); text-decoration:none; display:block; padding:6px 8px; border-radius:6px; }
nav.side a:hover { background:#eef1f4; }
nav.side a.current { background:#fff4cc; font-weight:600; }
nav.side .sub { margin-left:14px; font-size:14px; }
nav.side .sub a { padding:3px 8px; color:var(--muted); }
main { flex:1; max-width:860px; padding:36px 48px 80px; }
h1 { font-size:30px; margin-top:0; }
h2 { font-size:22px; margin-top:40px; border-bottom:1px solid var(--line); padding-bottom:6px; }
h3 { font-size:18px; margin-top:28px; }
h4 { font-size:16px; }
code { background:var(--code); padding:1px 5px; border-radius:4px; font:14px ui-monospace, Menlo, Consolas, monospace; }
pre { background:var(--code); padding:14px 16px; border-radius:8px; overflow-x:auto; border:1px solid var(--line); }
pre code { background:none; padding:0; font-size:13px; }
table { border-collapse:collapse; width:100%; margin:14px 0; font-size:15px; }
th, td { border:1px solid var(--line); padding:8px 10px; text-align:left; vertical-align:top; }
th { background:#fafbfc; }
blockquote { margin:14px 0; padding:8px 14px; border-left:4px solid var(--accent); background:#fffaea; color:var(--ink); }
.toc { background:#fafbfc; border:1px solid var(--line); border-radius:8px; padding:12px 18px; margin:20px 0 28px; }
.toc ol { margin:6px 0; padding-left:20px; }
.toc li { margin:3px 0; }
.pager { display:flex; justify-content:space-between; margin-top:48px; border-top:1px solid var(--line); padding-top:18px; }
.pager a { color:var(--ink); text-decoration:none; font-weight:600; }
@media (max-width: 800px) { body { display:block; } nav.side { width:auto; height:auto; position:static; } main { padding:24px 18px; } }
"""

CHAPTERS = [
    ("01-accesso-e-navigazione", "1. Primo accesso e navigazione"),
    ("02-namespace-ruoli-utenti", "2. Namespace, ruoli e utenti"),
    ("03-liste-e-iscritti", "3. Liste e iscritti"),
    ("04-segmenti", "4. Segmenti"),
    ("05-campagne", "5. Campagne"),
    ("06-galleria-e-spazio", "6. Galleria media e spazio"),
    ("07-statistiche", "7. Statistiche"),
    ("08-cestino", "8. Cestino e ripristino"),
    ("09-api", "9. API per sviluppatori"),
    ("10-crediti-invii", "10. Crediti sugli invii"),
]


def page(title: str, body: str, current: str, toc_html: str, prev_next: str) -> str:
    items = []
    for slug, label in CHAPTERS:
        cls = ' class="current"' if slug == current else ""
        items.append(f'<li><a href="{slug}.html"{cls}>{label}</a></li>')
    nav = (
        '<nav class="side"><h1>Manuale di Postino</h1>'
        '<ol><li><a href="index.html">Indice generale</a></li>'
        + "".join(items)
        + "</ol></nav>"
    )
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Manuale di Postino</title>
<style>{CSS}</style></head>
<body>{nav}<main>{toc_html}{body}{prev_next}</main></body></html>"""


def toc_for(html: str) -> str:
    """Indice del capitolo: i titoli di secondo livello (h2) con ancora."""
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    if not heads:
        return ""
    lis = "".join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>' for i, t in heads)
    return f'<div class="toc"><strong>In questa pagina</strong><ol>{lis}</ol></div>'


def main() -> None:
    OUT.mkdir(exist_ok=True)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])
    for idx, (slug, label) in enumerate(CHAPTERS):
        src = ROOT / f"{slug}.md"
        md.reset()
        html = md.convert(src.read_text(encoding="utf-8"))
        title = md.toc_tokens[0]["name"] if md.toc_tokens else label
        prev_link = next_link = ""
        if idx > 0:
            prev_link = f'<a href="{CHAPTERS[idx-1][0]}.html">← {CHAPTERS[idx-1][1]}</a>'
        if idx < len(CHAPTERS) - 1:
            next_link = f'<a href="{CHAPTERS[idx+1][0]}.html">{CHAPTERS[idx+1][1]} →</a>'
        pager = f'<div class="pager"><span>{prev_link}</span><span>{next_link}</span></div>'
        (OUT / f"{slug}.html").write_text(
            page(title, html, slug, toc_for(html), pager), encoding="utf-8"
        )

    md.reset()
    guide = md.convert((ROOT / "guida-redattore-lettore.md").read_text(encoding="utf-8"))
    guide_title = md.toc_tokens[0]["name"] if md.toc_tokens else "Guida per redattori e lettori"
    (OUT / "guida-redattore-lettore.html").write_text(
        page(guide_title, guide, "", toc_for(guide), ""), encoding="utf-8"
    )

    md.reset()
    intro = md.convert((ROOT / "README.md").read_text(encoding="utf-8"))
    intro = re.sub(r'href="([0-9]{2}-[a-z0-9-]+)\.md"', r'href="\1.html"', intro)
    (OUT / "index.html").write_text(page("Indice", intro, "", "", ""), encoding="utf-8")
    print(f"Generati {len(CHAPTERS) + 2} file in {OUT}")


if __name__ == "__main__":
    main()
