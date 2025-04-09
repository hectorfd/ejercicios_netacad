my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

my_list2 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list2[0]

for i in range(1, len(my_list2)):
    if my_list2[i] > largest:
        largest = my_list2[i]

print(largest)

my_list3 = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest2 = my_list3[0]

for i in my_list3:
    if i > largest2:
        largest2 = i

print(largest2)


lista = [1,2,4,5,7,9,12,17,12,19,20]
numero = [12]

encontrado = False
for i in lista:
    if i == numero[0]:
        encontrado = True
        break

if encontrado:
    print("El numero se encuentra en la lista")
else:
    print("El numero no se encuentra en la lista")
    
    
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

