import random

class Auto:
    
    

    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nyky_nopeus = 0
        self.kuljettu = 0

    def kiihdyta(self,nosto):
        if nosto > 0:
            if nosto < self.huippu:
                self.nyky_nopeus = nosto
    
    def kulje(self,tunti):
        self.kuljettu += self.nyky_nopeus * tunti


def kilpailu():
    kilpa_autot = {}
    aika = 0
    kaynnissa = True

    for tunnus in range(1,11):
        rekisteri = f"ABC-{tunnus}"
        huippu = random.randint(100,200)
        kilpa_autot[rekisteri] = {'nopeus':huippu,'ajettu':0}
        
    while kaynnissa is True:

        for rekisteri, tiedot in kilpa_autot.items():
            nosto = random.randint(-10,15)
            auto = Auto(rekisteri, tiedot['nopeus'])
            auto.kiihdyta(nosto)
            auto.kulje(1)

            kilpa_autot[rekisteri]['ajettu'] += auto.kuljettu
            print(kilpa_autot)

            
            if kilpa_autot[rekisteri]['ajettu'] >= 1000:
                break
    
            



kilpailu()
        






