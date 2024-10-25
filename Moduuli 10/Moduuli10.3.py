import random

class Hissi:

    def __init__(self, alin,ylin,sijainti):
        self.sijainti = sijainti
        self.ylin = ylin
        self.alin = alin
        self.arvo = False
    
    def kerros_ylös(self, siirry):
        for kerta in range(self.ylin):
            if self.sijainti != siirry: self.sijainti += 1
            self.arvo = True

    def kerros_alas(self, siirry):
        for kerta in range(self.ylin): 
            if self.sijainti != siirry: self.sijainti -= 1
            self.arvo = True

    def siirry_kerrokseen(self,siirto):
        if siirto >= self.alin and siirto <= self.ylin: #Verrataan, onko haluttu kerros olemassa
            if siirto != self.sijainti: #Verrataan hissin sijaintia ja haluttu kerros
                if self.sijainti < siirto: 
                    self.kerros_ylös(siirto) #Siirrytään tähän, jos halutaan ylös                   
                else: 
                    self.kerros_alas(siirto) #Siirrytään tähän, jos halutaan alas
                print(f"\nOlet nyt {self.sijainti} kerroksessa\n")            
            else: 
                print("\nOlet jo kyseisessä kerroksessa.\n")
                self.arvo = False       
        else: 
            print(f"\nNyt painoit väärää näppäintä. Talossa on {self.alin}-{self.ylin} kerrosta.\n")
            self.arvo = False

class Talo:
    
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.hissit = {}

    def luo_talo(self):
        #Luodaan taloyhtiölle hissit
        for x in range(1,random.randint(3,6)):
            hissi_nro = x
            self.hissit[hissi_nro] = 1
    
    def aja_hissia(self,hissi,kerros):
        koneisto = Hissi(self.alin,self.ylin,self.hissit[hissi])
        koneisto.siirry_kerrokseen(kerros)
        if koneisto.arvo is True: #Jos hissi on liikkunut, muutetaan kyseisen hissin arvo
            self.hissit[hissi] = kerros
    
    def palohalytys(self):
        for hissi in self.hissit.keys(): #Muutetaan hissien arvot
            self.hissit[hissi] = 1

def liikuta():

    kaytto = Talo(1,random.randint(3,10))
    kaytto.luo_talo()
    kayttaja = 1
    todennakoisyys = 0.10
    print(f"Tervetuloa Python AsOy taloyhtiöön! Taloyhtiössä on käytössä {len(kaytto.hissit)} hissiä ja talossa on {kaytto.ylin} kerrosta. \n")

    while True: #Silmukassa valitaan hissiä, jota halutaan käyttää
        hissi = int(input("Valitse, minkä hissiä haluat käyttää? Voit poistua rakennuksesta numerolla 0: "))
                
        if hissi == 0:
            break

        if hissi in kaytto.hissit: #Tarkastetaan, onko valittu hissi olemassa

            if kayttaja != kaytto.hissit[hissi]: #Jos valitulla hissillä on eri arvo kuin kayttaja-muuttujassa, niin muutetaan kyseisen hissin arvo samaksi.
                print(f"\nHissi on {kaytto.hissit[hissi]} kerroksessa ja sinä olet {kayttaja} kerroksessa. Kutsutaan hissi sinun luoksesi.\n")
                kaytto.hissit[hissi] = kayttaja

            while True: #Silmukassa liikutaan hissillä  
                siirto = int(input("Mihin kerrokseen haluat mennä? Voit poistua hissistä numerolla 0: "))
                if siirto != 0:
                    kaytto.aja_hissia(hissi, siirto)
                    kayttaja = kaytto.hissit[hissi]
                else:
                    break

            if random.random() < todennakoisyys: #Funktio arpoo mahdollisuuden palohälytykselle.
                kaytto.palohalytys()
                print("Taloyhtiössä on palohälytys. Käyttäkää lähintä poistumisreittiä. Hissin käyttö palohälytyksen aikana on kielletty. Hissit lähetetään katutasolle ja käyttö lukitaan.")
                todennakoisyys = 1
                break
            
        else:
            print("\nValittua hissiä ei ole olemassa. Yritä uudelleen.\n")
        
        if todennakoisyys == 1:
            break
    

liikuta()