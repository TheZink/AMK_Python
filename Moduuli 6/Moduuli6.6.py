def pizza():
    halkaisija_1 = int(input("Anna ensimmäisen pizzan halkaisija: "))
    summa_1 = float(input("Anna ensimmäisen pizzan hinta: "))
    halkaisija_2 = int(input("Anna toisen pizzan halkaisija: "))
    summa_2 = float(input("Anna toisen pizzan hinta: "))
    laske_pizza(halkaisija_1, summa_1, halkaisija_2, summa_2)

def laske_pizza(halkaisija_1, summa_1, halkaisija_2, summa_2):
    metri_1 = halkaisija_1 / 100
    metri_2 = halkaisija_2 / 100
    hinta_1 = summa_1 / (3.14159 * (metri_1/2)**2)
    hinta_2 = summa_2 / (3.14159 * (metri_2/2)**2)

    if hinta_1 < hinta_2:
        print(f"Ensimmäinen pizza on halvempi. Pizzan yksikköhinta oli {hinta_1:.2f} euroa/m^2")
        return
    elif hinta_1 > hinta_2:
        print(f"Toinen pizza on halvempi. Pizzan yksikköhinta oli {hinta_2:.2f} euroa/m^2")
        return
    else:
        print("Pizzat ovat samanhintaisia")


pizza()