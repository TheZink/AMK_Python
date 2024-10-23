class Auto:
    
    nyky_nopeus = 0
    kuljettu = 0


    def __init__(self, rekisteri, huippu,nopeus):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = nopeus

    def kiihdyta(self, nosto):
        if nosto > 0:
            if nosto < self.huippu:
                Auto.nyky_nopeus = nosto
                print(f"Auton nopeus nostettu {Auto.nyky_nopeus} km/h")
        else:
            Auto.nyky_nopeus = 0
            print("Suoritettu hätäjarrutus")

auto = Auto("ABC-123", 120, 0)

auto.kiihdyta(30)
auto.kiihdyta(50)
auto.kiihdyta(70)
auto.kiihdyta(-200)





