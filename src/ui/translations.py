"""
Translation dictionary
"""
translations = {
    "title": "Tytuł",
    "author": "Autor",
    "year": "Rok wydania",
    "id": "Identyfikator",
    "itemcount": "Liczba egzemplarzy",
    "isbn": "ISBN",
    "image": "Zdjęcie",
    "reader_id": "Id czytelnika",
    "returned": "Zwrócono",
    "start_date": "Data wydania",
    "end_date": "Termin zwrotu",
    "firstname": "Imię",
    "lastname": "Nazwisko",
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