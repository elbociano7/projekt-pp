# Działanie programu #

Program działa wg wcześniejszych załozeń.


- Mozliwe jest wyszukiwanie ksiazek, uzytkownikow
- Wypozyczanie ksiazek
- Sprawdzanie aktywnych wypozyczen (w tym sprawdzenie 
najstarszych)
- Zwracanie ksiazek
- Konfiguracja domyslnej ilosci ksiazki
(w konfiguracji programu: plik `src/configuration.py`)

Dane dodawane są do bazy danych podczas wyszukiwania. Przy wejściu w widok ksiązki pobierana jest jej okładka a następnie jest zapisywana w pamięci cache.

> Z powodu błędów obsługi biblioteki `tkinter` 
> mozliwe są chwilowe błędy w zmianie widoku programu
> na systemie macOS (niezaobserwowane na Windows ale
> istnieje ryzyko ze tez się moze pojawić). Jezeli po 
> zmianie widoku nie pojawia się nowy widok nalezy 
> przesunąć lekko okno programu lekko w którąkolwiek 
> stronę.