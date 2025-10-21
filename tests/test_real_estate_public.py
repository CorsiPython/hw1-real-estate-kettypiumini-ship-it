import pytest

from real_estate import add_listing, remove_listing, format_list


def _lines(s: str):
    # Normalizza in righe non vuote, rimuovendo spazi ai bordi
    return [ln.strip() for ln in s.splitlines() if ln.strip()]


def test_import_and_signatures():
    assert callable(add_listing)
    assert callable(remove_listing)
    assert callable(format_list)


def test_format_list_vuota():
    assert format_list({}) == ""


def test_add_listing_aggiunge_nuovo():
    data = {}
    data = add_listing(data, "Villa al Mare", {
        "prezzo": 300000,
        "posizione": "Spiaggia",
        "descrizione": "Una bellissima villa con vista mare.",
    })
    assert "Villa al Mare" in data
    assert isinstance(data["Villa al Mare"], dict)
    assert data["Villa al Mare"].get("prezzo") == 300000


def test_add_listing_aggiorna_esistente():
    data = {}
    data = add_listing(data, "Attico Centro", {
        "prezzo": 200000,
        "posizione": "Centro",
        "descrizione": "Attico con terrazza panoramica.",
    })
    data = add_listing(data, "Attico Centro", {
        "prezzo": 210000,
        "posizione": "Centro",
        "descrizione": "Attico con terrazza panoramica.",
    })
    assert data["Attico Centro"]["prezzo"] == 210000


def test_remove_listing_rimuove_se_presente():
    data = {}
    data = add_listing(data, "Monolocale", {"prezzo": 80000, "posizione": "Periferia", "descrizione": "Compresso ma funzionale."})
    data = remove_listing(data, "Monolocale")
    assert "Monolocale" not in data


def test_remove_listing_silenzioso_se_assente():
    data = {}
    # Non deve sollevare eccezioni
    data = remove_listing(data, "Inesistente")
    assert data == {}


def test_format_list_singolo_annuncio():
    data = {
        "Villetta": {"prezzo": 120000, "posizione": "Campagna", "descrizione": "Tranquilla e luminosa."}
    }
    out = format_list(data)
    # Accettiamo qualsiasi ordine dei dettagli ma la riga deve contenere le parti principali
    assert "Villetta" in out
    assert "120000" in out
    assert "Campagna" in out
    assert "Tranquilla" in out


def test_format_list_più_annunci_una_riga_per_annuncio():
    data = {
        "A": {"prezzo": 1, "posizione": "X", "descrizione": "d1"},
        "B": {"prezzo": 2, "posizione": "Y", "descrizione": "d2"},
    }
    out_lines = _lines(format_list(data))
    # Due righe, una per ogni immobile
    assert len(out_lines) == 2
    assert any(ln.startswith("A:") for ln in out_lines)
    assert any(ln.startswith("B:") for ln in out_lines)


def test_format_list_contenuti_attesi():
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
    out_lines = _lines(format_list(data))
    # Verifica che ogni riga contenga i dettagli principali
    assert any("Villa al Mare" in ln and "300000" in ln and "Spiaggia" in ln for ln in out_lines)
    assert any("Attico Centro" in ln and "210000" in ln and "Centro" in ln for ln in out_lines)
