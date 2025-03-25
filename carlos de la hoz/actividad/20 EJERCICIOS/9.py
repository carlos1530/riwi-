
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Error: No se puede dividir entre cero"

print(f"{suma}, {resta}, {multiplicacion}, {division}")
