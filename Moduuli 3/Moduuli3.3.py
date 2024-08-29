suku = input("Syötä suokopuolesi:  ")
arvo = int(input("Syötä hemoglobiiniarvon: "))

if suku == "Nainen" or suku == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo >= 117 and arvo <= 175:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

if suku == "Mies" or suku == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo >= 134 and arvo <= 195:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")
