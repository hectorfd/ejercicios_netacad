palabra = input('Introduce una palabra: ')
for i in range(0, len(palabra)):
    if palabra[i] in 'aeiou':
        continue
    print(palabra[i].upper())
    i += 1
    