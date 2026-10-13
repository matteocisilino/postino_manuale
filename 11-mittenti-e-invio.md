# 11. Mittenti e invio

Un **mittente** (configurazione di invio) raccoglie tutto il necessario per
spedire le campagne di un namespace: l'indirizzo da cui partono, il relay
SMTP che le invia materialmente, i limiti di velocità e il modo in cui
vengono gestite le mancate consegne (bounce). Lo trovi in **Mittenti**, per
ogni namespace su cui hai il ruolo di amministratore.

Puoi creare più mittenti per lo stesso namespace (per esempio uno per le
comunicazioni commerciali e uno per quelle informative) e scegliere, campagna
per campagna, quale usare.

Ogni campo del form ha accanto un punto interrogativo **?**: cliccandolo
compare una breve spiegazione, con un link a questa pagina per i dettagli.

## Trasporto

Scegli come vengono spedite le email di questo mittente:

- **Invio gestito da Postino:** Postino spedisce per te, firmando le email con
  il tuo dominio. L'email mittente deve appartenere a un [dominio di invio
  verificato](12-domini-di-invio.md). Non servono host, credenziali né
  impostazioni di bounce e DKIM: sono automatici.
- **Relay SMTP esterno:** usi il server SMTP di un tuo provider. In questo caso
  compili le sezioni seguenti (relay, bounce, DKIM).

## Nome

Serve solo per riconoscere questo mittente nell'elenco (per esempio
"Newsletter mensile"): non compare mai nelle email inviate né è visibile ai
destinatari.

## Mittente

- **Nome visualizzato:** il nome che il destinatario vede nella sua casella
  di posta, accanto all'indirizzo email (per esempio "Redazione Postino").
- **Email mittente:** l'indirizzo da cui parte la newsletter. Deve
  appartenere a un dominio che controlli davvero: è quello dominio che viene
  autenticato (SPF/DKIM) per non finire nello spam dei destinatari.

## Rispondi a

Indirizzo a cui arrivano le risposte dei destinatari, se diverso dall'email
del mittente. Lascia vuoto per usare quest'ultima anche per le risposte.

## Relay SMTP

Il relay è il server che invia materialmente le email per tuo conto. Te lo
fornisce il tuo provider di posta o di invio in massa (per esempio il tuo
hosting, Gmail/Google Workspace, o un servizio dedicato come quelli citati
più sotto).

- **Host e porta:** l'indirizzo del server e la porta su cui è in ascolto.
  Le combinazioni più comuni sono porta 587 con STARTTLS o porta 465 con
  TLS; la porta 25 senza cifratura è sconsigliata fuori da una rete locale.
- **Sicurezza:** il tipo di cifratura della connessione. STARTTLS e TLS
  proteggono le credenziali durante l'invio; scegli "Nessuna" solo se sei
  certo che la connessione resti in una rete locale sicura.
- **Utente e password:** le credenziali di accesso al relay, fornite dal tuo
  provider. Lascia vuoti se il relay non richiede autenticazione. Dopo il
  salvataggio la password non viene più mostrata in chiaro: lasciala vuota
  quando modifichi il mittente se non vuoi cambiarla.

Prima di salvare, usa il bottone **Verifica connessione SMTP** per controllare
che host, porta, sicurezza e credenziali siano corrette.

## Limiti di invio

- **Email al secondo:** quante email vengono inviate al massimo ogni
  secondo su questo relay. Un valore troppo alto rispetto a quanto concesso
  dal tuo provider può causare blocchi temporanei dell'invio.
- **Connessioni parallele:** quante connessioni SMTP vengono aperte
  contemporaneamente verso il relay durante un invio. Più connessioni
  velocizzano l'invio delle campagne grandi, ma vanno mantenute entro i
  limiti concessi dal provider.

Se non sai quali valori usare, parti da quelli proposti di default e
aumentali solo se il tuo provider ti garantisce limiti più alti.

## Gestione bounce

Un bounce è la notifica che un'email non è arrivata a destinazione (casella
piena, indirizzo inesistente...). Postino può riceverle in tre modi:

- **VERP (SMTP in ingresso):** ogni email porta un indirizzo di ritorno
  unico, e un bounce arriva direttamente a un server dedicato di Postino —
  vedi la sezione VERP più sotto.
- **Webhook del provider:** il provider di invio notifica Postino via
  webhook. Scegli anche il **servizio di invio** (se tra quelli noti) così
  Postino interpreta correttamente il formato delle notifiche.
- **Caselle IMAP:** Postino legge periodicamente una casella email dedicata
  ai bounce — vedi la sezione Bounce IMAP più sotto.

## VERP

Attivando VERP, ogni email in uscita porta un indirizzo di ritorno unico:
quando arriva un bounce, Postino sa con certezza a quale invio e a quale
destinatario corrisponde, senza doverlo indovinare dal testo della notifica.

Il **dominio VERP** (per esempio `bounce.tuodominio.it`) è il dominio usato
in quell'indirizzo di ritorno. Deve avere un record DNS che lo instrada al
server dei bounce di Postino: il tuo amministratore di sistema può indicarti
esattamente quale record impostare.

## Webhook bounce

Il **secret del webhook** è una chiave segreta che permette a Postino di
verificare che una notifica di bounce arrivi davvero dal provider scelto, e
non da chiunque indovini l'indirizzo del webhook. Il provider stesso ti
chiederà di inserire questa chiave nella sua configurazione.

## Bounce IMAP

- **Host e porta:** indirizzo e porta della casella email dedicata ai
  bounce. Tipicamente porta 993 con cifratura (la più comune) o 143 senza.
- **Utente e password:** le credenziali di accesso a quella casella.
- **Cartella:** la cartella da controllare per i bounce, di norma `INBOX`
  (la posta in arrivo).

## DKIM

DKIM è una firma digitale che dimostra che le email partono davvero dal
dominio che dicono di avere come mittente, e non sono contraffatte: è uno
dei fattori più importanti per non finire nello spam.

- **Dominio DKIM:** il dominio firmato — di norma coincide con il dominio
  dell'email mittente.
- **Selettore DKIM:** un'etichetta che indica quale chiave DKIM usare tra
  quelle pubblicate nel DNS del dominio. Serve soprattutto per poter
  cambiare la chiave in futuro senza interrompere l'invio.
- **Chiave privata DKIM:** la chiave usata per firmare le email in uscita.
  Va generata insieme a un record pubblico corrispondente, da pubblicare nel
  DNS del dominio mittente — il tuo amministratore di sistema ti fornisce i
  valori esatti da inserire.

## Avanzate

**List-Unsubscribe mailto:** un indirizzo email alternativo per la
disiscrizione in un clic, richiesto da alcuni client di posta oltre al link
di disiscrizione già incluso automaticamente in ogni campagna.
