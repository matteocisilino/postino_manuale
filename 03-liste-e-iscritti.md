# 3. Liste e iscritti

## Creare una lista

Vai in **Liste → Nuova lista**. Compila:

- **Namespace:** dove vive la lista.
- **Nome** e **descrizione** (facoltativa).
- **Modalità di opt-in**: come entrano gli iscritti (vedi sotto).
- **Verifica email con recipientcheck**: attiva o disattiva il controllo degli
  indirizzi per questa lista. Lo trovi sotto la modalità di opt-in.

Il riquadro della verifica mostra il saldo crediti del namespace e il costo di una
verifica, così sai quanto costa prima di creare la lista.

## Le modalità di opt-in

Il simbolo **?** accanto alla modalità apre la spiegazione delle quattro scelte:

- **Singolo (predefinito):** l'iscritto entra subito, senza mail di conferma. Usala
  solo se hai già un consenso valido, per esempio iscrizioni fatte sul tuo sito.
- **Doppio opt-in:** l'iscritto resta in attesa finché non clicca il link della mail
  di conferma. È la scelta più sicura per il consenso e la reputazione.
- **Doppio solo se non valido:** con la verifica attiva, un indirizzo valido entra
  subito; uno incerto (`risky` o `unknown`) riceve la conferma; uno non valido viene
  escluso. Senza verifica si comporta come il doppio opt-in.
- **Singolo con conferma per indirizzi incerti:** entrano subito; quelli incerti
  tornano in attesa e ricevono la conferma. Senza verifica si comporta come il singolo.

Puoi cambiare la modalità in qualsiasi momento dalla pagina della lista, con il
pulsante **Modifica**. La modifica vale per le iscrizioni future: chi è già nella
lista non cambia stato.

## La pagina della lista

Aprendo una lista vedi:

- la riga con **modalità di opt-in**, **stato della verifica** e **saldo crediti**;
- il pannello **Importa CSV**;
- i **Campi personalizzati** e i **Segmenti**;
- la tabella degli **Iscritti**, con stato e verifica email di ciascuno.

## Importare iscritti da CSV

Nella pagina della lista, in **Importa CSV**:

1. Clicca **Scegli file CSV** e seleziona il file (`.csv` o `.txt`).
2. Verifica la mappatura: a sinistra la colonna del file, a destra il campo di
   Postino. La colonna con l'email è obbligatoria.
3. Clicca **Importa**. Il file viene elaborato in background; lo stato si segue
   mentre avanza.

Gli iscritti importati entrano come **singoli**, anche se la lista è a doppio
opt-in: il file rappresenta già il consenso di chi l'ha fornito. Se la verifica
email è attiva, gli indirizzi vengono controllati come gli altri.

## Aggiungere un iscritto a mano

Nella tabella degli iscritti usa **Aggiungi iscritto**: inserisci l'email e i campi
personalizzati. La verifica email, se attiva per la lista, parte dopo l'inserimento.

## Esportare la lista

Dalla pagina della lista, **Esporta CSV** scarica tutti gli iscritti con i loro campi.

## Verifica email

Quando la verifica è attiva, gli indirizzi nuovi vengono controllati da
recipientcheck in background. L'esito appare nella colonna **Verifica email**:

- **valida:** può ricevere le campagne;
- **incerta** (`risky` o `unknown`): non riceve campagne finché non diventa valida;
- **non valida:** viene esclusa dagli invii futuri.

Nella pagina della campagna un banner indica quanti destinatari sono ancora in
attesa di verifica: la campagna parte solo con gli indirizzi già esaminati.
