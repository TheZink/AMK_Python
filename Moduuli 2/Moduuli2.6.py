syote1 = int(input("Anna leiviskien lukumäärä: "))
syote2 = int(input("Anna naulojen lukumäärä: "))
syote3 = float(input("Anna luodien lukumäärä: "))

luoti = 13.3
naula = luoti * 32 #Naula painaa 32 luodin verran3
leiviska = naula * 20 #Leiviskä painaa 20 naulan verran
yhteensa = ((luoti*syote3)+(naula*syote2)+(leiviska*syote1))/1000 #Lasketaan tavaroiden yhteispaino
kilo = int(yhteensa)
gramm = (yhteensa-kilo)*1000

print("Massa nykymittojen mukaan:")
print(f"{(yhteensa//1):.0f} kilogrammaa ja {(gramm):.2f}")

