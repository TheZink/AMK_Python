class Hissi:

    def __init__(self, alin,ylin):
        self.sijainti = 1
        self.ylin = ylin
        self.alin = alin
    
    def kerros_ylös(self, siirry):
        for kerta in range(self.ylin):
            if self.sijainti != siirry: self.sijainti += 1

    def kerros_alas(self, siirry):
        for kerta in range(self.ylin): 
            if self.sijainti != siirry: self.sijainti -= 1

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
        else: 
            print(f"\nNyt painoit väärää näppäintä. Talossa on {self.alin}-{self.ylin} kerrosta.\n")

def liikuta():
    kaytto = Hissi(1,10)
    print(f"Tervetuloa Python AsOy taloyhtiöön! Voit liikuttaa hissiä syöttämällä lukua {kaytto.alin}-{kaytto.ylin} väliltä. Numerolla 0 poistut hissistä.\n")
    while True:
        siirto = int(input("Mihin kerrokseen haluat mennä?: "))

        if siirto != 0:
            kaytto.siirry_kerrokseen(siirto)
        else:
            print(f"\nPoistuit {kaytto.sijainti}-kerroksessa.")
            if kaytto.sijainti != 1:
                print(f"Hissi palautetaan takaisin katutasolle.")
            print("Näkemiin!")
            break

liikuta()