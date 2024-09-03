import random

def noppa():
    while True:
        luku = random.randint(1,6)
        if luku == 6:
            print(luku)
            return
        else:
            print(luku)
            continue

noppa()
