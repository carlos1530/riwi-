def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador_vocales = 0

    for caracter in cadena:
        if caracter == ' ': 
         break
        
        if caracter in vocales:
            print("Vocal")
            contador_vocales += 1
    print("Cantidad total de vocales:", contador_vocales)

  
contar_vocales(input("Introduce una cadena de texto: "))
