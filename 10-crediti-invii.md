# 10. Crediti sugli invii

> **Stato:** le regole di questo capitolo sono quelle definite per il listino. Il
> conteggio e l'addebito dei crediti sono in fase di implementazione: finché non sono
> attivi, gli invii non consumano ancora il saldo.

## L'unità: il credito

Tutto il consumo di Postino si misura in **crediti**:

- **1 € = 1.000 crediti**, quindi **1 credito = 0,001 €**, cioè 0,1 centesimi.
- **1 email = 1 credito** al prezzo base, cioè 0,1 centesimi.
- **1 GB di galleria al mese = 1.000 crediti**, cioè 1 €.
- **Ricarica minima: 10 € = 10.000 crediti.**

Il listino completo, con i prezzi aggiornati, è visibile al super admin, che può
modificarlo in qualsiasi momento.

## Cosa si conta

Si conta un credito per **ogni destinatario effettivo** di un invio. Un destinatario
è effettivo quando:

- è iscritto e attivo nelle liste della campagna (non in attesa di conferma e non
  disiscritto);
- non è in una lista di soppressione (bounce definitivo, reclamo, indirizzo non
  valido);
- se la verifica email è attiva, il suo esito è `valid`;
- se la campagna usa un segmento, rientra nelle sue regole.

Ogni indirizzo conta **una sola volta**, anche se compare in più liste o segmenti
selezionati.

Non contano gli indirizzi esclusi: chi è disiscritto o non valido non consuma
crediti.

## Il livello di invio in parallelo

Il numero di invii simultanei ha un costo: più invii in parallelo significano più
risorse e una consegna più rapida. Il livello scelto moltiplica il costo di ogni
email.

| Livello | Invii in parallelo | Moltiplicatore | Costo per email |
|---|---|---|---|
| Base | 1 | 1× | 1 credito |
| Standard | 2 | 1,5× | 1,5 crediti |
| Veloce | 4 | 2× | 2 crediti |
| Massimo | 8 | 3× | 3 crediti |

Il costo finale è sempre un numero intero di crediti: se il calcolo dà una frazione,
si arrotonda **per eccesso**.

## Sconti

Il super admin può applicare uno **sconto per namespace**, che si esprime come
moltiplicatore sul costo in crediti: per esempio `0,8` equivale a uno sconto del
20%. Lo sconto si applica dopo il moltiplicatore del livello.

## Formula

```
crediti = ceil( destinatari effettivi × costo base × moltiplicatore livello × sconto )
```

## Esempi

Con un costo base di 1 credito per email:

| Destinatari | Livello | Sconto | Crediti addebitati | Costo |
|---|---|---|---|---|
| 5.000 | Base (1×) | nessuno | 5.000 | 5 € |
| 5.000 | Standard (1,5×) | nessuno | 7.500 | 7,50 € |
| 5.000 | Standard (1,5×) | 0,8 | 6.000 | 6 € |
| 1.200 | Base (1×) | 0,9 | 1.080 | 1,08 € |

Con la ricarica minima da 10 € (10.000 crediti) puoi inviare, al livello base, circa
9.000 email dopo aver pagato 1.000 crediti di galleria per il primo mese.

## Quando si addebita

I crediti si addebitano al momento in cui la campagna viene **preparata per
l'invio**, cioè quando l'avvio mette in coda i messaggi. Il conteggio è fatto sui
destinatari di quel momento: un iscritto aggiunto dopo l'avvio non entra nel
conteggio di quell'invio.

## Le prove non si addebitano

Una prova inviata al proprio indirizzo non consuma crediti.

## Triggered

Un'email automatica inviata tramite l'API (campagne triggered) costa **1 credito**
per invio, al livello base. Nessun livello di parallelismo si applica, perché l'invio
è singolo.

## Saldo esaurito

Quando il saldo non basta per l'invio successivo:

- gli invii sono **sospesi** e la campagna resta in attesa di crediti;
- i caricamenti nella galleria media sono bloccati;
- le **iscrizioni continuano** a funzionare, e il tracciamento resta attivo.

Il saldo si ricarica dalla pagina dei crediti. Quando torna disponibile, la campagna
sospesa riprende dai destinatari non ancora serviti.

## Dove vedere il consumo

Il registro dei consumi del namespace (crediti addebitati per invio, con data e
campagna) sarà disponibile nella pagina dei crediti. Fino ad allora, il conteggio
dei destinatari si può verificare nella scheda della campagna, prima dell'avvio.

## Domande frequenti

**Un invio fallito costa comunque?** Il criterio definitivo per i messaggi non
consegnati è in fase di definizione: questo capitolo sarà aggiornato quando sarà
fissato.

**Posso cambiare il livello dopo l'avvio?** No: il livello si sceglie prima di
avviare la campagna.

**Il moltiplicatore è applicato a ogni email?** Sì, a ogni destinatario effettivo,
non solo alla campagna nel suo insieme.
