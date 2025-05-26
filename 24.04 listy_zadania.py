# 1. Zadanie: Oblicz sumę wszystkich elementów na liście
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
suma = sum(dane)
print(f'Zad 1: {suma}')

# 2. Zadanie: Znajdź największy element w liście
# Dane: [15, 3, 10, 4, 22]
dane = [15, 3, 10, 4, 22]
najwiekszy = max(dane)
print(f'Zad 2: {najwiekszy}')

# 3. Zadanie: Usuń wszystkie wystąpienia określonej liczby z listy
# Dane: [2, 5, 3, 5, 7, 5]
usuwana_liczba = 5
dane = [2, 5, 3, 5, 7, 5]
po_usunieciu = [item for item in dane if item != usuwana_liczba]
print(f'Zad 3: {po_usunieciu}')

# 4. Zadanie: Zwróć nową listę, w której wszystkie elementy są pomnożone przez 2
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
processed_dane = [item * 2 for item in dane]
print(f'Zad 4: {processed_dane}')

# 5. Zadanie: Sprawdź, czy lista zawiera określoną liczbę
# Dane: [3, 7, 12, 9, 20]
szukana_liczba = 9
dane = [3, 7, 12, 9, 20]
if szukana_liczba in dane:
    print('Zad 5: istnieje na liście')
else:
    print('Zad 5: nie istnieje na liście')

# 6. Zadanie: Zwróć listę posortowaną rosnąco
# Dane: [5, 2, 9, 1, 6, 7]
dane = [5, 2, 9, 1, 6, 7]
dane.sort()
print(f'Zad 6: {dane}')

# 7. Zadanie: Zwróć listę posortowaną malejąco
# Dane: [1, 3, 8, 4, 7]
dane = [1, 3, 8, 4, 7]
dane.sort(reverse=True)
print(f'Zad 7: {dane}')

# 8. Zadanie: Zwróć tylko unikalne elementy z listy (usuń duplikaty)
# Dane: [1, 2, 3, 2, 4, 1, 5]
dane = [1, 2, 3, 2, 4, 1, 5]
unikalne = list(set(dane))
print(f'Zad 8: {unikalne}')
# lub
dane = [1, 2, 3, 2, 4, 1, 5]
unikalne_loop = []
for item in dane:
    if item not in unikalne_loop:
        unikalne_loop.append(item)
print(f'Zad 8: {unikalne_loop}')

# 9. Zadanie: Zwróć liczbę wystąpień określonego elementu w liście
# Dane: [10, 20, 20, 30, 20, 40]
# Szukana liczba: 20
szukana_liczba = 20
dane = [10, 20, 20, 30, 20, 40]
liczba_wystapien = dane.count(szukana_liczba)
print(f'Zad 9: {liczba_wystapien}')

# 10. Zadanie: Zwróć wszystkie liczby większe niż 10
# Dane: [5, 15, 10, 25, 8, 12]
dane = [5, 15, 10, 25, 8, 12]
wieszke_niz_10 = [item for item in dane if item > 10]
print(f'Zad 10: {wieszke_niz_10}')

# 11. Zadanie: Zwróć elementy na parzystych indeksach
# Dane: [10, 20, 30, 40, 50, 60]
dane = [10, 20, 30, 40, 50, 60]
parzyste_indeksy = dane[::2]
print(f'Zad 11: {parzyste_indeksy}')

# 12. Zadanie: Oblicz średnią z elementów listy
# Dane: [3, 5, 7, 9, 2]
dane = [3, 5, 7, 9, 2]
suma = sum(dane)
ilosc = len(dane)
srednia = suma / ilosc
print(f'Zad 12: {srednia}')

# 13. Zadanie: Odwróć kolejność elementów w liście
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
odwrocone = dane[::-1]
print(f'Zad 13: {odwrocone}')

# 14. Zadanie: Zwiększ każdy element w liście o 3
# Dane: [1, 2, 3, 4, 5]
dane = [1, 2, 3, 4, 5]
dane_zwiekszone = [item * 3 for item in dane]
print(f'Zad 14: {dane_zwiekszone}')

# 15. Zadanie: Wstaw element w określoną pozycję w liście
# Dane: [1, 2, 3, 4, 5]
# Pozycja: 2
# Element do wstawienia: 99
dane = [1, 2, 3, 4, 5]
pozycja = 2
element_do_wstawienia = 99
dane.insert(pozycja - 1, element_do_wstawienia)
print(f'Zad 15: {dane}')

# 16. Zadanie: Usuń element na określonym indeksie
# Dane: [10, 20, 30, 40, 50]
# Indeks do usunięcia: 3
dane = [10, 20, 30, 40, 50]
indeks_do_usunięcia = 3
dane.pop(indeks_do_usunięcia)
print(f'Zad 16: {dane}')

# 17. Zadanie: Zwróć listę tylko z liczbami parzystymi
# Dane: [1, 2, 3, 4, 5, 6]
dane = [1, 2, 3, 4, 5, 6]
parzyste = [item for item in dane if item % 2 == 0]
print(f'Zad 17: {parzyste}')

# 18. Zadanie: Połącz dwie listy w jedną
# Dane: [1, 2, 3] oraz [4, 5, 6]
daneA = [1, 2, 3]
daneB = [4, 5, 6]
daneA.extend(daneB)
print(f'Zad 18: {daneA}')

# 19. Zadanie: Zrób z listy słownik, gdzie klucze to elementy, a wartości to ich liczba wystąpień
# Dane: [1, 2, 2, 3, 3, 3, 4]
from collections import Counter
dane = [1, 2, 2, 3, 3, 3, 4]
slownik = Counter(dane)
print(f'Zad 19a: {slownik}')
# lub
slownik = {}
for element in dane:
    if element in slownik:
        slownik[element] += 1
    else:
        slownik[element] = 1
print(f'Zad 19b: {slownik}')

# 20. Zadanie: Zrób nową listę, zawierającą tylko te liczby, które są większe od średniej
# Dane: [5, 12, 7, 9, 3, 8]
dane = [5, 12, 7, 9, 3, 8]
suma = sum(dane)
ilosc = len(dane)
srednia = suma / ilosc
wieksze_od_sredniej = [item for item in dane if item > srednia]
print(f'Zad 20: {wieksze_od_sredniej}')

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
print(f'Zad 21: {zgrupowane}')
# ---------------------------------------------

zadania = [
    {
        "nazwa": "Zad 1",
        "opis": "Oblicza sumę wszystkich liczb w podanej liście.",
        "dane": [1, 2, 3, 4, 5],
        "oczekiwany_wynik": 15
    },
    {
        "nazwa": "Zad 2",
        "opis": "Znajduje największą liczbę w podanej liście.",
        "dane": [15, 3, 10, 4, 22],
        "oczekiwany_wynik": 22
    },
    {
        "nazwa": "Zad 3",
        "opis": "Usuwa wszystkie wystąpienia określonej liczby z listy.",
        "dane": [2, 5, 3, 5, 7, 5],
        "usuwana_liczba": 5,
        "oczekiwany_wynik": [2, 3, 7]
    },
    {
        "nazwa": "Zad 4",
        "opis": "Zwraca nową listę, w której wszystkie elementy są pomnożone przez 2.",
        "dane": [1, 2, 3, 4, 5],
        "oczekiwany_wynik": [2, 4, 6, 8, 10]
    },
    {
        "nazwa": "Zad 5",
        "opis": "Sprawdza, czy lista zawiera określoną liczbę.",
        "dane": [3, 7, 12, 9, 20],
        "szukana_liczba": 9,
        "oczekiwany_wynik": True
    },
    {
        "nazwa": "Zad 6",
        "opis": "Zwraca listę posortowaną rosnąco.",
        "dane": [5, 2, 9, 1, 6, 7],
        "oczekiwany_wynik": [1, 2, 5, 6, 7, 9]
    },
    {
        "nazwa": "Zad 7",
        "opis": "Zwraca listę posortowaną malejąco.",
        "dane": [1, 3, 8, 4, 7],
        "oczekiwany_wynik": [8, 7, 4, 3, 1]
    },
    {
        "nazwa": "Zad 8",
        "opis": "Zwraca tylko unikalne elementy z listy (usuń duplikaty).",
        "dane": [1, 2, 3, 2, 4, 1, 5],
        "oczekiwany_wynik": [1, 2, 3, 4, 5]
    },
    {
        "nazwa": "Zad 9",
        "opis": "Zwraca liczbę wystąpień określonego elementu w liście.",
        "dane": [10, 20, 20, 30, 20, 40],
        "szukana_liczba": 20,
        "oczekiwany_wynik": 3
    },
    {
        "nazwa": "Zad 10",
        "opis": "Zwraca wszystkie liczby większe niż 10.",
        "dane": [5, 15, 10, 25, 8, 12],
        "oczekiwany_wynik": [15, 25, 12]
    },
    {
        "nazwa": "Zad 11",
        "opis": "Zwraca elementy na parzystych indeksach.",
        "dane": [10, 20, 30, 40, 50, 60],
        "oczekiwany_wynik": [10, 30, 50]
    },
    {
        "nazwa": "Zad 12",
        "opis": "Oblicza średnią z elementów listy.",
        "dane": [3, 5, 7, 9, 2],
        "oczekiwany_wynik": 5.2
    },
    {
        "nazwa": "Zad 13",
        "opis": "Odwraca kolejność elementów w liście.",
        "dane": [1, 2, 3, 4, 5],
        "oczekiwany_wynik": [5, 4, 3, 2, 1]
    },
    {
        "nazwa": "Zad 14",
        "opis": "Zwiększa każdy element w liście o 3.",
        "dane": [1, 2, 3, 4, 5],
        "oczekiwany_wynik": [4, 5, 6, 7, 8]
    },
    {
        "nazwa": "Zad 15",
        "opis": "Wstawia element w określoną pozycję w liście.",
        "dane": [1, 2, 3, 4, 5],
        "pozycja": 2,
        "element_do_wstawienia": 99,
        "oczekiwany_wynik": [1, 99, 2, 3, 4, 5]
    },
    {
        "nazwa": "Zad 16",
        "opis": "Usuwa element na określonym indeksie.",
        "dane": [10, 20, 30, 40, 50],
        "indeks_do_usuniecia": 3,
        "oczekiwany_wynik": [10, 20, 30, 50]
    },
    {
        "nazwa": "Zad 17",
        "opis": "Zwraca listę tylko z liczbami parzystymi.",
        "dane": [1, 2, 3, 4, 5, 6],
        "oczekiwany_wynik": [2, 4, 6]
    },
    {
        "nazwa": "Zad 18",
        "opis": "Łączy dwie listy w jedną.",
        "dane1": [1, 2, 3],
        "dane2": [4, 5, 6],
        "oczekiwany_wynik": [1, 2, 3, 4, 5, 6]
    },
    {
        "nazwa": "Zad 19",
        "opis": "Zrób z listy słownik, gdzie klucze to elementy, a wartości to ich liczba wystąpień.",
        "dane": [1, 2, 2, 3, 3, 3, 4],
        "oczekiwany_wynik": {1: 1, 2: 2, 3: 3, 4: 1}
    },
    {
        "nazwa": "Zad 20",
        "opis": "Zrób nową listę, zawierającą tylko te liczby, które są większe od średniej.",
        "dane": [5, 12, 7, 9, 3, 8],
        "oczekiwany_wynik": [12, 9, 8]
    },
    {
        "nazwa": "Zad 21",
        "opis": "Utwórz słownik, gdzie klucze to pierwsze litery słów, a wartości to listy słów zaczynających się od tej litery.",
        "dane": ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"],
        "oczekiwany_wynik": {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
    }
]

def operacja_1(dane):
    return sum(dane)

def operacja_2(dane):
    return max(dane)

def operacja_3(dane, usuwana_liczba):
    return [x for x in dane if x != usuwana_liczba]

def operacja_4(dane):
    return [x * 2 for x in dane]

def operacja_5(dane, szukana_liczba):
    return szukana_liczba in dane

def operacja_6(dane):
    return sorted(dane)

def operacja_7(dane):
    return sorted(dane, reverse=True)

def operacja_8(dane):
    return list(set(dane))

def operacja_9(dane, szukana_liczba):
    return dane.count(szukana_liczba)

def operacja_10(dane):
    return [x for x in dane if x > 10]

def operacja_11(dane):
    return dane[::2]

def operacja_12(dane):
    if not dane:
        return 0
    return sum(dane) / len(dane)

def operacja_13(dane):
    return dane[::-1]

def operacja_14(dane):
    return [x + 3 for x in dane]

def operacja_15(dane, pozycja, element_do_wstawienia):
    nowa_lista = dane[:]
    nowa_lista.insert(pozycja - 1, element_do_wstawienia)
    return nowa_lista

def operacja_16(dane, indeks_do_usuniecia):
    nowa_lista = dane[:]
    if 0 <= indeks_do_usuniecia < len(nowa_lista):
        nowa_lista.pop(indeks_do_usuniecia)
    return nowa_lista

def operacja_17(dane):
    return [x for x in dane if x % 2 == 0]

def operacja_18(dane1, dane2):
    return dane1.extend(dane2)

def operacja_19(dane):
    licznik = {}
    for element in dane:
        licznik[element] = licznik.get(element, 0) + 1
    return licznik

def operacja_20(dane):
    srednia = sum(dane) / len(dane) if dane else 0
    return [x for x in dane if x > srednia]

def operacja_zgrupuj_po_pierwszej_literze(dane_slowa):
    zgrupowane = {}
    for slowo in dane_slowa:
        pierwsza_litera = slowo[0]
        if pierwsza_litera in zgrupowane:
            zgrupowane[pierwsza_litera].append(slowo)
        else:
            zgrupowane[pierwsza_litera] = [slowo]
    return zgrupowane

print(f"Zadanie 1: Suma - {operacja_1(zadania[0]['dane'])}")
print(f"Zadanie 2: Największy - {operacja_2(zadania[1]['dane'])}")
print(f"Zadanie 3: Usuń '{zadania[2]['usuwana_liczba']}' - {operacja_3(zadania[2]['dane'], zadania[2]['usuwana_liczba'])}")
print(f"Zadanie 4: Pomnożone przez 2 - {operacja_4(zadania[3]['dane'])}")
print(f"Zadanie 5: Czy '{zadania[4]['szukana_liczba']}' jest? - {operacja_5(zadania[4]['dane'], zadania[4]['szukana_liczba'])}")
print(f"Zadanie 6: Posortowane rosnąco - {operacja_6(zadania[5]['dane'])}")
print(f"Zadanie 7: Posortowane malejąco - {operacja_7(zadania[6]['dane'])}")
print(f"Zadanie 8: Unikalne elementy - {operacja_8(zadania[7]['dane'])}")
print(f"Zadanie 9: Liczba wystąpień '{zadania[8]['szukana_liczba']}' - {operacja_9(zadania[8]['dane'], zadania[8]['szukana_liczba'])}")
print(f"Zadanie 10: Większe niż 10 - {operacja_10(zadania[9]['dane'])}")
print(f"Zadanie 11: Parzyste indeksy - {operacja_11(zadania[10]['dane'])}")
print(f"Zadanie 12: Średnia - {operacja_12(zadania[11]['dane'])}")
print(f"Zadanie 13: Odwrócona lista - {operacja_13(zadania[12]['dane'])}")
print(f"Zadanie 14: Zwiększone o 3 - {operacja_14(zadania[13]['dane'])}")
print(f"Zadanie 15: Wstawiono '{zadania[14]['element_do_wstawienia']}' na poz. {zadania[14]['pozycja']} - {operacja_15(zadania[14]['dane'], zadania[14]['pozycja'], zadania[14]['element_do_wstawienia'])}")
print(f"Zadanie 16: Usunięto indeks {zadania[15]['indeks_do_usuniecia']} - {operacja_16(zadania[15]['dane'], zadania[15]['indeks_do_usuniecia'])}")
print(f"Zadanie 17: Tylko parzyste - {operacja_17(zadania[16]['dane'])}")
print(f"Zadanie 18: Połączone listy - {operacja_18(zadania[17]['dane1'], zadania[17]['dane2'])}")
print(f"Zadanie 19: Liczba wystąpień elementów - {operacja_19(zadania[18]['dane'])}")
print(f"Zadanie 20: Większe od średniej - {operacja_20(zadania[19]['dane'])}")
print(f"Zadanie Grupowanie: {operacja_zgrupuj_po_pierwszej_literze(zadania[20]['dane'])}")