user = "python"
password = "rules"
time = 0


while True:
    input1 = input("Syötä käyttäjätunnus: ")
    input2 = input("Syötä salasana: ")

    if input1 == user and input2 == password:
        print("Tervetuloa!")
        break
    elif input1 != user or input2 != password:
        time += 1    
        if time == 5:
            print("Pääsy evätty")
            break
