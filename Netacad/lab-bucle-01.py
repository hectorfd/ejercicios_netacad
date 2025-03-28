secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = int(input("Ingrese un número: "))
while numero != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Ingrese un número: "))
print("¡Bien hecho, muggle! Eres libre ahora")

