luku = int(input("Syötä vuosiluku: "))

if luku % 4 == 0 and (luku % 100 != 0 or luku % 400 == 0):
    print("Vuosi on karkausvuosi.")

else:
    print("Vuosi ei ole karkausvuosi.")