#pedir al usuario una calificacion 
calificacion = int(input("introduce tu clasificacion (un numero entre 0 y 10): "))

#verificar si la calificacion esta dentro ddel rango valido 
if 0<= calificacion <= 10: 

    # categorizar la clasificacion segun el rango 
    if calificacion >= 9:
        letra = "A"
    elif calificacion >= 7:
        letra = "B"
    elif calificacion >= 5:
        letra = "C"
    else: 
        letra = "F"

    # Mostrar el resultado 
    print(f"Tu calificacion es {calificacion} y corresponde a la letra {letra}. ")
else: 
     print("por favor, ingresa una calificacion valida entre 0 y 10. ") 