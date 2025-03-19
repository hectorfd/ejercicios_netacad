ingreso = float(input("Ingrese su ingreso anual: "))
IMPUESTO = 0.18
if ingreso <= 85528:
    impuesto = ingreso * IMPUESTO - 556.2
    if impuesto < 0:
        impuesto = 0.0
elif ingreso > 85528:
    impuesto = 14839.2 + (0.32 * (ingreso - 85528))
    if impuesto < 0:
        impuesto = 0.0
elif ingreso < 0:
    impuesto = 0.0
else:
    print("Error")
    
print("El impuesto es: ", round(impuesto, 0), "pesos")