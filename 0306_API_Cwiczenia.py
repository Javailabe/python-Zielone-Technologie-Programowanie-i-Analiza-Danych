import pandas as pd
import requests as request

# 1. Pobieranie nazw Pokémonów
# Pobierz pierwsze 20 Pokémonów i zapisz ich nazwy do listy oraz Pandas DataFrame.
def getFirst20Pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=20'
    response = request.get(url)
    if response.status_code == 200:
        poke_json = response.json()
        poke_list = poke_json["results"]
        return poke_list
    else:
        return None

def processData(data):
    poke_list = []
    for pokemon in data:
        newItem = {
            "Name":pokemon["name"]
        }
        poke_list.append(newItem)
    return pd.DataFrame(poke_list)

pokemons = getFirst20Pokemons()
poke_df = processData(pokemons)

# 2. Dodanie ID Pokémonów
# Dla każdego z tych Pokémonów pobierz jego id i dodaj jako nową kolumnę do DataFrame.
def setPoke_With_Ids(poke_data_frame):
    pokemons_serie = poke_data_frame['Name']
    poke_with_ids = []
    for pokemon in pokemons_serie:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = request.get(url)
        if response.status_code == 200:
            poke_json = response.json()
            poke_id = poke_json["id"]
            new_item = {
                "Id": poke_id,
                "Name": pokemon
            }
            poke_with_ids.append(new_item)
    return pd.DataFrame(poke_with_ids)

pokemons_with_ids = setPoke_With_Ids(poke_df)

# 3. Typy Pokémonów
# Pobierz typy (np. fire, water, grass) dla każdego z tych Pokémonów i dodaj jako kolumnę types
# (jeśli mają więcej niż jeden typ – zapisz jako listę/string).
def get_poke_types(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
    response = request.get(url)
    if response.status_code == 200:
        poke_json = response.json()
        types = [t['type']['name'] for t in poke_json['types']]
        return ', '.join(types)
    else:
        return None

pokemons_names = pokemons_with_ids['Name']
pokemons_with_types = {}
for pokemon in pokemons_names:
    types = get_poke_types(pokemon)
    pokemons_with_types[pokemon] = types
pokemons_with_ids['Type'] = pokemons_with_ids['Name'].map(pokemons_with_types)
pokemons_with_types = pokemons_with_ids

# 4. Filtracja po typie
# Wyświetl tylko te Pokémony, które mają typ "water".

water_pokemons = pokemons_with_types[pokemons_with_types['Type'].str.contains('Water', case=False, na=False)]
# print(water_pokemons)

# 5. Statystyki ataku i obrony
# Dla tych Pokémonów pobierz attack i defense i dodaj je jako kolumny do DataFrame.
def get_pokemon_stats(pokemon):
    stats_data = {
        'Attack': None,
        'Defense': None
    }
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'
    response = request.get(url)
    if response.status_code == 200:
        poke_json = response.json()
        for stat_entry in poke_json['stats']:
            stat_name = stat_entry['stat']['name']
            base_stat = stat_entry['base_stat']
            if stat_name == 'attack':
                stats_data['Attack'] = base_stat
            elif stat_name == 'defense':
                stats_data['Defense'] = base_stat
    return stats_data

pokemon_attack_map = {}
pokemon_defense_map = {}
for pokemon in pokemons_names:
    stats = get_pokemon_stats(pokemon)
    if stats:
        pokemon_attack_map[pokemon] = stats['Attack']
        pokemon_defense_map[pokemon] = stats['Defense']
pokemons_with_types['Attack'] = pokemons_with_types['Name'].map(pokemon_attack_map)
pokemons_with_types['Defense'] = pokemons_with_types['Name'].map(pokemon_defense_map)
# print(pokemons_with_types)

# 6. Średni atak i obrona
# Oblicz średnie wartości attack i defense dla wszystkich Pokémonów z listy.
mean_att = pokemons_with_types['Attack'].mean()
mean_def = pokemons_with_types['Defense'].mean()
# print(f'Mean attack: {mean_att}')
# print(f'Mean defense: {mean_def}')

# 7. Sortowanie po ataku
# Posortuj DataFrame malejąco według attack i wyświetl 5 najsilniejszych Pokémonów.
top_5_attack = pokemons_with_types.sort_values(by='Attack', ascending=False).head(5)
# print(top_5_attack)

# 8. Pobieranie nazw postaci
# Pobierz pierwsze 10 postaci ze Star Wars i zapisz ich name, height, mass do Pandas
# DataFrame.

# 9. Filtrowanie po wzroście
# Wyświetl postacie, których wzrost (height) jest większy niż 170 cm.

# 10. Dodanie planety
# Dla każdej postaci pobierz nazwę jej planety (homeworld) i dodaj jako nową kolumnę planet.