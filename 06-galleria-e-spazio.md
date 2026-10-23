# 6. Galleria media e spazio

## La galleria

Le immagini usate nelle campagne e nei template vivono nella **galleria del
namespace**: appartengono al namespace, non a chi le ha caricate, così
restano disponibili a chiunque lavori su quel namespace. La trovi aprendo
**Galleria media** dall'editor visuale di una campagna o di un template.

- **Caricare un'immagine:** scegli il file dalla galleria. Formati accettati:
  JPG, PNG, GIF, WebP; dimensione massima 5 MB.
- **Nessun duplicato:** se carichi un'immagine già presente nella galleria del
  namespace (stesso contenuto, anche con nome file diverso), Postino
  riconosce il duplicato e riusa quella già caricata, senza occupare altro
  spazio.
- **Selezionare un'immagine:** nell'editor visuale, seleziona prima un
  elemento del canvas, poi apri la galleria e scegli l'immagine: viene
  inserita subito dopo l'elemento selezionato. Per sostituire un'immagine
  già nel messaggio, fai doppio clic su di essa.

## Lo spazio

Lo spazio della galleria è assegnato **a namespace**, non per singolo
utente. Lo trovi in **Spazio media**.

### Come funziona l'assegnazione

Lo spazio si distribuisce "a bottiglia", dall'alto verso il basso:

- Il super admin assegna la quota ai namespace radice.
- Chi amministra un namespace può a sua volta assegnare parte del proprio
  spazio **libero** ai propri sotto-namespace.
- Un namespace non può mai ricevere più spazio di quanto il suo genitore ha
  ancora libero, e non si può scendere sotto quanto è già stato ripartito ai
  figli.

Per ogni namespace la pagina mostra: quota assegnata, spazio usato dalla
galleria, spazio già ripartito ai figli, spazio libero.

### Assegnare lo spazio

Apri **Gestisci** sul namespace:

- **Quota del namespace:** la imposta chi amministra il namespace genitore
  (o il super admin, per i namespace radice). Si assegna in **multipli di
  1 GB** (minimo 1 GB; 0 revoca tutto lo spazio).
- **Soglia di avviso:** percentuale della quota oltre la quale compare un
  avviso di spazio quasi esaurito (default 80%, personalizzabile).
- **Assegna ai sotto-namespace:** se il namespace ha dei figli, puoi
  ripartire tra loro lo spazio libero rimasto, con lo stesso meccanismo.

Quando lo spazio usato supera la quota (stato "esaurito"), non è più
possibile caricare nuove immagini nella galleria di quel namespace finché
non viene liberato spazio (eliminando immagini non più usate) o la quota
non viene aumentata.
