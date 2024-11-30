# DRIVERS #

## STRUKTURA PLIKOW ##

```
nazwa/
|__ __main__.py #required
|__ dir1/
    |__ one.py
    |__ two.py
    ...

```

plik `__main__.py` powinien zawierać:
- zmienną `classname` zawierającą nazwę klasy
- klasę o nazwie zdefiniowanej w `classname` zawierającą odpowiednie metody

## METODY ##

- `get(field, value, object)` - szukanie jednego obiektu po wskazanej właściwości `field` odpowiadającej wartości `value`. Nazwa tabeli pobierana jest z obiektu `object` za pomocą metody `object.getTableName()`. Zwracany jest obiekt typu `object.__class__` z własciwościami odpowiadającymi danym z tabeli. \
 __Jezeli znaleziony zostanie więcej niz jeden obiekt zwracany jest tylko pierwszy__.
- `search(filters, object)` - wyszukiwanie obiektów wg filtrów z parametru `filters`. Zwraca tablicę ze wszystkimi wyszukaniami.
- `update(object)` - metoda uzywana do aktualizacji danych w bazie danych. Aktualizowana jest tabela `object.getTableName()` w miejscu gdzie kolumna `id` jest równa wartości `object.id`
- `update(object)` - metoda uzywana do tworzenia rekordów w bazie danych. Tworzony jest rekord w tabeli `object.getTableName()` z `id` równym `object.id` lub jeśli `object.id == Null` id tworzone jest wg. konfiguracji bazy danych.

Mozliwe jest wykorzystanie innych, własnych metod.
