import random

def noppa(summa):
    while True:    
        luku = random.randint(1,summa)
        if luku == summa:
            print(luku)
            return
        else:
            print(luku)
            continue

noppa(summa = int(input("Kuinka monta?: ")))