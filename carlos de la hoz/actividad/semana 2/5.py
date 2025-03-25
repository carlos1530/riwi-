contar_numeros = 0
while True: 
    numeros = int(input("Ingresa un numero entero, (0 para terminar)"))
    if numeros <0: 
        print("el numero es negativo, ingresa otro numero")

    if numeros ==0:
        break
    contar_numeros +=1 
    print(f"cantidad de numeros positivos ingresados:  {contar_numeros}")