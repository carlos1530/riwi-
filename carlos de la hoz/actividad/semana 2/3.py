def procesar_lista(numeros):
    count_mayores_50 = 0
    i = 0
    
    while i < len(numeros):
        numero = numeros[i]
        
        if numero < 0:
            print("Número negativo encontrado, deteniendo el ciclo.")
            break
        if numero > 100:
            i += 1
            continue
        if numero > 50:
            count_mayores_50 += 1
        
        i += 1
    
    print(f"Cantidad de números mayores que 50: {count_mayores_50}")

numeros = [10, 60, 150, -5, 80, 200, 30]
procesar_lista(numeros)

