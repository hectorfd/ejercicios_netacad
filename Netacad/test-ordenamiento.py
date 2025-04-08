lista = [8,10,6,2,4] #!Lista a ordenar
intercambio = True #?variable para controlar el bucle
while intercambio:
    intercambio = False #?inicializa la variable en falso
    for i in range(len(lista)-1): #?el rango de la lista menos el numero a comparar
        if lista[i] > lista[i+1]: #?compara el elemento i con el siguiente
            intercambio = True
            lista[i], lista[i+1] = lista[i+1], lista[i] #?intercambia los elementos si el i es mayor que el siguiente
            
print(lista) #!imprime la lista ordenada



# lista = [8, 10, 6, 2, 4]  # Índices: 0, 1, 2, 3, 4 -> 5 posiciones
# for i in range(len(lista) - 1)  # range(4) = 4 intercambios (i = 0 a 3)

# i = posición 0
# 8 > 10 = False → no hay intercambio
# [8, 10, 6, 2, 4]

# i = posición 1
# 10 > 6 = True → hay intercambio
# [8, 6, 10, 2, 4]

# i = posición 2
# 10 > 2 = True → hay intercambio
# [8, 6, 2, 10, 4]

# i = posición 3
# 10 > 4 = True → hay intercambio
# [8, 6, 2, 4, 10]
