lista = [1,2,4,1,6,3,8,1,9,2,1,4,5,6,7,8,9]
lista_sin_repetidos = []
for i in lista:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)
        
#* ordenar la lista son sort()
lista_sin_repetidos.sort()
print(lista_sin_repetidos)
    