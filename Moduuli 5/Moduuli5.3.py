#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

input1 = int(input("Anna luku: "))
alkuluku = False

for i in range(input1):
    if input1 == i or input1 % 2 == 0 or input1 % 3 == 0:
        alkuluku = False
    else:
        alkukulu = True

if alkuluku is True:
    print(f"{input1} on alkuluku")
else:
    print(f"{input1} ei ole alkuluku")