# 9. API per sviluppatori

Questo capitolo serve a collegare un sistema esterno a Postino (un sito, un
e-commerce, un CRM, un'applicazione interna) senza usare la console. Gli esempi sono
in **PHP**, **Ruby** e **Python**, ma l'API è un normale servizio HTTP con risposte
JSON: qualsiasi linguaggio con un client HTTP può usarla.

## Panoramica

| Cosa | Dove |
|---|---|
| URL di base | `https://<tua-istanza>/api/v1` |
| Formato | JSON, UTF-8 |
| Autenticazione | `Authorization: Bearer <chiave>` |
| Errori | RFC 9457 (`application/problem+json`) |
| Limite | 10 richieste al secondo per chiave |

La documentazione interattiva (OpenAPI) è disponibile su `/api/v1/docs` della tua
istanza.

## Autenticazione

Crea una chiave dalla console, nella pagina **Chiavi API**. La chiave ha un formato
del tipo `pst_<prefisso>_<segreto>` ed è legata a:

- **un namespace**: l'API vede solo le liste di quel namespace;
- **uno o più scope**, cioè i permessi;
- facoltativamente, un elenco di **liste ammesse**: la chiave non vede le altre.

Il segreto viene mostrato **una sola volta**, alla creazione. Conservalo nel gestore
di segreti del tuo sistema, mai nel codice sorgente.

Gli scope disponibili:

| Scope | Permette |
|---|---|
| `lists:read` | leggere le liste e i loro campi |
| `subscribers:read` | leggere un iscritto |
| `subscribers:write` | iscrivere, modificare, disiscrivere, cancellare |
| `campaigns:read` | leggere le campagne |
| `campaigns:trigger` | inviare un'email automatica da una campagna triggered |

Una richiesta senza lo scope necessario risponde `403`.

Esempio di intestazione:

```
Authorization: Bearer pst_a1b2c3d4_<segreto>
```

## Limite di richieste

Il limite è di **10 richieste al secondo per chiave**. Ogni risposta include:

```
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1735689600
```

Oltre il limite Postino risponde `429`. Il comportamento corretto del client è
aspettare fino al momento indicato da `X-RateLimit-Reset` e riprovare.

## Errori

Gli errori seguono lo standard RFC 9457:

```json
{
  "type": "about:blank",
  "title": "NotFoundError",
  "status": 404,
  "detail": "Lista non trovata."
}
```

- `status`: il codice HTTP.
- `title`: il tipo di errore, stabile e adatto allo smistamento nel codice
  (`NotFoundError`, `ConflictError`, `SuppressedError`, `ValidationDomainError`).
- `detail`: un messaggio in italiano, pensato per essere mostrato a una persona. Non
  usarlo per la logica del programma.

I codici più comuni:

| Codice | Significato |
|---|---|
| `200`, `201`, `204` | operazione riuscita (`201` = creato) |
| `401` | chiave mancante o non valida |
| `403` | scope insufficiente |
| `404` | risorsa non trovata |
| `409` | indirizzo in una lista di soppressione |
| `422` | dati non validi (per esempio email malformata) |
| `429` | troppe richieste |

## Idempotenza

Per l'iscrizione puoi inviare l'intestazione `Idempotency-Key` con un valore scelto
da te, per esempio l'id dell'ordine. Postino conserva la risposta per **24 ore**: una
seconda richiesta con la stessa chiave riceve la risposta della prima, senza ripetere
l'operazione. È utile quando il client riprova in automatico dopo un errore di rete.

## Endpoint

### Liste

#### `GET /api/v1/lists`

Scope `lists:read`. Restituisce le liste visibili alla chiave.

#### `GET /api/v1/lists/{list_cid}/fields`

Scope `lists:read`. Restituisce i campi personalizzati della lista: utili per
costruire un modulo esterno con gli stessi campi della console.

### Iscritti

#### `POST /api/v1/lists/{list_cid}/subscriptions`

Scope `subscribers:write`. Iscrive un indirizzo alla lista.

Corpo della richiesta:

| Campo | Obbligatorio | Descrizione |
|---|---|---|
| `email` | sì | indirizzo da iscrivere |
| `fields` | no | campi personalizzati, per esempio `{"FIRST_NAME": "Maria"}` |
| `double_opt_in` | no | `true` = doppio opt-in, `false` = singolo; se omesso vale la modalità della lista |
| `force_resubscribe` | no | `true` per reiscrivere chi si era disiscritto |
| `source_label` | no | etichetta libera per sapere da dove arriva l'iscrizione |

Risposte: `201` nuovo iscritto (in attesa di conferma se la modalità lo richiede),
`200` già presente o aggiornato, `409` indirizzo soppresso, `422` dati non validi.

**PHP** (Guzzle):

```php
use GuzzleHttp\Client;

$http = new Client(['base_uri' => 'https://posta.esempio.it/api/v1/', 'http_errors' => false]);

$response = $http->post("lists/{$listCid}/subscriptions", [
    'headers' => [
        'Authorization' => "Bearer {$token}",
        'Idempotency-Key' => 'ordine-8841',
    ],
    'json' => [
        'email' => 'cliente@esempio.it',
        'fields' => ['FIRST_NAME' => 'Maria'],
        'double_opt_in' => true,
        'source_label' => 'checkout',
    ],
]);

echo $response->getStatusCode(), ' ', $response->getBody();
```

**Ruby** (libreria standard):

```ruby
require "net/http"
require "json"
require "uri"

uri = URI("https://posta.esempio.it/api/v1/lists/#{list_cid}/subscriptions")
req = Net::HTTP::Post.new(uri)
req["Authorization"] = "Bearer #{token}"
req["Idempotency-Key"] = "ordine-8841"
req["Content-Type"] = "application/json"
req.body = {
  email: "cliente@esempio.it",
  fields: { FIRST_NAME: "Maria" },
  double_opt_in: true,
  source_label: "checkout"
}.to_json

res = Net::HTTP.start(uri.host, uri.port, use_ssl: true) { |http| http.request(req) }
puts "#{res.code} #{res.body}"
```

**Python** (libreria `requests`):

```python
import requests

response = requests.post(
    f"https://posta.esempio.it/api/v1/lists/{list_cid}/subscriptions",
    headers={"Authorization": f"Bearer {token}", "Idempotency-Key": "ordine-8841"},
    json={
        "email": "cliente@esempio.it",
        "fields": {"FIRST_NAME": "Maria"},
        "double_opt_in": True,
        "source_label": "checkout",
    },
    timeout=10,
)
print(response.status_code, response.text)
```

#### `GET /api/v1/lists/{list_cid}/subscriptions/{email}`

Scope `subscribers:read`. Restituisce stato e campi dell'iscritto. Risponde `404`
sia se l'iscritto non esiste sia se l'indirizzo non è valido: così non si rivela a
chi non dovrebbe la presenza di un contatto.

#### `PATCH /api/v1/lists/{list_cid}/subscriptions/{email}`

Scope `subscribers:write`. Aggiorna i campi personalizzati. È un'unione: i campi che
non invii restano invariati.

```python
requests.patch(
    f"https://posta.esempio.it/api/v1/lists/{list_cid}/subscriptions/cliente@esempio.it",
    headers={"Authorization": f"Bearer {token}"},
    json={"fields": {"CITY": "Milano"}},
    timeout=10,
)
```

#### `POST /api/v1/lists/{list_cid}/unsubscribe`

Scope `subscribers:write`. Corpo: `{"email": "..."}`. È idempotente: se l'indirizzo
è già disiscritto risponde `204` senza errore.

#### `DELETE /api/v1/lists/{list_cid}/subscriptions/{email}`

Scope `subscribers:write`. Cancellazione per GDPR: l'indirizzo viene anonimizzato,
non cancellato, per non rompere la storia degli invii. Risponde `204`.

### Campagne triggered

#### `POST /api/v1/campaigns/{campaign_cid}/trigger`

Scope `campaigns:trigger`. Invia subito un'email usando una campagna di tipo
**triggered** come modello. Serve per le automazioni legate a un evento (ordine
confermato, carrello abbandonato), non per gli invii di massa.

Vincoli:

- il destinatario deve essere **già iscritto e confermato** alla lista della campagna;
  altrimenti risponde `404` e non invia nulla;
- i valori in `data` valgono solo per questo invio: diventano segnaposto come
  `[ORDER_ID]` nel modello, senza essere salvati sull'iscritto.

Corpo: `{"email": "...", "data": {"ORDER_ID": "A-1042"}}`. Risposta `200` con
`{"status": "sent", "campaign_message_id": 68}`, oppure `"failed"` se il server di
posta ha rifiutato il messaggio.

```ruby
uri = URI("https://posta.esempio.it/api/v1/campaigns/#{campaign_cid}/trigger")
req = Net::HTTP::Post.new(uri)
req["Authorization"] = "Bearer #{token}"
req["Content-Type"] = "application/json"
req.body = { email: "cliente@esempio.it", data: { ORDER_ID: "A-1042", AMOUNT: "39.90" } }.to_json
res = Net::HTTP.start(uri.host, uri.port, use_ssl: true) { |http| http.request(req) }
```

## Webhook: ricevere notifiche

I webhook non si configurano dall'API ma dalla console, nella pagina **Webhook**.
Postino chiama il tuo endpoint quando succede qualcosa.

Eventi: `subscriber.created`, `subscriber.confirmed`, `subscriber.unsubscribed`,
`subscriber.bounced`, `subscriber.complained`, `campaign.finished`.

Ogni chiamata porta:

- `X-Postino-Event`: il nome dell'evento;
- `X-Postino-Signature`: firma HMAC-SHA256 del corpo, con il segreto del webhook, in
  esadecimale;
- corpo JSON: `{"event": "subscriber.bounced", "data": {...}}`.

**Verifica sempre la firma prima di fidarti del contenuto.** Se la risposta non è
2xx, Postino riprova con attese crescenti (1, 5, 15, 30 minuti, poi 1, 2, 4, 8 ore),
per un massimo di 9 tentativi.

**PHP:**

```php
$expected = hash_hmac('sha256', $rawBody, $webhookSecret);
if (! hash_equals($expected, $_SERVER['HTTP_X_POSTINO_SIGNATURE'] ?? '')) {
    http_response_code(401);
    exit;
}
```

**Ruby:**

```ruby
require "openssl"

expected = OpenSSL::HMAC.hexdigest("SHA256", webhook_secret, raw_body)
valid = Rack::Utils.secure_compare(expected, request.get_header("HTTP_X_POSTINO_SIGNATURE").to_s)
```

**Python:**

```python
import hashlib
import hmac

expected = hmac.new(webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()
valid = hmac.compare_digest(expected, request.headers.get("X-Postino-Signature", ""))
```

Nota: la firma va calcolata sul corpo **grezzo** della richiesta, prima di
qualsiasi decodifica JSON.

## Un piccolo client riutilizzabile

Per non ripetere l'intestazione in ogni chiamata, incapsula le richieste in una
classe o in una funzione. Esempio in Python:

```python
class Postino:
    def __init__(self, base_url: str, token: str):
        self.base = base_url.rstrip("/") + "/api/v1"
        self.headers = {"Authorization": f"Bearer {token}"}

    def subscribe(self, list_cid: str, email: str, fields: dict | None = None, **extra):
        body = {"email": email, "fields": fields or {}, **extra}
        return requests.post(f"{self.base}/lists/{list_cid}/subscriptions",
                             headers=self.headers, json=body, timeout=10)
```

Gli stessi principi valgono per PHP (una classe con Guzzle) e per Ruby (un modulo con
`Net::HTTP`).
