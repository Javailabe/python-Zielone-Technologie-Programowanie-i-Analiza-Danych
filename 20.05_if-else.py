import datetime as dt
# zad 1
user_role = "usr"
is_logged = True

if user_role == "admin" and is_logged:
    print("Witaj w panelu admina")
elif user_role == "mod" and is_logged:
    print("Witaj w panelu moderatora")
elif user_role == "usr" and is_logged:
    print("Witaj w panelu użytkownika")
else:
    print("Błąd logowania")

# zad 2
countries = ["Polska", "Niemcy", "Czechy"]
user_country = "Francja"

if user_country in countries:
    print("Zamówienie przyjęte")
else:
    print("Dostawa towaru niemożliwa")

# zad 3
curretnt_hour = dt.datetime.now().hour
print(curretnt_hour)
if curretnt_hour >= 6 and curretnt_hour < 12:
    print("Good Morning")
elif curretnt_hour >= 12 and curretnt_hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")