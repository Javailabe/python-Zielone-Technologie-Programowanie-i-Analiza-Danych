import math
import datetime

# Zadanie 1
a = 5
b = 7

result = (a + b) * 7
print(result)
print("")

# Zadanie 2
c = 5
d = 7
e = 2
max_num = max(c, d, e)
print(max_num)
print("")

# Zadanie 3
f = 5
g = 8
h = 3
avg = round(((f + g + h) / 3), 2)
print(avg)
print("")

# Zadanie 4
temp = 301.23
celsjus = round((temp - 273.15), 1)
print(celsjus)
print("")

# Zadanie 5
num = 25
sqr_from_number = math.sqrt(num)
print(sqr_from_number)

# Zadnie dodatkowe
# Napisz input w którym wpiszesz liczbę i przekonwartujesz ją na Int
# Pomnóż liczbę przez obecną godzinę (chodzi o cyfrę godziny np. 12. Spróbuj wyciągnąć godzinę z wbudowanej metody python)

some_input = input("Podaj liczbe: ")
converted_input = int(some_input)
current_time = datetime.datetime.now()
result = current_time.hour * converted_input
print(result)