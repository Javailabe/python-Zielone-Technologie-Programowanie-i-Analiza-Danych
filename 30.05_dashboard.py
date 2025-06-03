import pandas as pd
import streamlit as st

data = {
    "Produkt": ["Laptop", "Tablet", "Smartfon", "Monitor", "Laptop", "Tablet", "Smartfon", "Monitor"],
    "Kraj": ["Polska", "Polska", "Niemcy", "Niemcy", "Polska", "Niemcy","Polska", "Polska"],
    "Sprzedaż": [120, 80, 200, 60, 100, 70, 180, 90],
    "Miesiąc": ["Styczeń", "Luty", "Styczeń", "Styczeń", "Luty", "Styczeń", "Luty", "Luty"]
}
df = pd.DataFrame(data)

st.title("Tabela sprzedaży")

selected_country = st.sidebar.multiselect(
    label="Wybierz kraj",
    options=df["Kraj"].unique(),
    default=df["Kraj"].unique()[0],
)

selected_month = st.sidebar.multiselect(
    label="Wybierz miesiąc",
    options=df["Miesiąc"].unique(),
    default=df["Miesiąc"].unique()[0]
)

filtered_df = df[
    (df["Kraj"].isin(selected_country)) &
    (df["Miesiąc"].isin(selected_month))
]

st.subheader("Przefiltrowane dane")
st.dataframe(filtered_df, use_container_width=True) 