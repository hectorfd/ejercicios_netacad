list_1 = [1]
list_2 = list_1[:]#! este rebanador : permite crear una nueva lista
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

my_list2 = [10, 8, 6, 4, 2]
new_list2 = my_list2[1:-1]
print(new_list2)

my_list3 = [10, 8, 6, 4, 2]
new_list3 = my_list3[:3]
print(new_list3)

#? si dejas [:] vacio mostrara toda la lista sin rebanar nada
#? la funcion Del permite eliminar un elemento de la lista y tambien rebanadas
#? evitando que se creen nuevas listas con esa rebanada
my_list4 = [10, 8, 6, 4, 2]
del my_list4[1:3] #! elimina el elemento 8 y 6
print(my_list4) #! imprime la lista sin los elementos eliminados
#! en caso de uar Del lista[:] se eliminara el contenido de la lista
#! quedando vacia en cambio Del lista eliminara la lista como tal