syote = input("Syötä luku: ")
pienin = int(syote)
suurin = 0

while True:
    syote = input("Syötä luku: ")
    if syote == "":
        print(f"Suurin luku on {suurin} ja pienin luku on {pienin}")
        break
    muunto = int(syote)
    if muunto < pienin:
        pienin = muunto
    elif muunto > suurin:
        suurin = muunto


    
