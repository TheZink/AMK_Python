class Auto:
    
    nopeus = 0
    kuljettu = 0


    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu

auto = Auto("ABC-123", 120)

print(f"{auto.rekisteri} auton huippunopeus on {auto.huippu} km/h")
