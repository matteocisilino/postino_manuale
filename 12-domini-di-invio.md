# 12. Domini di invio

Per inviare le newsletter con l'invio gestito da Postino, il dominio del
mittente deve essere un **dominio di invio verificato**. Lo configuri in
**Domini di invio**, per ogni namespace su cui hai il ruolo di amministratore.

Il motivo è la reputazione: i provider (Gmail, Outlook, Yahoo…) accettano bene
solo le email che dimostrano di provenire davvero dal dominio indicato. Per
questo Postino ti fa pubblicare alcuni record nel DNS e controlla che ci siano
prima di consentire l'invio.

## Dominio di invio

È il dominio che compare nell'indirizzo del mittente, per esempio
`esempio.com` o `news.esempio.com`. Puoi usare il dominio principale o un
sottodominio dedicato. Devi poter aggiungere record nel suo DNS (pannello del
tuo provider di dominio o del tuo hosting).

I mittenti gestiti da Postino possono usare qualunque indirizzo di quel
dominio (o dei suoi sottodomini).

## Record da pubblicare

Dopo aver aggiunto il dominio, la pagina mostra una tabella con i record da
inserire nel DNS. Accanto a ogni valore c'è il pulsante per copiarlo.

- **Prova di proprietà (TXT):** dimostra che il dominio è tuo. Se il dominio è
  un sottodominio di una zona di Postino non serve.
- **Firma DKIM (due CNAME):** permettono a Postino di firmare le email a nome
  del tuo dominio. Sono due per consentire la rotazione delle chiavi.
- **Bounce (CNAME):** fa tornare a Postino le email respinte, così gli
  indirizzi inesistenti vengono riconosciuti e non ricevono più invii.
- **DMARC (TXT):** richiesto da Gmail e Yahoo. Se il dominio ha già un record
  DMARC va bene quello esistente.

Alcuni consigli ricorrenti:

- Se usi Cloudflare, disattiva il proxy (nuvola arancione) sui CNAME: devono
  essere "solo DNS".
- Alcuni pannelli aggiungono da soli il dominio in fondo al nome: se il nome
  compare ripetuto (`…esempio.com.esempio.com`), togli la parte finale.
- Copia i valori senza spazi né virgolette aggiuntive.

## Verifica

Premi **Verifica ora** dopo aver pubblicato i record. Postino interroga
direttamente i nameserver del tuo dominio, quindi una correzione si vede
subito. Accanto a ogni record compare l'esito; se qualcosa non va, trovi cosa
è stato letto e un suggerimento per correggere.

Se il dominio è appena stato configurato, la propagazione del DNS può
richiedere qualche minuto. Postino ricontrolla da solo ogni 15 minuti finché il
dominio non è attivo.

## Stati del dominio

- **In attesa della prova di proprietà / dei record DNS:** non puoi ancora
  inviare con questo dominio.
- **Attivo:** puoi inviare. Postino ricontrolla i record una volta al giorno.
- **Sospeso:** i record non risultano più corretti (per esempio sono stati
  rimossi). Le campagne in corso vanno **in pausa** e ripartono da sole appena
  i record tornano validi. Le campagne messe in pausa da te non ripartono da
  sole.

Un dominio attivo viene sospeso solo dopo due controlli falliti di fila: un
problema temporaneo del DNS non interrompe gli invii.

## Eliminare un dominio

Eliminando un dominio, i mittenti che lo usano non potranno più inviare finché
non ne verifichi un altro.
