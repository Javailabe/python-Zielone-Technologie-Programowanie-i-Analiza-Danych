print("Zadanie 1")
imie = "Paweł"
nazwisko = "Kulecki"
miasto = "Kraków"

wynik = f"To jest {imie} {nazwisko}. Jego miejsce urodzenia to {miasto}."
print(wynik)
print("")

print("Zadanie 2")
result = "to jest krótkie zdanie na temat Jana"
result_processed = result.replace(" ", "-")
print(result_processed)
print("")

print("Zadanie 3")
greeting = "hello world"

# a)
greeting_length = len(greeting)
print(f"a) {greeting_length}")

# b)
GREETING = greeting.upper()
print(f"b) {GREETING}")

# c)
Greeting = greeting.capitalize()
print(f"c) {Greeting}")
print("")

print("Zadanie 4")
movie = "lord of the rings"
movie_capitalized_letters = movie.title()
print(movie_capitalized_letters)
print("")

print("Zadanie 5")
# na indeksie 0 jest litera d, na indeksie 4 jest litera i; miejsce 5 uznaje jako index 4
today = "dzisiaj jest sobota"
today_letter = today[4]
print(today_letter)

print("nowy print")
nowa = "nowa zmienna"
nowa_do_githuba = "nowa zmienna do githuba"
print("commit na nowej galezi")