class Auto:
    
    nyky_nopeus = 0
    kuljettu = 2000


    def __init__(self, rekisteri, huippu,nopeus,tunti):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = nopeus
        self.tunti = tunti

    def kiihdyta(self, nosto):
        if nosto > 0:
            if nosto < self.huippu:
                Auto.nyky_nopeus = nosto
                print(f"Auton nopeus nostettu {Auto.nopeus} km/h")
        else:
            Auto.nyky_nopeus = 0
            print("Suoritettu hätäjarrutus")
    
    def kulje(self,tunti):
        Auto.kuljettu += self.nopeus * tunti
        print(f"Auto kulki {self.kuljettu} km")


auto = Auto("ABC-123", 120, 60, 0)

auto.kulje(1.5)





