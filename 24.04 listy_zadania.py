# 1. Zadanie: Oblicz sumę wszystkich elementów na liście
# Dane: [1, 2, 3, 4, 5]
from operator import index

dane = [1, 2, 3, 4, 5]
suma = sum(dane)
print(suma)

# 2. Zadanie: Znajdź największy element w liście
# Dane: [15, 3, 10, 4, 22]
dane = [15, 3, 10, 4, 22]
najwiekszy = max(dane)
print(najwiekszy)

# 3. Zadanie: Usuń wszystkie wystąpienia określonej liczby z listy
# Dane: [2, 5, 3, 5, 7, 5]
usuwana_liczba = 5
dane = [2, 5, 3, 5, 7, 5]
po_usunieciu = [item for item in dane if item != usuwana_liczba]
print(po_usunieciu)

# 4. Zadanie: Zwróć nową listę, w której wszystkie elementy są pomnożone przez 2
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
processed_dane = [item * 2 for item in dane]
print(processed_dane)

# 5. Zadanie: Sprawdź, czy lista zawiera określoną liczbę
# Dane: [3, 7, 12, 9, 20]
szukana_liczba = 9
dane = [3, 7, 12, 9, 20]
if szukana_liczba in dane:
    print('istnieje na liście')
else:
    print('nie istnieje na liście')

# 6. Zadanie: Zwróć listę posortowaną rosnąco
# Dane: [5, 2, 9, 1, 6, 7]
dane = [5, 2, 9, 1, 6, 7]
dane.sort()
print(dane)

# 7. Zadanie: Zwróć listę posortowaną malejąco
# Dane: [1, 3, 8, 4, 7]
dane = [1, 3, 8, 4, 7]
dane.sort(reverse=True)
print(dane)

# 8. Zadanie: Zwróć tylko unikalne elementy z listy (usuń duplikaty)
# Dane: [1, 2, 3, 2, 4, 1, 5]
dane = [1, 2, 3, 2, 4, 1, 5]
unikalne = list(set(dane))
print(unikalne)
# lub
dane = [1, 2, 3, 2, 4, 1, 5]
unikalne_loop = []
for item in dane:
    if item not in unikalne_loop:
        unikalne_loop.append(item)
print(unikalne_loop)

# 9. Zadanie: Zwróć liczbę wystąpień określonego elementu w liście
# Dane: [10, 20, 20, 30, 20, 40]
# Szukana liczba: 20
szukana_liczba = 20
dane = [10, 20, 20, 30, 20, 40]
liczba_wystapien = dane.count(szukana_liczba)
print(liczba_wystapien)

# 10. Zadanie: Zwróć wszystkie liczby większe niż 10
# Dane: [5, 15, 10, 25, 8, 12]
dane = [5, 15, 10, 25, 8, 12]
wieszke_niz_10 = [item for item in dane if item > 10]
print(wieszke_niz_10)

# 11. Zadanie: Zwróć elementy na parzystych indeksach
# Dane: [10, 20, 30, 40, 50, 60]
dane = [10, 20, 30, 40, 50, 60]
parzyste_indeksy = dane[::2]
print(parzyste_indeksy)

# 12. Zadanie: Oblicz średnią z elementów listy
# Dane: [3, 5, 7, 9, 2]
dane = [3, 5, 7, 9, 2]
suma = sum(dane)
ilosc = len(dane)
srednia = suma / ilosc
print(srednia)

# 13. Zadanie: Odwróć kolejność elementów w liście
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
odwrocone = dane[::-1]
print(odwrocone)

# 14. Zadanie: Zwiększ każdy element w liście o 3
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
dane_zwiekszone = [item * 3 for item in dane]
print(dane_zwiekszone)

# 15. Zadanie: Wstaw element w określoną pozycję w liście
# Dane: [1, 2, 3, 4, 5]
# Pozycja: 2
# Element do wstawienia: 99
dane = [1, 2, 3, 4, 5]
pozycja = 2
element_do_wstawienia = 99
dane.insert(pozycja - 1, element_do_wstawienia)
print(dane)

# 16. Zadanie: Usuń element na określonym indeksie
# Dane: [10, 20, 30, 40, 50]
# Indeks do usunięcia: 3
dane = [10, 20, 30, 40, 50]
indeks_do_usunięcia = 3
dane.pop(indeks_do_usunięcia)
print(dane)

# 17. Zadanie: Zwróć listę tylko z liczbami parzystymi
# Dane: [1, 2, 3, 4, 5, 6]
dane = [1, 2, 3, 4, 5, 6]
parzyste = [item for item in dane if item % 2 == 0]
print(parzyste)

# 18. Zadanie: Połącz dwie listy w jedną
# Dane: [1, 2, 3] oraz [4, 5, 6]
daneA = [1, 2, 3]
daneB = [4, 5, 6]
daneA.extend(daneB)
print(daneA)

# 19. Zadanie: Zrób z listy słownik, gdzie klucze to elementy, a wartości to ich liczba wystąpień
# Dane: [1, 2, 2, 3, 3, 3, 4]
from collections import Counter
dane = [1, 2, 2, 3, 3, 3, 4]
slownik = Counter(dane)
print(slownik)
# lub
slownik = {}
for element in dane:
    if element in slownik:
        slownik[element] += 1
    else:
        slownik[element] = 1
print(slownik)

# 20. Zadanie: Zrób nową listę, zawierającą tylko te liczby, które są większe od średniej
# Dane: [5, 12, 7, 9, 3, 8]
dane = [5, 12, 7, 9, 3, 8]
suma = sum(dane)
ilosc = len(dane)
srednia = suma / ilosc
wieksze_od_sredniej = [item for item in dane if item > srednia]
print(wieksze_od_sredniej)

# —------------------------------------------------------------------------------------------------------------------------
# Zadanie: Zgrupuj elementy w słownik, gdzie klucze to pierwsze litery
# słów
# Dane: ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
# Opis: Utwórz słownik, gdzie klucze to pierwsze litery słów, a wartości to listy słów
# zaczynających się od tej litery.
dane = ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
zgrupowane = {}
for item in dane:
    pierwsza_litera = item[0]
    if pierwsza_litera in zgrupowane:
        zgrupowane[pierwsza_litera].append(item)
    else:
        zgrupowane[pierwsza_litera] = [item]
print(zgrupowane)
