#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
luvut = []
tulostus = ""

while True:
    input1 = input("Anna luku. Tyhjä merkkijono lopettaa ohjelman: ")

    if input1 == "":
        break

    x = int(input1)
    luvut.append(x)
    luvut.sort(reverse=True)

for i in range(5):
    tulostus += f"{str(luvut[i])} "
print(tulostus)





