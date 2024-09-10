import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="sinkki",
    password="1234",
    autocommit=True,
    collation='utf8mb4_unicode_ci'
    )

def valitse_lentokentat():
    kentta1 = input("Syötä lähtöpaikan ICAO: ")
    kentta2 = input("Syötä määränpään ICAO: ")
    etsi_kentta(kentta1, kentta2)


def etsi_kentta(kentta1, kentta2):
    sql = f"SELECT airport.ident, airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident in ('{kentta1}', '{kentta2}')"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    sijainti_1, sijainti_2 = (),()
    if kursori.rowcount >0 :
        for rivi in tulos:
            if rivi[0] == kentta1:
                sijainti_1 = (rivi[1],rivi[2])
            if rivi[0] == kentta2:
                sijainti_2 = (rivi[1],rivi[2])
    laske_etaisyys(sijainti_1,sijainti_2)
    return

def laske_etaisyys(sijainti_1,sijainti_2):
    etaisyys = distance.great_circle(sijainti_1,sijainti_2).kilometers
    print(f"Lentokenttien välinen etäisyys on {etaisyys:.2f} kilometriä")
    return

valitse_lentokentat()