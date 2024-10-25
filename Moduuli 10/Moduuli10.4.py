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

class Kilpailu():

    def __init__(self, nimi, pituus, lista):
        self.nimi = nimi
        self.pituus = pituus
        self.lista = lista
        self.ajot = {}

    def tunti_kuluu(self):
        # Puretaan autojen tiedot
        for rekisteri in self.lista.keys():
            self.ajot[rekisteri] = 0

        #Aloitetaan kilpailu
        while True:
            for auto, nopeus in self.lista.items():
                nosto = random.randint(-10,15)
                muutos = Auto(auto, nopeus)
                muutos.kiihdyta(nosto)
                muutos.kulje(1)
                self.ajot[auto] += muutos.kuljettu
            self.tulosta_tilanne()
            tarkistus = self.kilpailu_ohi()
            
            if tarkistus == False:
                break

    def tulosta_tilanne(self):
        #Tulostetaan tämän hetkisen ajot
        osallistujat = dict(sorted(self.ajot.items(),key=lambda item: item[1],reverse=True))
        sijoitus = 1
        print()
        print("="*66)
        print(f"\n{self.nimi} tilanne tällä hetkellä:\n")
        print()
        for kilpailija, matka in osallistujat.items():
            print(f'\n{sijoitus}. {kilpailija} on ajannut {matka}')
            print("-"*66)
            sijoitus += 1
            print("="*66)


    def kilpailu_ohi(self):
        #Tarkastetaan, onko voittajia
        if self.pituus in self.ajot.values():
            return False

def main():
    auto_tiedot = {}
    sijoitus = 1

    # Luodaan autot ja tallennetaan nämä listaan
    for tunnus in range(1,11):
        rekisteri = f"ABC-{tunnus}"
        huippu = random.randint(100,200)
        auto_tiedot[rekisteri] = huippu
    
    aloitus = Kilpailu("Suuri romuralli",8000,auto_tiedot)
    aloitus.tunti_kuluu()

    #Tulostetaan tilastot ja voittaja     
    osallistujat = dict(sorted(aloitus.ajot.items(),key=lambda item: item[1],reverse=True))

    print()
    print("="*66)
    print(f"\n{aloitus.nimi} on päättynyt. Alla lista:\n")
    print()
    for voittaja, matka in osallistujat.items():
        print(f'\n{sijoitus}. {voittaja} auton huippunopeus on {auto_tiedot[voittaja]} ja oli ajanut {matka} kilometriä\n')
        print("-"*66)
        sijoitus += 1
    print(f"\nKilpailun voittaja on {max(osallistujat.keys(),key=lambda item: item[1])}. Onnittelut voittajalle!\n")
    print("="*66)
    


        

            



main()
        






