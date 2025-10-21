# Classwork 1: Gestore Annunci Immobiliari (Starter con pytest)

Questo repository è il punto di partenza per l'homework “Gestore Annunci Immobiliari”.
L’obiettivo è esercitarti con dizionari e liste in Python, cicli e funzioni, sviluppando
una piccola applicazione a riga di comando per gestire annunci immobiliari.

In questa versione “starter” trovi lo scheletro delle funzioni da completare e un
setup di test basato su `pytest`.

---

## Cosa devi fare

Implementa le tre funzioni nel file `real_estate.py`:

1. `add_listing(real_estate_list: dict, name: str, details: dict) -> dict`
   - Se l’immobile `name` è già presente in `real_estate_list`, aggiorna i suoi dettagli.
   - Se non c’è, aggiungilo con i dettagli forniti.
   - Ritorna il dizionario aggiornato.

2. `remove_listing(real_estate_list: dict, name: str) -> dict`
   - Se l’immobile `name` è presente, rimuovilo.
   - Se non è presente, non fare nulla.
   - Ritorna il dizionario aggiornato.

3. `format_list(real_estate_list: dict) -> str`
   - Crea una stringa che elenca ogni immobile e i suoi dettagli, una riga per immobile.
   - Esempio di riga: `"Villa al Mare: 300000, Spiaggia, Una bellissima villa con vista mare.\n"`
   - Se la lista è vuota, ritorna la stringa vuota `""`.

Mantieni le firme esattamente come sopra: i test le importano direttamente.

---

## Requisiti

- Python 3.10 o superiore (consigliato 3.11)
- `pytest` (viene installato da `requirements.txt`)

---

## Struttura del repository

```
.
├── .github/
│   └── workflows/
│       └── tests.yml        # Esegue i test su GitHub Actions (push/PR)
├── tests/
│   └── test_real_estate_public.py  # Esempi di test (segnati xfail)
├── .gitignore
├── pytest.ini               # Configurazione minimale di pytest
├── real_estate.py           # FILE DA COMPLETARE (funzioni richieste)
├── requirements.txt         # Dipendenze per i test
└── README.md
```

---

## Setup locale (consigliato)

1) Clona il repository (o accetta l’invito su GitHub Classroom, creando la tua copia).

2) Crea ed attiva un ambiente virtuale con `uv` (consigliato):

```bash
uv venv # solo la prima volta
source .venv/bin/activate  # sempre
```

Da Visual Studio Code, puoi selezionare il virtual environment `.venv` come interprete Python
dalla barra di stato in basso a destra.

3) Installa le dipendenze con `uv`:

```bash 
uv pip install -r requirements.txt # solo la prima volta
```

4) Esegui i test in locale con `uv`:

```bash
uv run pytest # ogni volta che vuoi verificare le tue implementazioni
```

Finché non implementi le funzioni, vedrai dei fallimenti nei test (FAIL).

---

## Dettagli di implementazione

- Il dizionario principale rappresenta la “lista” degli annunci: le chiavi sono i nomi degli
  immobili (stringhe), i valori sono dizionari con i dettagli (ad es. `{"prezzo": 300000, ...}`).
- `add_listing` deve aggiungere o aggiornare la voce (update). Puoi restituire lo stesso
  oggetto `real_estate_list` dopo la modifica.
- `remove_listing` deve rimuovere la voce se esiste, altrimenti non fa nulla. Anche qui puoi
  restituire lo stesso oggetto dopo la modifica.
- `format_list` deve creare una stringa; ogni immobile su una riga, terminata con `\n`.
  Se vuoi una formattazione deterministica, puoi ordinare alfabeticamente i nomi degli immobili.

Esempio di `real_estate_list`:

```python
data = {
    "Villa al Mare": {
        "prezzo": 300000,
        "posizione": "Spiaggia",
        "descrizione": "Una bellissima villa con vista mare.",
    },
    "Attico Centro": {
        "prezzo": 210000,
        "posizione": "Centro",
        "descrizione": "Attico con terrazza panoramica.",
    },
}
```

---

## Come funziona la valutazione con GitHub Classroom

- Quando fai push su GitHub, parte automaticamente un workflow (GitHub Actions) che esegue `pytest` usando `uv`.
- L’insegnante può avere test privati che non sono visibili nel repository studente ma vengono eseguiti
  durante l’autograding. Assicurati che le tre funzioni si comportino come richiesto.
- Continua a committare e pushare i tuoi progressi: vedrai lo stato dei test su GitHub.

---

## Suggerimenti

- Usa i metodi dei dizionari: assegnazione diretta, `in`, `pop`, `get`.
- Fai attenzione ai `None` e ai tipi dei valori (prezzo numerico, posizioni/descrizioni stringhe).
- Per `format_list`, cura bene spazi, virgole e `\n` finali.

---

## Domande frequenti (FAQ)

- “Devo mantenere l’ordine?” – Se non specificato, non è richiesto. Se vuoi stabilità nei test,
  ordina per nome immobile.
- “Posso modificare la firma delle funzioni?” – No. Mantieni esattamente i nomi e i parametri.
- “Dove scrivo il mio codice?” – In `real_estate.py`.

Buon lavoro! 💪
