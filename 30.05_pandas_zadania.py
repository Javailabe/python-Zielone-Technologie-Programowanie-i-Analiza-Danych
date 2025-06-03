import pandas as pd

# 1. Wczytaj plik 'books_sample.csv' i wyświetl pierwsze 5 wierszy.
# df = pd.read_csv('books_sample.csv').head()
df = pd.read_csv('books_sample.csv')
print(df)

# 2. Wyświetl informacje o danych (liczba kolumn, typy danych, brakujące wartości)."
print(df.info())

# 3. Posortuj dane rosnąco po kolumnie 'Price'.
print(df.sort_values(by='Price', ascending=True))

# 4. Wyświetl książki, które kosztują więcej niż 20 zł i mają ocenę powyżej 4.5."
filtered = df[(df['Price'] > 20) & (df['User Rating'] > 4.5)]
print(filtered)

# 5. Oblicz średnią, medianę i odchylenie standardowe ceny książek."
mean  = df.select_dtypes(include="number").mean()
median = df.select_dtypes(include="number").median()
std = df.select_dtypes(include="number").std()
print(f'****Mean: {mean},\n****median: {median},\n****std: {std}')

# 6. Zmień nazwę kolumny 'User Rating' na 'Rating'.
df_updated = df.rename(columns={'User Rating': 'Rating'})
print(df_updated)

# 7. Utwórz kolumnę 'Discounted Price', gdzie cena jest o 20% niższa niż oryginalna."
df['Discounted Price'] = df['Price'] * 0.8
print(df)

# 8. Oblicz średnią ocenę (Rating) dla każdej kategorii (Genre).
df_grupped = df.groupby("Genre")["User Rating"].mean()
print(df_grupped)

# 9. Utwórz tabelę przestawną z Genre jako wierszami, Year jako kolumnami i Price jako wartością."
pivot = pd.pivot_table(df, values='Price', columns='Year', index='Genre')
print(pivot)

# 10. Zapisz przefiltrowane dane (np. z zadania 4) do pliku 'filtered_books.csv'
filtered.to_csv('filtered_books.csv')