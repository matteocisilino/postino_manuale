# 5. Campagne

## Creare una campagna

Vai in **Campagne → Nuova campagna**. Scegli il **namespace** e il **tipo di
campagna**: non si cambia più dopo la creazione.

- **Normale (`regular`):** una newsletter che invii tu, subito o pianificata.
- **Digest RSS:** genera e invia automaticamente i nuovi articoli di un feed.
- **Triggered:** innescata da un sistema esterno tramite API, non da qui.

Compila nome, oggetto email e scegli il **mittente** (una configurazione di
invio già creata in Mittenti). In **Destinatari** scegli una o più liste e
segmenti: un iscritto presente in più destinatari riceve la campagna **una
sola volta**. Finché non scegli almeno un destinatario il pulsante per
salvare resta disattivato, e sotto compare il link **Vai ai destinatari**.

**Email mittente:** per una nuova campagna è precompilata con il tuo
indirizzo, ed è l'indirizzo da cui partono la campagna e le prove. Svuotala
per usare l'indirizzo del mittente scelto. Con l'invio gestito da Postino il
dominio dell'indirizzo deve essere un dominio di invio verificato, altrimenti
la campagna non parte. Con un relay SMTP, controlla che il tuo server di
posta accetti quell'indirizzo come mittente.

## Scrivere il contenuto

Puoi partire da un **template** esistente (opzionale): se il template era
stato creato con l'editor visuale lo ritrovi così com'era; se era in
HTML/testo semplice, parti da quel testo.

Il contenuto si scrive in due modi, intercambiabili con un clic:

- **Editor visuale:** componi il messaggio trascinando blocchi su un
  canvas (lo stesso motore usato per i Template). Usa **Galleria media**
  per inserire un'immagine già caricata o per caricarne una nuova: prima
  seleziona un elemento del canvas, poi scegli l'immagine, che viene
  inserita subito dopo l'elemento selezionato. Per **sostituire**
  un'immagine fai doppio clic su di essa e scegline un'altra dalla galleria.
- **Modifica HTML:** la casella di testo parte dall'HTML del messaggio che
  stai componendo nell'editor visuale, così puoi ritoccarlo o copiarlo.

Il passaggio tra le due modalità funziona così:

- Da **visuale a HTML** non perdi nulla: ritrovi esattamente il contenuto
  del canvas, convertito in HTML.
- Da **HTML a visuale** l'editor visuale riprende il suo contenuto, ma non
  può importare l'HTML scritto a mano. Se nel frattempo hai modificato
  l'HTML, Postino ti chiede conferma prima di scartare quelle modifiche.
- Una campagna salvata in modalità HTML si riapre in HTML, e chi la apre
  vede le modifiche fatte a mano. Passando all'editor visuale si riparte da
  un modello nuovo, e anche qui viene chiesta conferma.

**Tag di merge:** scrivi `[FIRST_NAME]`, `[EMAIL]`, `[UNSUBSCRIBE_URL]` o la
chiave di un campo personalizzato in maiuscolo (es. `[CITTA]`) per inserire
i dati di ogni iscritto. Un tag che non corrisponde a nessun campo, o un
campo vuoto, diventa testo vuoto. Il resto del messaggio, comprese altre
parentesi quadre, resta com'è.

**URL base delle immagini** (opzionale): se nell'HTML usi percorsi relativi
come `img/logo.png`, indica qui l'indirizzo da cui vanno recuperati (es.
`https://tuosito.it/cartella/`).

### Libreria di scraping

Nel pannello **Libreria di scraping**, a fianco dell'editor visuale, puoi
incollare l'URL di una pagina web (tipicamente il tuo sito) e premere
**Scansiona**: il sistema scarica testo e immagini della pagina, li ripulisce
da stili e script e li mostra come blocchi da trascinare nel messaggio. Le
pagine già scansionate restano come scorciatoie, anche se chiudi e riapri la
campagna, per poterle riscansionare in futuro.

**Attenzione**, come ricorda l'avviso nel pannello: usa solo contenuti di cui
hai i diritti (il tuo sito o materiale di tua proprietà) — la responsabilità
dell'uso di contenuti di terzi è tua. Le immagini che trascini nel messaggio
e poi salvi restano ospitate su Postino, non collegate al sito originale;
quelle scaricate ma non usate vengono eliminate al salvataggio.

## Invio

Dalla scheda di una campagna in bozza:

- **Avvia invio:** parte subito, senza ulteriori conferme. Compare il
  messaggio "Invio avviato": Postino prepara l'elenco dei destinatari e
  dopo pochi secondi la scheda si aggiorna da sola con l'avanzamento. Un
  secondo clic non provoca un doppio invio. Se l'invio non
  può partire (per esempio perché la campagna è già stata avviata), il
  motivo compare in cima alla scheda.
- **Pianifica:** scegli data e ora (nel tuo fuso orario) e conferma — un
  controllo automatico avvia la campagna quando arriva l'orario.
- **Invia prova:** manda il messaggio a un indirizzo a tua scelta, per
  controllare com'arriva prima dell'invio vero.

Durante l'invio puoi **metterlo in pausa** e **riprenderlo**. Per annullare
una campagna pianificata, in pausa o in corso usa **Annulla**: una campagna
solo pianificata (non ancora partita) torna in **bozza**, così puoi
pianificarla di nuovo o avviarla subito; una campagna che aveva già iniziato
a inviare resta segnata come annullata, senza possibilità di ripianificarla.

A invio terminato, **Reinvia ai nuovi destinatari** manda la campagna solo a
chi, nel frattempo, è diventato un destinatario valido e non l'ha ancora
ricevuta (per esempio un indirizzo che era in attesa di verifica email).

**Duplica** crea una copia della campagna in bozza, con lo stesso contenuto e
le stesse impostazioni, utile per rimandare un invio annullato o ripetere una
campagna simile.

## Digest RSS

Alla creazione scegli "Digest RSS" e indica l'URL del feed: non serve
scrivere il contenuto, viene generato automaticamente a ogni nuovo articolo
(il controllo avviene periodicamente). Al primo controllo viene inviato solo
l'articolo più recente, non tutto lo storico del feed. La scheda della
campagna mostra l'URL del feed e il link dell'ultimo articolo già inviato.

## Triggered

Alla creazione scegli "Triggered": oggetto e contenuto si scrivono come per
una campagna normale (puoi anche inviare una prova), ma l'invio non parte da
qui — lo innesca un sistema esterno con una chiave API dedicata (vedi il
capitolo API). Il destinatario deve essere già iscritto e confermato sulla
lista scelta come target: non viene iscritto automaticamente.
