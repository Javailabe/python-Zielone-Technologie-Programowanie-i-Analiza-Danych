import datetime as dt

# zad 1
# 1.Za pomocą match wypisz odpowiednią
# informację o języku programowania
# jeśli język to: Python,PHP,Java to wyświetlaj informację “Backend”
# jeśli język to JavaScript, HTML to wyświetlaj informację “Frontend”

language = input("Wpisz język programowania: ").lower()
match language:
    case "python" | "php" | "java":
        print("Backend")
    case "javascript" | "html":
        print("Frontend")
    case _:
        print("Nie znam tego języka")

# zad 2
# Za pomocą pythona spróbuj uzyskać informacje o aktualnym miesiącu, za pomocą
# match - przetłumacz nazwy miesiący lub ich cyfrę na polskie nazwy

current_month = dt.datetime.now().month
match current_month:
    case 1:
        print("Styczeń")
    case 2:
        print("Luty")
    case 3:
        print("Marzec")
    case 4:
        print("Kwiecień")
    case 5:
        print("Maj")
    case 6:
        print("Czerwiec")
    case 7:
        print("Lipiec")
    case 8:
        print("Sierpień")
    case 9:
        print("Wrzesień")
    case 10:
        print("Październik")
    case 11:
        print("Listopad")
    case 12:
        print("Grudzień")

# try different approach but in english
print(dt.date(1900, current_month, 1).strftime('%B'))

# zad 3
# Napisz słownik (dictionary) z kluczami, imię,nazwisko, wiek
# w try except spróbuj wyprintować klucz który nie istnieje np. miasto
# napisz except, który obsłuży błąd klucza (nie istniejący klucz)
searched_key = input("Podaj szukany klucz: ")
person = {
    "imie" : "Jan",
    "nazwisko" : "Kowalski",
    "wiek" : 31
}
try:
    print(person[searched_key])
except KeyError:
    print("Klucz nie istenieje")
finally:
    print("Dziękuje za skorzystanie z aplikacji")