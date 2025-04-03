numbers = [1,2,3,4,5]
print(len(numbers))
print(numbers)

numbers.append(4)

print(len(numbers))
print(numbers)

numbers.insert(0,222)

print(numbers)

my_list = []

for i in range(5):
    my_list.append(i + 1)
print(my_list)

lista3 = []

for i in range(3):
    lista3.insert(0, i + 1)
print(lista3)

total = 0

for i in range(len(lista3)):
    total += lista3[i]
print(total)

total2 = 0
for i in my_list:
    total2 += i
print(total2)

desorden = [4,2,1,3]

desorden[0], desorden[2] = desorden[2], desorden[3]

desorden.insert(3,4)
del desorden[-1]

print(desorden)