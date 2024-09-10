import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="sinkki",
    password="1234",
    autocommit=True,
    collation='utf8mb4_unicode_ci'
    )

def lentokentan_tunnus():
    maatunnus = input("Syö maakoodin: ")
    etsi_tunnus(maatunnus)

def etsi_tunnus(maatunnus):
    sql = f"SELECT airport.type FROM airport WHERE airport.iso_country = '{maatunnus}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    small_airport, medium_airport, large_airport, heliport, closed = 0,0,0,0,0
    if kursori.rowcount >0 :
        for rivi in tulos:
            if rivi[0] == "small_airport": small_airport += 1
            if rivi[0] == "medium_airport": medium_airport += 1
            if rivi[0] == "large_airport": large_airport += 1
            if rivi[0] == "heliport": heliport += 1
            if rivi[0] == "closed": closed += 1
    
    print(f"Maakoodissa {maatunnus} on {small_airport} pientä lentokenttää, {medium_airport} keskikokoista lentokenttää, {large_airport} isokokoista lentokenttää sekä {heliport} helikopterikenttää. {closed} lentokenttää on suljettu")
    return

lentokentan_tunnus()