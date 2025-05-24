# dla porownania z lista, listy uzywaja indeksow
user = ["Jan","Kowalski",40,"Krakow"]

# slowniki uzywaja kluczy
# uzytkownik = {
#     "imie":"Jan",
#     "nazwisko":"Kowalski",
#     "wiek":40,
#     "miasto":"Kraków"
# }
# print(uzytkownik)

uzytkownik = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 40,
    "adres": {
        "miasto":"Kraków",
        "kod":"44-444",
        "ulica":"Warszawska"
    }
}

a1 = uzytkownik["adres"]["miasto"]
a2 = uzytkownik.get("adres").get("ulica")
print(a2)

# kopiowanie obiektu
a1 = {
    "nazwa":"Monitor LG",
    "producent":"LG"
}
b2 = {
    "cena":2000,
    "wyprzedaz": False
}
produkt = {
    **a1,
    **b2,
    "koniec":"koncowa wartosc"
}

produkty = [
    {
        "id": 1,
        "nazwa": "Pomidory",
        "cena": 12,
        "ilosc":1200
    },
    {
        "id": 2,
        "nazwa": "Jabłka",
        "cena": 10,
        "ilosc": 870
    }
]

from functools import reduce
nazwy = [x["nazwa"] for x in produkty]
ilosci = [x["ilosc"] for x in produkty]
wartosc = [x["cena"] * x["ilosc"] for x in produkty]

# lacznie = reduce(lambda a, b: a + b, ilosci)
print(wartosc)
# lub
lacznie = sum(ilosci)
laczna_wartosc = sum(wartosc)
print(lacznie, laczna_wartosc)