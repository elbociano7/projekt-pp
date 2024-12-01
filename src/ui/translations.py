"""
Translation dictionary
"""
translations = {
    "title": "Tytuł",
    "author": "Autor",
    "year": "Rok wydania",
    "id": "Identyfikator",
    "itemcount": "Liczba egzemplarzy",
    "isbn": "ISBN (lub inny - TYP:KOD)",
    "image": "Zdjęcie",
    "reader_id": "Id czytelnika",
    "returned": "Zwrócono",
    "start_date": "Data wydania",
    "end_date": "Termin zwrotu",
    "firstname": "Imię",
    "lastname": "Nazwisko",
    "book": "Ksiązka",
    "loan_id": "Id wypozyczenia",
    "save": "Zapisz",
    "cancel": "Anuluj",
    "search": "Szukaj",
    "return": "Zwróć",
    "loan": "Wypozycz",
    "search_book_str": "Wyszukaj ksiązke \r\n(max 10 wyników. dostępne filtry: id:identyfikator, intitle:tekst, inauthor:tekst, isbn:tekst np: \"id:12345abcd\")",
    "search_reader_str": "Wyszukaj czytelnika (id/imie/nazwisko)",
    "search_book": "Wyszukaj ksiązkę",
    "search_reader": "Wyszukaj czytelnika",
    "loan_timespan": "Długość wypozyczenia (dni)",
    "active_loans": "Aktywne wypozyczenia",
    "back": "Powrót",
    "select": "Wybierz",
    "reader": "Czytelnik",
    "add": "Dodaj",
    'error': "Błąd",
    'no_results': "Brak wyników dla danej frazy.",
    "search_field_cannot_be_empty": "To pole wyszukiwania nie moze być puste!",
    'invalid_days': "Błędna ilość dni! \r\n (1-999)",
    "invalid_book_id": "Błędny identyfikator!",
    "empty_fields": "Pola nie mogą być puste!",
    "click_search": "Wciśnij przycisk \"Szukaj\".",
}

def Tr(key):
    """
    Translates the given key into its corresponding value if it exists
    in the translations dictionary; otherwise, it returns the key itself.

    :param key: The key to be translated.
    :type key: str
    :return: The corresponding value from the translations dictionary
             if it exists; otherwise, the key itself.
    :rtype: str
    """
    if key in translations.keys():
        return translations[key]
    else:
        return key