kklista = {"talvi":{12:"Joulukuu",1:"Tammikuu",2:"Helmikuu"},
           "Kevät":{3:"Maaliskuu", 4:"Huhtikuu",5:"Toukokuu"},
           "Kesä":{6:"Kesäkuu",7:"Heinäkuu",8:"Elokuu"},
           "Syksy":{9:"Syyskuu",10:"Elokuu",11:"Marraskuu"}}
syote = int(input("Anna luku: "))

for vuodenajat, kuukaudet in kklista.items():
    for x in kuukaudet:
        if x == syote:
            print(kuukaudet[x])