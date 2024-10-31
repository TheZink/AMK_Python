import requests
import json

city_name = input("Mitä kaupunkia haetaan?: ")
request = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={'35b3bc3ba3391714e7060d165ae93c52'}"

try:
    status = requests.get(request)
    
    if status.status_code == 200:
        answer = status.json()
        get_city = f"https://api.openweathermap.org/data/3.0/onecall?lat={answer[0]['lat']}&lon={answer[0]['lon']}&exclude={'current'}&appid={'35b3bc3ba3391714e7060d165ae93c52'}"
        
        status_1 = requests.get(get_city)
        print(get_city)

        try:

            if status_1.status_code == 200:
                city_temp = status_1.json()
                print(city_temp)
            else:
                print(status_1)
                print("Ei voitu tulostaa lämpötila")
                
        except requests.exceptions.RequestException as error:
            print("Ei voitu suorittaa pyyntöä")
            print()
            print(error)



    else:
        print(f"Haku ei onnistunut. Status {status.status_code}")

except requests.exceptions.RequestException as error:
    print("Ei voitu suorittaa pyyntöä")
    print()
    print(error)
