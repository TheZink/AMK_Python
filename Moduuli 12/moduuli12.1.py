import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    tila = requests.get(pyyntö)
    
    if tila.status_code == 200:

        vastaus = tila.json()
        print(vastaus["value"])

    else:
        print(f"Haku ei onnistunut. Status {tila.status_code}")

except requests.exceptions.RequestException as error:
    print("Ei voitu suorittaa pyyntöä")
    print()
    print(error)
