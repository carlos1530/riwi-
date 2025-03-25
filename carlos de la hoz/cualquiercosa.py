print("Institución Riwi")
print("                  - Sistema de calificación de notas -             ")
print(" ")  # Separación del mensaje de bienvenida

while True:
    # Menú principal
    print("\n--- Menú ---")
    print("1. Determinar estado de aprobación")
    print("2. Calcular promedio de calificaciones")
    print("3. Contar calificaciones mayores a un valor")
    print("4. Verificar cuántas veces aparece una calificación específica")
    print("5. Salir")
    opcion = input("Selecciona una opción (1-5): ")

    # Opción 1: Determinar estado de aprobación
    if opcion == "1":
        while True:
            try:
                calificacion = float(input("Ingresa la calificación (0-100): "))
                if calificacion < 0 or calificacion > 100:
                    print("Las calificaciones no pueden ser negativas o mayores a 100. Intenta de nuevo.")
                    continue
                if calificacion >= 60:
                    print("¡Aprobado!")
                else:
                    print("Reprobado.")  
                break   
            except ValueError:
                print("Valor no válido. Por favor ingresa un número.")

    # Opción 2: Calcular promedio de calificaciones
    elif opcion == "2":
        while True:
            try:
                calificaciones = input("Ingresa las calificaciones separadas por comas: ")
                lista_calificaciones = [float(calificacion) for calificacion in calificaciones.split(',')]
                
                if any(calificacion < 0 or calificacion > 100 for calificacion in lista_calificaciones):
                    print("Las calificaciones no pueden ser negativas o mayores a 100. Intenta de nuevo.")
                    continue
                if len(lista_calificaciones) > 0:
                    promedio = sum(lista_calificaciones) / len(lista_calificaciones)
                    print(f"El promedio de las calificaciones es: {promedio:.2f}")
                    break 
                else:
                    print("No se ingresaron calificaciones válidas.")
                    continue
            except ValueError:
                print("Error al ingresar las calificaciones. Asegúrate de usar números o no dejar espacios vacíos.")
                continue

    # Opción 3: Contar calificaciones mayores a un valor
    elif opcion == "3":
        while True:
            try:
                calificaciones = input("Ingresa las calificaciones separadas por comas: ")
                lista_calificaciones = [float(calificacion) for calificacion in calificaciones.split(',')]

                if any(calificacion < 0 or calificacion > 100 for calificacion in lista_calificaciones):
                    print("Las calificaciones no pueden ser negativas o mayores a 100. Intenta de nuevo.")
                    continue
                
                valor = float(input("Ingresa el valor para comparar: "))
                if valor < 0:
                    print("Ingresa un valor positivo para la comparación.")             
                    continue 
                contador = 0
                for calificacion in lista_calificaciones:
                    if calificacion > valor:
                        contador += 1
                print(f"Hay {contador} calificaciones mayores que {valor}.")
                break 
            except ValueError:
                print("Error al ingresar las calificaciones. Asegúrate de usar números o no dejar espacios vacíos.")
                continue

    # Opción 4: Verificar cuántas veces aparece una calificación específica
    elif opcion == "4":
        while True:
            try:
                calificaciones = input("Ingresa las calificaciones separadas por comas: ")
                lista_calificaciones = [float(calificacion) for calificacion in calificaciones.split(',')]

                if any(calificacion < 0 or calificacion > 100 for calificacion in lista_calificaciones):
                    print("Las calificaciones no pueden ser negativas o superiores a 100. Intenta de nuevo.")
                    continue
                else:
                    break

            except ValueError:
                print("Error al ingresar las calificaciones. Asegúrate de usar números o no dejar espacios vacíos.")
                continue 

        while True:
            try:
                valor_especifico = float(input("Ingresa la calificación específica a buscar: "))

                if valor_especifico < 0 or valor_especifico > 100:
                    print("La calificación debe estar entre 0 y 100. Intenta de nuevo.")
                    continue
                else:
                    contador = lista_calificaciones.count(valor_especifico)
                    print(f"La calificación {valor_especifico} aparece {contador} veces.")
                    break  

            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue 

    # Opción 5: Salir
    elif opcion == "5":
        print("¡Hasta luego!")
        break

    # Opción inválida
    else:
        print("Opción no válida, por favor ingresa una opción del 1 al 5.")
