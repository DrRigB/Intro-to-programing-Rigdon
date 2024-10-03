import random
import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(base_url + "1/")
pokemon_data = response.json()

#print("Pokemon Name:", pokemon_data['name'])

random_pokemon_id = random.randint(1, 151)


# Fetch data for the randomly selected Pokémon
response = requests.get(base_url + str(random_pokemon_id) + "/")
pokemon_data = response.json()


# Print the Pokémon's name and other details
print("Randomly Selected Pokémon:", pokemon_data['name'])
print("Height:", pokemon_data['height'], "decimeters")
print("Weight:", pokemon_data['weight'], "hectograms")
print("Abilities:", [ability['ability']['name'] for ability in pokemon_data['abilities']])


for i in range(3):
    random_pokemon_id = random.randint(1, 151)
    response = requests.get(base_url + str(random_pokemon_id) + "/")
    pokemon_data = response.json()
   
    print(f"\nPokémon {i+1}: {pokemon_data['name']}")
    print("Height:", pokemon_data['height'], "decimeters")
    print("Weight:", pokemon_data['weight'], "hectograms")
    print("Abilities:", [ability['ability']['name'] for ability in pokemon_data['abilities']])


 