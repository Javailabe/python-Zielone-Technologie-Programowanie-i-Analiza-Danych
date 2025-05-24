kraje = ["Polska", "Niemcy", "Francja", "Czechy", "Brazylia", "USA"]
inne_kraje = ["Włochy","Hiszpania","Szwajcaria"]

najnowszy = kraje[-1]
najnowszy2 = kraje[len(kraje) - 1]

print(najnowszy2)

kraje.extend(inne_kraje)
print(kraje)

# plaska = [x for nowa in tablica for x in nowa]

# filtrowanie
imiona = ["Jan","Kasia","Anna"]
filrowane_imiona = [imie for imie in imiona if imie.endswith("a")]

print(filrowane_imiona)
#################
wszystkie_kraje = [
    ["Polska","USA"], #element 1
    ["Francja","Niemcy"],#element 2
    ["kONGO","EGIPT"] #element 3
]

for podtablica in wszystkie_kraje: # podtablica - ["Polska","USA"],
    print(podtablica)
    for kraj in podtablica: # kraj - Polska
        print(kraj)

plaska = [kraj for podtablica in wszystkie_kraje for kraj in podtablica]
print(plaska)