"""
Classwork 1: Gestore Annunci Immobiliari (Starter)

Questo modulo espone tre funzioni che gestiscono un semplice dizionario di annunci:
- add_listing(real_estate_list, name, details) -> dict
- remove_listing(real_estate_list, name) -> dict
- format_list(real_estate_list) -> str

Mantieni le funzioni esattamente come definite: i test automatici importano queste funzioni.
"""
from typing import Dict, Any

# Tipo di supporto per maggiore chiarezza (opzionale per gli studenti)
RealEstateList = Dict[str, Dict[str, Any]]

__all__ = [
    "add_listing",
    "remove_listing",
    "format_list",
]


def add_listing(real_estate_list: Dict[str, Dict[str, Any]], name: str, details: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Aggiunge o aggiorna un annuncio immobiliare nella lista.

    Parametri
    ---------
    real_estate_list : dict
        Il dizionario che rappresenta la lista degli annunci immobiliari.
        Le chiavi sono i nomi degli immobili (str), i valori sono dizionari con i dettagli.
    name : str
        Il nome dell'immobile da aggiungere o aggiornare (es. "Villa al Mare").
    details : dict
        Un dizionario contenente i dettagli dell'immobile, ad esempio:
        {"prezzo": 300000, "posizione": "Spiaggia", "descrizione": "..."}

    Comportamento
    -------------
    - Se l'immobile è già presente, i suoi dettagli devono essere aggiornati.
    - Se non è presente, deve essere aggiunto.

    Ritorno
    -------
    dict
        Il dizionario aggiornato degli annunci immobiliari (puoi restituire lo stesso oggetto).
    """
    # Placeholder di starter: restituisce la lista invariata.
    # Implementazione attesa: aggiungere/aggiornare la voce e restituire il dizionario aggiornato.
    return real_estate_list


def remove_listing(real_estate_list: Dict[str, Dict[str, Any]], name: str) -> Dict[str, Dict[str, Any]]:
    """Rimuove un annuncio immobiliare dalla lista (se esiste).

    Parametri
    ---------
    real_estate_list : dict
        Il dizionario degli annunci immobiliari.
    name : str
        Il nome dell'immobile da rimuovere.

    Comportamento
    -------------
    - Se l'immobile è presente nella lista, deve essere rimosso.
    - Se non è presente, la funzione non deve fare nulla.

    Ritorno
    -------
    dict
        Il dizionario aggiornato degli annunci immobiliari (puoi restituire lo stesso oggetto).
    """
    # Placeholder di starter: restituisce la lista invariata.
    # Implementazione attesa: rimuovere la voce se presente e restituire il dizionario aggiornato.
    return real_estate_list


def format_list(real_estate_list: Dict[str, Dict[str, Any]]) -> str:
    """Crea una stringa ben formattata con tutti gli immobili e i loro dettagli.

    Parametri
    ---------
    real_estate_list : dict
        Il dizionario degli annunci immobiliari.

    Comportamento
    -------------
    Deve creare una stringa formattata che elenca ogni immobile e i suoi dettagli.
    Esempio di riga (terminata con "\n"):
        "Villa al Mare: 300000, Spiaggia, Una bellissima villa con vista mare.\n"
    - Ogni immobile deve essere su una nuova riga (\n).
    - Se la lista è vuota, deve restituire una stringa vuota.

    Ritorno
    -------
    str
        La stringa formattata con tutti gli annunci.
    """
    # Placeholder di starter: restituisce stringa vuota.
    # Implementazione attesa: generare una riga per immobile con i dettagli separati da virgole e newline finale.
    return ""
