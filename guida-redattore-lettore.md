# Guida per redattori e lettori

Questa guida è per chi lavora su un namespace con il ruolo di **redattore** o di
**lettore**. Se sei amministratore, consulta il manuale generale.

## Cosa puoi fare, in breve

| Attività | Lettore | Redattore |
|---|:-:|:-:|
| Consultare liste, iscritti, campagne | sì | sì |
| Creare e modificare liste e iscritti | no | sì |
| Creare e modificare segmenti | no | sì |
| Creare e modificare template | no | sì |
| Creare e modificare campagne | no | sì |
| Inviare una prova di campagna | no | sì |
| Avviare un invio | no | sì |
| Caricare e usare immagini nella galleria | no | sì |
| Configurare il namespace, mittenti, chiavi API, webhook | no | no |
| Assegnare spazio e ruoli | no | no |

I permessi valgono nel namespace in cui hai il ruolo, e anche nei suoi figli.

## Se sei lettore

Il tuo lavoro è consultare. Nella barra laterale vedi le sezioni **Liste**,
**Campagne** e **Template**, ma i pulsanti di modifica non sono disponibili.

- **Liste:** apri una lista per vedere gli iscritti, i campi, lo stato di ciascun
  indirizzo e la verifica email.
- **Campagne:** apri una campagna per leggere il contenuto, lo stato dell'invio e i
  risultati. Non puoi modificarla, né avviarla o metterla in pausa.
- **Template:** puoi leggerli, non modificarli.

Se ti serve una modifica, chiedila a un redattore o all'amministratore del tuo
namespace.

## Se sei redattore

### Liste e iscritti

Il lavoro sulle liste è descritto nel manuale generale, nei capitoli *Liste e
iscritti* e *Segmenti*. In sintesi:

- crei una lista e ne scegli la modalità di opt-in;
- importi iscritti da un file CSV, o ne aggiungi uno alla volta;
- controlli lo stato di verifica degli indirizzi prima di inviare.

### Campagne

Per creare una campagna vai in **Campagne → Nuova**.

1. **Impostazioni.** Dai un nome, un oggetto e scegli il **mittente**.
2. **Destinatari.** Nel campo **Destinatari** scrivi il nome di una lista o di un
   segmento: compaiono i suggerimenti, ciascuno con il tipo (**Lista** o
   **Segmento**). Puoi anche spuntarli nel pannello dei segmenti. Se ti serve un
   segmento che non esiste, scegli **+ Crea segmento**. Un iscritto che rientra in
   più destinatari riceve la campagna una sola volta.
3. **Contenuto.** Usa l'editor visuale: trascini i blocchi nel messaggio. Se hai
   già un template, puoi partire da quello con **Parti da un template**.
4. **Immagini.** Usa **Galleria media** per scegliere un'immagine già caricata
   nel namespace, o per caricarne una nuova. Per inserirla, seleziona prima una
   colonna nel messaggio: l'immagine va dentro quella colonna. Con un doppio clic
   su un'immagine già presente, la galleria la sostituisce.
5. **Pagina da un sito.** Il pannello di scraping ti permette di copiare il
   contenuto di una pagina web, o gli ultimi articoli di un sito WordPress, e
   trascinarlo nel messaggio. Le immagini scaricate finiscono nella galleria del
   namespace e si riusano in altre campagne.
6. **Prova.** Prima di inviare, manda una prova al tuo indirizzo. La prova è
   consentita solo al tuo indirizzo.
7. **Salva.** Il pulsante **Salva** conserva la campagna senza inviarla.

Per avviare l'invio apri la campagna e usa il pulsante di avvio. Durante l'invio
puoi metterla in pausa, riprenderla o annullarla. Se un iscritto è in attesa di
verifica email, la campagna lo segnala nel banner e non lo includerà finché
l'esito non è disponibile.

### Galleria media e spazio

La **Galleria media** è condivisa da tutto il namespace: le immagini caricate da
un redattore sono visibili a tutti i colleghi del namespace.

- Il caricamento accetta JPG, PNG, GIF e WebP, fino a 5 MB per file.
- Lo spazio è del namespace. Nella finestra della galleria vedi lo spazio usato,
  quello libero e la soglia di avviso.
- Se lo spazio è esaurito, il caricamento è bloccato. Puoi liberare spazio
  eliminando immagini che non usi più, oppure chiedere all'amministratore di
  assegnarne altro.
- Eliminare un'immagine la toglie anche dalle campagne che la usano: le loro
  immagini smettono di comparire.

### Statistiche

Le statistiche di una campagna sono nella sua scheda. Il dettaglio delle viste
disponibili è descritto nel manuale generale, nel capitolo *Statistiche*, che è in
preparazione.

## Errori frequenti

- **"Spazio media esaurito"**: lo spazio del namespace è pieno. Elimina immagini
  inutilizzate o chiedi più spazio.
- **Un destinatario non compare**: il suo indirizzo non è ancora stato verificato,
  oppure è stato escluso (non valido, disiscritto, in una lista di soppressione).
- **Prova non inviata**: la prova si può mandare solo al tuo indirizzo.
- **Campagna non modificabile**: è già stata avviata. Una campagna in invio non
  si cambia.
