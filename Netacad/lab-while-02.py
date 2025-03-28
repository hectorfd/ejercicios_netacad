c0 = int(input('ingrese un numero entero positivo: '))
c = 0
while c0 > 0:
    if c0 != 1:
        c +=1
        if c0 % 2 == 0:
            c0 /= 2
            print(round(c0))
        else:
            c0 = 3 * c0 + 1
            print(round(c0))
            
    if c0 == 1:
        break
print('pasos:', c)