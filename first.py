import requests


def get_all_pokemon():
    response = requests.get(URL)
    data = response.json()
    result = data.get('results')
    for x in result:
        name = x.get('name')
        url = x.get('url')
        print("Name:", name)
        print("URL:", url)


def display_all_powers_of_pokemon():
    num = int(input("Enter the number: "))
    URL = f"https://pokeapi.co/api/v2/pokemon/{num}"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        moves = data.get('moves')
        for x in moves:
            move = x.get('move').get('name')
            print("Name:", move)
    else:
        print("Pokemon not found or invalid input")


ch = int(input("Enter the choice: "))
URL = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(URL)
data = response.json()


if ch == 1:
    get_all_pokemon()
elif ch == 2:
    display_all_powers_of_pokemon()
else:
    print("Invalid choice")


