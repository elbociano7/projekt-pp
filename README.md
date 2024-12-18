# PROJEKT

## Pobieranie

Najłatwiej wejść w release'y i tam z pierwszego (i ostatniego) pobrać paczkę z kodem źródłowym. Następnie rozpakowujemy archiwum i w nim robimy odpowiednie rzeczy wg. instrukcji na dole.
Opcja druga to klonowanie repozytorium za pomocą gita (trzeba mieć gita zainstalowanego): `git clone https://github.com/elbociano7/projekt-pp`

## Uruchomienie aplikacji

### Wymagania

> Do poprawnego działania interfejsu zalecana jest wersja pythona 3.13. Starsze wersje mogą powodować błędy

- Python w wersji `>=3.13` (z powodu problemu z biblioteką tkinter na starszych wersjach na niektórych systemach)
- Zewnętrzne biblioteki zawarte w pliku `requirements.txt` w odpowiadających im wersjach.
- Baza danych `MySQL` w wersji `>=8.0.33`

### Przygotowanie

- Instalacja pythona w odpowiedniej wersji
- __tylko na macOS:__ instalacja biblioteki python-tk: `brew install python-tk`
- Instalacja bibliotek pythona z pliku `requirements.txt`:  `pip install -r requirements.txt`
- Utworzenie oraz ruchomienie bazy danych (np za pomocą pakietu `xampp` lub `lampp`)
- Uzupełnienie konfiguracji bazy danych w pliku `src/configuration.py` Na domyślnej konfiguracji bazy danych z pakietu `xampp` z utworzoną bazą `pp-data` powinna działać domyślna konfiguracja programu, jednak nie jest to pewne.

### Uruchomienie

- za pomocą komendy `python3 run.py` lub `py run.py`
- korzystając z `.venv` po wcześniejszym jego utworzeniu: `.venv/bin/python3.13 run.py`

> Inne informacje o programie zawarte są w pliku `docs/program.md`
