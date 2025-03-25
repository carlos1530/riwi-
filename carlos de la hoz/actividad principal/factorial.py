#pedir un numero positivo al usuario 

n = int(input("ingresa un numero positivo: "))

#calcular el factorial usando un ciclo 
factorial = 1 
for i in range(1, n + 1): 
    factorial *= i 
# Mostrar el resultado 
print("El factorial de", n, "es:", factorial)
