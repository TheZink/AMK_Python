luku = 0

while luku <= 1000:
    if luku % 3 == 0:
        if luku > 0:    
            print(luku)
        luku += 1
    else:
        luku += 1
        continue