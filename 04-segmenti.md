# 4. Segmenti

## Cos'è un segmento

Un segmento è un filtro salvato sugli iscritti: sceglie chi rientra in base a campi
e stato. Non è una lista separata: gli iscritti restano dove sono, il segmento ne
seleziona un sottoinsieme.

Un segmento appartiene al namespace e vale su **tutte le liste** del namespace. Puoi
quindi definirlo una volta e usarlo in più campagne.

## Creare un segmento

Dalla pagina della lista, nel pannello **Segmenti**, oppure dal selettore dei
destinatari di una campagna:

1. Clicca **+ Nuovo segmento** e dai un nome.
2. Aggiungi una o più regole, nella forma **campo → confronto → valore**. Per
   esempio: `FIRST_NAME` **è uguale a** `Marco`, oppure `CITTÀ` **è compilato**.
   Confronti disponibili: è uguale a, è diverso da, contiene, è maggiore di, è
   minore di, è compilato, è vuoto.
3. Salva. Tutte le regole devono valere insieme (E logico).

Ogni segmento considera solo gli **iscritti attivi**: chi si è disiscritto o è in
attesa di conferma non rientra.

## Usare un segmento in una campagna

Nel box impostazioni della campagna, il campo **Destinatari** accetta liste e
segmenti. Scrivi il nome: compaiono in tempo reale le liste e i segmenti che
corrispondono, ciascuno con il suo tipo (**Lista** o **Segmento**). Se non esiste
ancora il segmento che ti serve, scegli **+ Crea segmento** e definilo sul posto.

Un iscritto che rientra in più destinatari riceve la campagna **una sola volta**.

## Modificare un segmento

Per ora un segmento si crea ma non si modifica dalla console: per cambiarne le
regole, creane uno nuovo. Le campagne già inviate non cambiano.
