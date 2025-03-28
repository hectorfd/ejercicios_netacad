año = int(input('Introduce un año\n'))
if año < 1582:
    print('No dentro del período del calendario gregoriano')
elif año % 4 != 0:
    print('Año común')
elif año % 100 != 0:
    print('Año bisiesto')
elif año % 400 != 0:
    print('Año común')
else:
    print('Año bisiesto')