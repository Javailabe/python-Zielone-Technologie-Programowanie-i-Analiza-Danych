# # 1. Utwórz listę imiona i napisz w niej 5 imion, za pomocą petli for wyświetl w princie imię każdej osoby z dopiskiem "Cześć, tu ...."
#
# imiona = ["Paweł", "Marek", "Kasia", "Bartek", "Ewa"]
# for imie in imiona:
#     print(f"Cześć, tu {imie}")
#
# # 2. Napisz pętle for range dla liczb od 10 do 250, za pomocą modulo i słówka continue wypisz tylko te liczby, które są podzielne przez 7
#
# for i in range(10,250):
#     if i % 7 != 0:
#         continue
#     print(i)
#
# # 3.
# # Fizz Buzz to popularna gra, która często jest używana jako zadanie
# # w trakcie procesu rekrutacyjnego do pracy jako programista.
# # Gra polega na tym, że gracze na zmianę wypowiadają liczby,
# # ale jeśli liczba jest podzielna przez 3, mówią "Fizz",
# # z kolei jeśli jest podzielna przez 5, mówią "Buzz".
# # Jeśli liczba jest podzielna zarówno przez 3, jak i 5, mówią "FizzBuzz"
# #
# # Za pomocą pętli i instrukcji warunkowych, spróbuj napisać algorytm FizzBuzz
# # w którym gracze liczą do liczby 101
#
# for i in range(1,102):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print(f"Dla {i} - FizzBuzz")
#     elif i % 3 == 0:
#         print(f"Dla {i} - Fizz")
#     elif i % 5 == 0:
#         print(f"Dla {i} - Buzz")
#     else:
#         print(i)
#
# #  4. Napisz program, który:
# # Pobiera od użytkownika zdanie (input).#
# # Pobiera od użytkownika jedną literę, której wystąpienia mają być policzone (input).#
# # Z użyciem pętli zlicza, ile razy ta litera występuje w zdaniu.#
# # Na końcu wypisuje wynik
#
# phrase = input("Napisz zdanie: ")
# char_to_check = input("Jaką literę zliczyc: ")
# char_amout = 0
# for char in phrase:
#     if char_to_check != char:
#         continue
#     char_amout += 1
# print(f"Ilosć wystąpień {char_to_check} to {char_amout}")

#  5. Napisz program, który:#
# Pobiera od użytkownika ciąg liczb całkowitych (oddzielonych spacją).
# Zamienia je na listę liczb.
# Za pomocą pętli znajduje:
# największą liczbę i jej indeks w liście,
# najmniejszą liczbę i jej indeks w liście.
# Wyświetla te wartości i ich indeksy.
# sequence = input("Podaj ciąg liczb odzielonych spacjami: ").split()
# highest_num = 0
# for num in sequence:
#     if num > highest_num:
#         highest_num = num
#
# print(highest_num)

# 1.
# Stwórz pustą listę i dodaj do niej kilka liczb za pomocą metody append()
# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(3)
# print(list)
#
# # 2.
# # Użyj odpowiedniej metody do połączenia dwóch poniższych list.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# list1.extend(list2)
# print(list1)
#
# # 3.
# # Z poniższej listy, za pomocą odpowiedniej metody usuń pierwsze wystąpienie cyfry 2
# my_list = [1, 2, 3, 4, 2]
# my_list.pop(my_list.index(2))
# print(my_list)
#
# # Następnie z tej samej listy usuń ostatni element
# my_list.pop()
# print(my_list)
#
# # 4.
# # Z poniższej listy znajdź numer indeksu liczby 40. Wynik przypisz do zmiennej
# my_list = [10, 20, 40, 30, 20]
# looking_index = my_list.index(40)
# print(looking_index)
#
# # 5.
# # Policz za pomocą odpowiedniej metody ilość wystąpień liczby 2 w poniższej liście
# my_list = [1, 2, 2, 3, 2, 4, 2]
# count = my_list.count(2)
# print(count)

# 1. Utwórz obiekt dotyczący twojego miasta: nazwa, województwo, populacja, kraj
miasto = {
    "nazwa": "Kraków",
    "wojewodzwto": "Małopolska",
    "populacja": 800653,
    "kraj": "Polska"
}
# 2. Wyciągnij z niego w osobnych zmiennych klucze i wartości
keys = miasto.keys()
values = miasto.values()

from datetime import  date

# 3. Utwórz tablicę z 3 obiektami symbolizującymi Loty i 4. W każdym locie dodaj klucze: samolot, kierunek, cena, pasażerowie
loty = [
    {
        "samolot": "Airbus",
        "cena": 123,
        "kierunek": "Warsaw",
        "pasazerowie": 100,
        "liczba_miejsc":100
    },
    {
        "samolot": "Cesna",
        "cena": 456,
        "kierunek": "London Stansted",
        "pasazerowie": 85,
        "liczba_miejsc": 120
    },
    {
        "samolot": "Airbus",
        "cena": 135,
        "kierunek": "Rome",
        "pasazerowie": 120,
        "liczba_miejsc": 150
    }
]
today = date.today()
# ta petla dodaje dodatkowe pole w slowniku
for lot in loty:
    lot["data_odlotu"] = str(today)
    lot["dostepne_miejsca"] = lot["liczba_miejsc"] > lot["pasazerowie"]

samoloty = [lot["samolot"] for lot in loty]
tanie_loty = [lot for lot in loty if lot["cena"] < 400]
lot_do_rome = [lot for lot in loty if lot["kierunek"] == "Rome"]

miejsca = [lot['liczba_miejsc'] for lot in loty]
suma_miejsc = sum(miejsca)
# print(suma_miejsc)

# 1. Oblicz ilość wszystkich pasażerów latających naszymi liniami
ile_pasazerow = [lot['pasazerowie'] for lot in loty]
suma_pasazerow = sum(ile_pasazerow)

# 2. Utwórz tablicę zawierającą tylko nazwy kierunków lotów
kierunki = [lot['kierunek'] for lot in loty]


# 3. Oblicz ile w sumie zarobiły nasze linie lotnicze (zlicz pasażerów i ceny lotów)
zarobek = [(lot["pasazerowie"] * lot["cena"]) for lot in loty]
total = sum(zarobek)
# print(total)

# 5. Wypisz te loty, w których zostały wolne miejsca
wolne_miejsca = [lot for lot in loty if lot["pasazerowie"] < lot["liczba_miejsc"]]
# print(wolne_miejsca)

# from collections import Counter
#
# samoloty = Counter([lot['samolot'] for lot in loty])
# dict_samoloty = dict(samoloty)
# print(dict_samoloty)
#
# for klucz, wartosc in samoloty.items():
#     print(f"Model {klucz}, ilość {wartosc}")
#
#  samoloty = Counter([lot["samolot"] for lot in loty])
# slownik_samolotow = dict(samoloty)
#
# for klucz, wartosc in slownik_samolotow.items():
#     print(f"Model {klucz}, ilość {wartosc} sztuk")
#
# slownik = {}
# for model in samoloty:
#     if model in slownik:
#         slownik[model] += 1
#     else:
#         slownik[model] = 1
#
# print(slownik)

