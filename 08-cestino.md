# Cestino e ripristino

Quando elimini un elemento di Postino, non viene cancellato subito: finisce nel
**Cestino**. Lì resta per 30 giorni, e puoi riportarlo indietro con un clic. Dopo
30 giorni viene cancellato in modo definitivo.

## Cosa finisce nel cestino

- **Namespace**
- **Utenti**
- **Liste**
- **Mittenti** (configurazioni di invio)
- **Template**
- **Webhook**
- **Campagne**, con le loro statistiche

Anche i **singoli indirizzi** (iscritti) finiscono nel cestino: eliminando un iscritto dalla
sua lista, lo ritrovi nel gruppo **Iscritti** e puoi riportarlo dentro la lista.

## Chi può eliminare

Chi elimina un elemento lo sposta nel cestino, a seconda del proprio ruolo:

- **Redattore**: può eliminare iscritti, liste, campagne e altri contenuti del namespace in
  cui lavora.

Una campagna si può eliminare quando non è in invio né in pausa: se è in corso, annullala
prima.
- **Amministratore del namespace**: può eliminare il namespace. Non può eliminare il
  proprio account: per quello serve un altro amministratore o il super admin.
- **Super admin**: può eliminare qualunque elemento, in tutti i namespace.

## Aprire il cestino

Dalla barra laterale, sezione **Sistema**, voce **Cestino**. La pagina raggruppa gli
elementi per tipo: Namespace, Utenti, Liste, Mittenti, Template, Webhook. Per ogni
elemento vedi il nome e la data in cui è stato eliminato.

Se non vedi la voce, il tuo ruolo non ha elementi da recuperare.

## Ripristinare un elemento

1. Apri il **Cestino**.
2. Trova l'elemento nel suo gruppo.
3. Premi **Ripristina**.

L'elemento torna esattamente come era, con i suoi collegamenti: le liste tornano con
i propri iscritti, i mittenti con le proprie impostazioni.

Possono ripristinare un elemento tutti gli utenti collegati ad esso e che hanno
accesso al suo namespace, nel ruolo che hanno: un redattore riporta indietro ciò che
può gestire, un amministratore ciò che può amministrare, il super admin tutto.

Eccezione: il ripristino di un utente è riservato al super admin.



## Scadenza dopo 30 giorni

Ogni notte, alle 03:15, Postino cancella in modo definitivo gli elementi nel cestino
da più di 30 giorni. Una volta cancellati non si recuperano.

I namespace figli vengono cancellati prima dei padri, perché un padre non si può
rimuovere finché ha figli.

## Svuotare il cestino subito

Il super admin può svuotare il cestino prima della scadenza con **Svuota cestino ora**.
Il pulsante cancella **tutto** il contenuto del cestino, in tutti i namespace, anche
gli elementi eliminati da pochi minuti. Il sistema chiede conferma: l'operazione non
si annulla.

Usalo solo se sei certo di non voler recuperare nulla. Altrimenti lascia che il
cestino si svuoti da solo dopo 30 giorni.

## Domande frequenti

**Un elemento nel cestino conta ancora nello spazio?**
Sì, finché non viene cancellato in modo definitivo: anche il cestino occupa spazio.

**Posso ripristinare un namespace i cui figli sono stati cancellati?**
Il namespace torna, ma i figli cancellati definitivamente non tornano. Se li vuoi
indietro, ricreali.

**Ho eliminato un elemento per errore e sono passati più di 30 giorni: posso recuperarlo?**
No. Dopo la cancellazione definitiva non è più recuperabile. Per evitarlo, controlla il
cestino entro 30 giorni dall'eliminazione.
