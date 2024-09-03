def polttoaine():
    while True:
        gallona = int(input("Kuinka monta gallonaa: "))
        if gallona < 0:
            print("Heippa!")
            return
        litra = muunto(gallona)
        print(f"{gallona} gallona on {litra} litraa")

def muunto(gallona):
    return gallona * 3.785

polttoaine()
    

