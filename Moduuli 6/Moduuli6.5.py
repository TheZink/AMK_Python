def karsi_parittomat(lista_1):
    for i in lista_1:
        if i % 2 != 0:
            lista_1.remove(i)
    return lista_1

print(karsi_parittomat([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))