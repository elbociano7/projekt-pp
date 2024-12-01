# Działanie programu #

Program działa wg wcześniejszych załozeń.


- Mozliwe jest wyszukiwanie ksiazek, uzytkownikow
- Wypozyczanie ksiazek
- Sprawdzanie aktywnych wypozyczen (w tym sprawdzenie 
najstarszych)
- Zwracanie ksiazek
- Konfiguracja domyslnej ilosci ksiazki
(w konfiguracji programu: plik `src/configuration.py`)

Dane o ksiązkach dodawane są do bazy danych podczas wyszukiwania. Przy wejściu w widok ksiązki pobierana jest jej okładka a następnie jest zapisywana w pamięci cache.

### Obsługa ###

Wypozyczanie ksiązki jest mozliwe poprzez wejście w ksiazke > przycisk wypozycz > wybranie czytelnika > wpisanie ilosci dni (1-999). Zwrocenie mozliwe jest z poziomu czytelnika oraz ksiazki.

Domyslnie po dodaniu czytelnika jest on automatycznie wyszukiwany i aby go wybrać nalezy wcisnąć przycisk znajdujacy się przy uzytkowniku.

Wyszukiwanie ksiazek wymaga wpisania dowolnego ciagu znaków do paska wyszukiwania. Możliwe jest także użycie filtrów (`intitle:`, `inauthor:`, `isbn:`, `id:`), przy czym użycie filtru `id:` wymaga wpisania `id:` na początku pola wyszukiwania a następnie podania identyfikatora zasobu. Niepodanie identyfikatora zwraca błąd, natomiast podanie błędnego identyfikatora powoduje niepokazanie się żadnego wyniku wyszukiwania.

Podczas wyszukiwania czytelników automatycznie sprawdzane jest występowanie ciągu znaku lub podobieństwo ciągu znaków do kolejnych pól: Identyfikator, Imię, Nazwisko. Aby wyszukać konkretną osobę najlepiej jest wpisać w pole wyszukiwania identyfikator czytelnika opcjonalnie z imieniem a następnie nazwiskiem oddzielonymi spacją (koniecznie w tej kolejności).



> Z powodu błędów obsługi biblioteki `tkinter` 
> mozliwe są chwilowe błędy w zmianie widoku programu
> na systemie macOS (niezaobserwowane na Windows ale
> istnieje ryzyko ze tez się moze pojawić). Jezeli po 
> zmianie widoku nie pojawia się nowy widok nalezy 
> przesunąć lekko okno programu lekko w którąkolwiek 
> stronę.