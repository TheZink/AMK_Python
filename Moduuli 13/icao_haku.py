import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="rahtipeli",
    user="root",
    password="KaOl2024",
    autocommit=True,
    collation='utf8mb4_unicode_ci'
    )

def etsi_lentoasema(ICAO):
    sql = f"SELECT airport.ident, airport.name, airport.municipality FROM airport WHERE airport.ident = '{ICAO}';"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0 :
        for rivi in tulos:
            return(rivi[0],rivi[1],rivi[2])