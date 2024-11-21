# DRIVERS #

## STRUKTURA ##

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
