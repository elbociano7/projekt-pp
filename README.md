# PROJEKT

## Uruchomienie aplikacji

### Wymagania

- Python w wersji `>=3.13` (z powodu problemu z biblioteką tkinter na starszych wersjach na niektórych systemach)
- Zewnętrzne biblioteki zawarte w pliku `requirements.txt` 
- Baza danych `MySQL` w wersji `>=8.0.33`

### Przygotowanie

- Instalacja pythona w odpowiedniej wersji
- __tylko na macOS__ instalacja biblioteki python-tk: `brew install python-tk`
- Instalacja bibliotek pythona z pliku `requirements.txt`
- Utworzenie oraz ruchomienie bazy danych (np za pomocą pakietu `xampp` lub `lampp`)
- Uzupełnienie konfiguracji bazy danych w pliku `src/configuration.py`

### Uruchomienie
uruchomienie:
- za pomocą komendy `python3 run.py` lub `py run.py`
- korzystając z `.venv` po wcześniejszym jego utworzeniu: `.venv/bin/python3.13 run.py`

> Inne informacje o programie zawarte są w pliku `docs/program.md`