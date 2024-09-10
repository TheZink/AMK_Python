nimilista = []

while True:
    syote = input("Syötä nimi: ")
    if syote == "":
        break
    elif syote in nimilista:
        print("Aiemmin syötetty nimi")
    else:
        nimilista.append(syote)
        print("Uusi nimi")
        
for nimi in nimilista:
    print(nimi)