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
    auto_tiedot = {}
    ajot = {}
    sijoitus = 1

    # Luodaan autot ja tallennetaan nämä listaan
    for tunnus in range(1,11):
        rekisteri = f"ABC-{tunnus}"
        huippu = random.randint(100,200)
        auto_tiedot[rekisteri] = huippu
        ajot[rekisteri] = 0
        
    while True:

        # Puretaan autojen tiedot ja aloitetaan kilpailu
        for auto, nopeus in auto_tiedot.items():
            nosto = random.randint(-10,15)
            muutos = Auto(auto, nopeus)
            muutos.kiihdyta(nosto)
            muutos.kulje(1)

            ajot[auto] += muutos.kuljettu
        
        # Tarkistetaan, onko sanakirjassa voittaja
        if 1000 in ajot.values():
            break
    
    osallistujat = dict(sorted(ajot.items(),key=lambda item: item[1],reverse=True))
    print()
    print("="*66)
    print()
    for voittaja, matka in osallistujat.items():
        print(f'\n{sijoitus}. {voittaja} auton huippunopeus on {auto_tiedot[voittaja]} ja oli ajanut {matka} kilometriä\n')
        print("-"*66)
        sijoitus += 1
    print(f"\nKilpailun voittaja on {max(osallistujat.keys(),key=lambda item: item[1])}. Onnittelut voittajalle!\n")
    print("="*66)
    


        

            



kilpailu()
        






