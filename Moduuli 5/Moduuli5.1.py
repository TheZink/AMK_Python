import random

input = int(input("Anna lukumäärä: "))
amount = 0

for i in range(input):
    amount += random.randint(1,6)

print(f"Arpakuutioiden silmälukujen summa on {amount}")
