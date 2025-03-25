# pedir al usuario un numero
numero = int(input("introduce un numero entero: "))

# comprobar si el numero es par o inpar 
if numero % 2 == 0:
    tipo = "par"
else: 
    tipo = "inpar"

# comprobar si el numero es mayor que 10
if numero > 10: 
    mayor_que_10 = "y es mayor que 10"
else: 
    mayor_que_10 = "y no es mayor que10"

# Mostar el resultado 
print(f"El numero {numero} es {tipo} {mayor_que_10}")