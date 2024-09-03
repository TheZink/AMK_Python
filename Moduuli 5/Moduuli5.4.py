#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan 
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. 
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä 
#kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta 
#niiden läpikäymiseen.

city = []
for i in range(5):
    syote = input("Syötä kaupunki: ")
    city.append(syote)

for x in city:
    print(x)