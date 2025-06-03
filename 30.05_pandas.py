import pandas as pd
import openpyxl

df = pd.read_csv('amazon.csv')

print(df)

df.to_excel('amazon.xlsx')
#
# cena_wysoka = df['Price'] > 20
#
# df.drop()
# print(cena_wysoka)