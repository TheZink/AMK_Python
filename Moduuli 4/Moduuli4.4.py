import random

arpo = random.randint(1,10)

while True:
    luku = int(input("Syötä luku: "))

    if luku != arpo:
        if luku < arpo:
            print(f"Liian pieni arvaus.")
            #Jos luku on pienempi, kuin ohjelman arpoma, niin siirrytään tähän
        elif luku > arpo: 
            print(f"Liian suuri arvaus.")
            #Jos luku on suurempi, kuin ohjelman arpoma, niin siirrytään tähän
    else:
        print("Oikein!")
        break            