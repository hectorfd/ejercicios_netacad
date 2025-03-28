numero = int(input('Digite um número: '))
contador = 1
suma = 0
while suma <= numero:
    suma += contador
    if suma > numero:
        contador-=1
        break
    if suma == numero:
        break
    contador += 1
print('La altura de la piramide es:', contador)

