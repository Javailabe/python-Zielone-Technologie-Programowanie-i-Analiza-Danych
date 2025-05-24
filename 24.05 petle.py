# import random
#
# num = 1
# iteracje = 0
#
# while num != 7:
#     if iteracje >= 5000:
#         print("Przerywam pętlę")
#         break
#     iteracje += 1
#
#     num = random.randint(0,5000)
#     print(f"Iteracja {iteracje}. Wylosowano liczbę {num}")

stan_konta = 5000

while True:
    print("--Witamy w aplikacji--")
    print("1. Podaj stan konta")
    print("2. Wpłać pieniądze")
    print("3. Wypłać pieniądze")
    print("4. Zeruj środki")
    print("5. Wyjdź")
    operacja = int(input("Wybierz operację: "))

    match operacja:
        case 1:
            print(f"Stan konta to: {stan_konta} zł")
        case 2:
            kwota = int(input("Wpisz kwotę do wpłaty: "))
            stan_konta += kwota
            print(f"Wpłacono {kwota} zł")
        case 3:
            kwota_wyplacana = int(input("Wpisz kwotę do wypłaty: "))
            if kwota_wyplacana > stan_konta:
                print("Nie masz wystarczających środków")
                continue
            stan_konta -= kwota_wyplacana
            print(f"Na koncie pozostalo {stan_konta} zł")
        case 4:
            stan_konta = 0
            print("Wyzerowano środki na koncie.")
        case 5:
            print("Dziękuje my za skorzysystanie z aplikacji")
            break