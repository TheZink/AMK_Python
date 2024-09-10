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

def lentoasema():
    ICAO = input("Anna lentoaseman ICAO-koodin: ")
    etsi_lentoasema(ICAO)

def etsi_lentoasema(ICAO):
    sql = f"SELECT airport.name, country.name FROM airport, country WHERE airport.ident = '{ICAO}' AND airport.iso_country = country.iso_country"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{ICAO} on {rivi[0]} ja sijaitsee {rivi[1]}")
    return

lentoasema()