# 2. Namespace, ruoli e utenti

## Cos'è un namespace

Un namespace è un contenitore organizzativo: di solito un cliente, un'azienda o un
reparto. Dentro ci sono liste, iscritti, campagne, template, mittenti e la galleria
media. I namespace possono avere figli, per esempio un'azienda con più marchi.

Per creare un namespace serve essere amministratori del genitore; un namespace
radice lo crea solo il super admin. Dalla pagina **Namespace** puoi modificare il
nome e la descrizione, e spostare un namespace nel cestino.

## I ruoli

Ogni utente ha un ruolo per namespace:

| Ruolo | Può |
|---|---|
| **Lettore** | consultare liste, iscritti, campagne e statistiche, senza modificare nulla |
| **Redattore** | creare e modificare liste, iscritti, template e campagne; inviare le prove; caricare e gestire le immagini della galleria |
| **Amministratore** | tutto quanto sopra, più configurazione del namespace, mittenti, chiavi API, webhook, verifica email, assegnazione dello spazio e dei ruoli |

I permessi si ereditano: un amministratore del namespace padre lo è anche dei figli.

## Gestire gli utenti

Dalla pagina **Utenti e accessi** (riservata agli amministratori):

1. **Crea un utente:** inserisci email, namespace e ruolo. Viene generata una
   password provvisoria, mostrata una sola volta: comunicala all'utente, che la
   dovrà cambiare al primo accesso.
2. **Assegna un ruolo a un utente esistente:** scegli l'utente, il ruolo e conferma.
3. **Cambia il ruolo:** dal menu di ogni assegnazione.

Il riquadro in fondo alla pagina riassume i tre livelli, con la descrizione di ciò
che permettono.
