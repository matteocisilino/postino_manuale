# Statistiche

Ogni campagna ha una pagina **Statistiche**, raggiungibile dal pulsante omonimo nella scheda della campagna. Mostra come è andato l'invio: chi ha ricevuto il messaggio, chi lo ha aperto, quali link ha cliccato, quando.

I numeri si calcolano quando apri la pagina: per vederli aggiornati mentre la campagna è in corso, ricarica la pagina. Restano disponibili anche dopo la fine dell'invio.

## Come leggere la pagina

### Indicatori in alto

- **Destinatari**: quanti messaggi sono stati preparati per la campagna. Sotto, quanti sono stati rimbalzati.
- **Consegnati**: messaggi accettati dal server di posta. Sotto, quanti sono falliti.
- **Aperture umane**: percentuale di consegnati che hanno aperto il messaggio. Sotto, il numero di iscritti.
- **Click**: percentuale di consegnati che hanno cliccato almeno un link.
- **Click su aperture**: di chi ha aperto, quanti hanno anche cliccato. È l'indicatore più utile per giudicare il contenuto.
- **Mediana prima apertura**: il tempo tipico che passa dall'invio alla prima apertura. Sotto, l'intervallo in cui cade la metà centrale degli iscritti.
- **Mediana primo click**: lo stesso, per il primo click.
- **Bot rilevati**: aperture e click fatti da sistemi automatici (vedi sotto).

### Aperture e click per ora

Due grafici con 24 colonne, una per ora del giorno in UTC. Ogni colonna conta gli iscritti che hanno aperto (o cliccato) per la prima volta in quell'ora. Passando il mouse sulla colonna si legge l'ora esatta.

Gli orari sono in UTC, cioè in tempo universale. In Italia l'ora legale è due ore dopo, quella solare un'ora dopo.

### Link

Una tabella con ogni link del messaggio, nell'ordine in cui compare:

- **Posizione**: il numero del link nel messaggio, dall'alto verso il basso.
- **Sezione**: il titolo che precede il link nel messaggio, quando c'è. È un'indicazione: un link in fondo al messaggio, dopo l'ultimo titolo, prende il titolo precedente.
- **Testo** e **destinazione**: il testo visibile e l'indirizzo a cui porta.
- **Click** e **Iscritti**: quanti click umani ha ricevuto il link, e da quanti iscritti diversi.
- **Caricamenti immagine**: quante volte un'immagine del messaggio è stata caricata.

Due link con lo stesso indirizzo, uno in alto e uno in fondo, hanno righe separate: così si vede quale dei due funziona.

### Client di posta e dispositivi

Due elenchi con le aperture umane per programma di posta (Apple Mail, Outlook, Gmail…) e per tipo di dispositivo (computer, telefono, tablet). Dove il programma non è riconoscibile la voce è "non rilevato".

### Per lista

Se la campagna ha raggiunto più liste, una riga per lista: destinatari, aperture e click umani. Serve a capire quale lista risponde meglio.

## Dettaglio iscritti

Sotto la tabella dei link c'è il dettaglio per iscritto: una riga per ogni destinatario, con:

- la prima apertura e il numero di aperture;
- il primo click e il numero di click;
- una colonna per ogni link del messaggio, con quanti click ha fatto quell'iscritto su quel link. Passando il mouse sulla cella si legge l'ora del primo click su quel link.

Il menu **Mostra** filtra le righe: tutti, hanno aperto, hanno cliccato, non hanno aperto. Con **Carica altri** si scorrono gli iscritti a blocchi di cento.

Per lavorare sui dati fuori da Postino usa **Scarica CSV**. Il file contiene tutti gli iscritti del filtro scelto, con una colonna per link. Si apre direttamente in Excel; il separatore è il punto e virgola.

Il dettaglio mostra indirizzi email: è un'informazione riservata. Non condividere il file con chi non deve vedere la lista.

## Bot e aperture automatiche

Alcuni sistemi non sono persone, ma seguono i link o caricano le immagini appena un messaggio arriva: sono i controlli di sicurezza delle aziende, o i servizi che generano anteprime. Postino li riconosce in tre modi:

- dal nome del sistema, quando è noto (per esempio i filtri antispam di grandi provider);
- quando l'apertura o il click arrivano pochi secondi dopo l'invio, troppo presto per una lettura;
- quando lo stesso evento si ripete in pochi istanti.

Le aperture e i click di questi sistemi non entrano nei numeri principali: compaiono solo come **Bot rilevati**. Un numero alto di bot su un link o un dominio può indicare che il messaggio viene scansionato dai filtri: vale la pena controllarne il contenuto.

## Limiti da conoscere

- **Aperture e Apple Mail.** Dal 2021 Apple Mail scarica le immagini di tutte le email, anche se l'utente non le legge. Le aperture da Apple Mail vanno quindi lette come "messaggio ricevuto", non come lettura. Il dato più affidabile è il click: per questo l'indicatore **Click su aperture** conta più dell'apertura da sola.
- **Solo per chi ha aperto le immagini.** Un messaggio senza immagini non può registrare l'apertura. Il numero di aperture è una stima per difetto.
- **Nessuna posizione geografica e nessun indirizzo IP.** Postino non registra dove si trova chi apre il messaggio, né il suo indirizzo di rete.
- **Storico.** Le campagne inviate prima dell'aggiornamento delle statistiche mostrano i dati per link in forma aggregata, senza le posizioni né le sezioni.
- **Conservazione.** Quanto restano i dati di tracciamento dipende dal piano del tuo namespace. Il super admin definisce il valore predefinito; l'admin del namespace può cambiarlo.

## Domande frequenti

**Perché il numero di aperture cambia nel tempo?**
Le aperture si registrano quando le immagini vengono caricate, e alcune arrivano con ritardo, per esempio quando un iscritto riapre la posta il giorno dopo.

**Perché un iscritto ha aperto ma non compare come "ha aperto"?**
Se la sua apertura è stata classificata come bot, non entra nei numeri principali. Controlla la colonna **Bot rilevati** e il dettaglio dell'iscritto.

**Posso vedere le statistiche di una campagna mentre è in invio?**
Sì. I numeri crescono man mano che i messaggi partono e gli iscritti rispondono; ricarica la pagina per l'ultimo dato. Le percentuali sono definitive solo a invio concluso.

## Eliminare una campagna

Le statistiche seguono la campagna. Quando sposti una campagna nel cestino, con lei
finiscono nel cestino anche le sue statistiche. Ripristinandola, tornano insieme. Dopo
30 giorni nel cestino la campagna e le statistiche vengono cancellate in modo definitivo.
