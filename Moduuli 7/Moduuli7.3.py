airport = {}

def aloitus(airport):    
    while True:
        syote = input("Mitä haluat tehdä? Kirjoita haluamasi toiminto. Tyhjä merkkijono lopettaa ohjelman. ('lisaa' tai 'hae'): ")
        if syote == "lisaa":
            lisaa(airport)
        elif syote == "hae":
            hae(airport)
        elif syote == "":
            break

def lisaa(airport):
    ICAO = input("Anna lentokentän ICAO-tunnus: ")
    air_name = input("Anna lentokentän nimen: ")
    airport[ICAO] = air_name
    print("Tieto lisätty onnistuneesti!")
    return(airport)

def hae(airport):
    ICAO = input("Anna lentokentän ICAO-tunnus: ")
    if ICAO in airport:
        print(airport[ICAO])
        return
    else:
        print(f"{ICAO} ei löytynyt tietokannasta")
      


aloitus(airport)