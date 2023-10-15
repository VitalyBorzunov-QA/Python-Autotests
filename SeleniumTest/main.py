import requests


token = "4820d3fa9b872c438462ac46114fd094"
host = "https://api.pokemonbattle.me:9104"


'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg',
                         json={"trainer_token": token,
                               "email": "ns9pi@rentforsale7.com",
                               "password": "Iloveqa1"},
                                 headers={"Content-Type" : "application/json"})
print(response.text)'''

'''
response_activation = requests.post(f'{host}/trainers/confirm_email',
                                    json={"trainer_token" : token},
                                    headers={"Content-Type" : "application/json"})
print(response_activation.status_code)

if response_activation.status_code == 200:
    print('ok!')
else:
    print('not ok!')'''




''' создание пакемена'''
response_create_pokemon = requests.post(f'{host}/pokemons',
                                   json={"name": "АвтотестерСан", 
                                         "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                                   headers={"trainer_token":token, "Content-Type" : "application/json"})
print(response_create_pokemon.text)

'''смена имени покемона'''
response_change_name = requests.put(f'{host}/pokemons',
                                    json={"pokemon_id": 12524,
                                    "name": "KANZAS",
                                    "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                                    headers={"trainer_token": token, "Content-Type" : "application/json"})
print(response_change_name.text)


'''поймать пакемона в пакетбол'''
response_catch = requests.post(f'{host}/trainers/add_pokeball',
                               json={"pokemon_id": 12524},
                               headers={"trainer_token": token, "Content-Type" : "application/json"})
print(response_catch.text)


''' убить покемона'''
response_kill_pokemon = requests.post(f'{host}/pokemons/kill',
                                      json={ "pokemon_id": "12522"},
                                      headers={"trainer_token": token, "Content-Type" : "application/json"})
print(response_kill_pokemon.text)


