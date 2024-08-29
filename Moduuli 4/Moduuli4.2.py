luku = 0

while True:
    luku = int(input("Syötä tuuma. Negatiivinen luku lopettaa ohjelman: "))
    if luku > 0:
        print(f"{luku} tuumaa on {luku * 2.54}cm")
    elif luku == 0:
        print("Syötit 0, joten senttimetreinä se on myöskin 0")
    else:
        break
