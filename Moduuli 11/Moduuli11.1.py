class Julkaisu:

    kirja_nro = 0

    def __init__(self,nimi):
        self.nimi = nimi
        Julkaisu.kirja_nro += 1
        self.kirja_lkm = Julkaisu.kirja_nro

    def tulosta_tiedot(self):
        print(f"{self.kirja_lkm}: {self.nimi}")


class kirja(Julkaisu):
    
    def __init__(self, nimi,kirjailija,sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"{self.kirja_lkm}: {self.nimi}, kirjan kirjoitti {self.kirjailija} ja siinä on {self.sivumaara} sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi,toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        print(f"{self.kirja_lkm}: {self.nimi}. Lehden päätoimittaja on {self.toimittaja}.")


julkaisut = []
julkaisut.append(kirja("Python käsikirja","Metropolia",300))
julkaisut.append(Lehti("Pythonkylän lehti","Pekka Koodari"))
julkaisut.append(kirja("VSCoden salaisuudet","Ville Kirjoittaja",1000))
julkaisut.append(Lehti("Koodausmaailman uutiset","Kalle Untinen"))



for julkaisu in julkaisut:
    julkaisu.tulosta_tiedot()