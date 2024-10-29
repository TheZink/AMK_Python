import random

class Auto:
    
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.kuljettu = 0
        self.kulutettu = 0

    def kiihdyta(self,nosto):
        if nosto <= self.huippu:
            self.nyky_nopeus = nosto
    
    def kulje(self,kulutus,nopeus,tunti):
        self.kuljettu = nopeus * tunti
        self.kulutettu = (kulutus/100) * self.kuljettu

class Sahkoauto(Auto):

    def __init__(self, rekisteri, huippu,kulutus,nopeus,aika):
        super().__init__(rekisteri, huippu)
        self.kulutus = kulutus
        self.nopeus = nopeus
        self.aika = aika
    
    def aja(self):
        self.kulje(self.kulutus,self.nopeus,self.aika)
        print(f"Sähköauto rekisterinumerolla {self.rekisteri} ajoi {self.kuljettu} kilometriä ja kulutti {self.kulutettu:.2f} kWh")


class Bensaauto(Auto):

    def __init__(self, rekisteri, huippu,kulutus,nopeus,aika):
        super().__init__(rekisteri, huippu)
        self.kulutus = kulutus
        self.nopeus = nopeus
        self.aika = aika
    
    def aja(self):
        self.kulje(self.kulutus,self.nopeus,self.aika)
        print(f"Bensa-auto rekisterinumerolla {self.rekisteri} ajoi {self.kuljettu} kilometriä ja kulutti {self.kulutettu:.2f} litraa")


autot = []
autot.append(Sahkoauto("Sahko-1",180,52.5,150,5))
autot.append(Bensaauto("Bensa-2",165,32.3,165,1))

for auto in autot:
    auto.aja()