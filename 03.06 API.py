import pandas as pd
import requests
import streamlit as st
import plotly.express as px

def getCountryData():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data

def processData(data):
    countries = []
    for country in data:
        newItem = {
            "Name": country['name']['common'],
            "Population": country.get("population",0),
            "Area": country.get("area",None),
            "Region": country.get("region",""),
            "Subregion": country.get("subregion",""),
            "Capital": ", ".join(country.get("capital",[])),
            "Languages": ", ".join(country.get("languages",{}).values())
        }
        countries.append(newItem)
    return pd.DataFrame(countries)


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title("Statystyki krajów na podstawie danych z Rest Countries API")

# Pobierz dane
with st.spinner("Ładowanie danych...."):
    rawData = getCountryData()
    df = processData(rawData)

# Podstawowe statystyki
st.subheader("Podstawowe statystyki")
col1, col2, col3 = st.columns(3)
col1.metric("Liczba krajów", df.shape[0])
col2.metric("Populacja świata", df["Population"].sum())
col3.metric("Średnia powierzchnia", f"{df['Area'].mean()} km2")

# Wykres: populacja top 10

st.subheader("Top 10 krajów - populacja")

topPopulation = df.nlargest(10,"Population")
fig1 = px.bar(topPopulation, x="Name", y="Population")
st.plotly_chart(fig1, use_container_width=True)

# Wykres: Liczba krajów w regionach
st.subheader("Liczba krajów w regionach")

regionCount = df["Region"].value_counts().reset_index()
regionCount.columns = ["Region","Count"]
fig2 = px.pie(regionCount, names="Region", values="Count")
st.plotly_chart(fig2, use_container_width=True)

# Tabela danych
st.subheader("Dane źródłowe")
st.dataframe(df)







# def getCountry():
#     url = "https://restcountries.com/v3.1/name/france"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#
#         print(f"Nazwa kraju to: {data[0]['name']['common']}")
#         print(f"Nazwa waluty: {data[0]['currencies']['EUR']['name']}")
#         print(f"Kod waluty: {list(data[0]['currencies'].keys())[0]}")
#         print(f"Oficjalna nazwa kraju: {data[0]['name']['official']}")
#         print(f"Stolica kraju: {data[0]['capital']}")
#         print(f"Link z google maps: {data[0]['maps']['googleMaps']}")
#         print(f"Godło: {data[0]['coatOfArms']['png']}")
#         print(f"Sąsiedzi: {data[0]['borders']}")
#
#     else:
#         print("Nie udało się pobrać danych")
#
#
# getCountry()