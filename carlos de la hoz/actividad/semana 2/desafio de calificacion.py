#Paso 1 Determinar la aprobacion segun la calificacion ingresada 
#Paso 2 calcular el promedio seguna las calificaciones ingresadas(separadas por coma)
#Paso 3 contar calificaciones mayores 
#paso 4 verificacione y conteo 
#Paso 5 Imprimimos 
#-------------------------------------------------------
#Solicitar la primera calificacion y evaluar su estado 
try:
   notas = float(input("Ingresa una calificacion numerica (0-100)"))
   if 0 <= notas <=100:
      if notas >=60: 
         print("Aprobaste")
      else:
       print("Lo siento, no aprobaste")

   # Solicitar calificaciones separadas por coma 
   notas_input = input ("Ingresa las calificaciones separadas por coma: ")

   #Convertir las calificaciones ingresadas en float 
   lista_notas = [float(notas) for notas in notas_input.split (',')]

   # solicitar las calificaciones especificas que desea buscar 
   calificacion_especifica = float(input("Ingresa la calificacion especifica que desea buscar: "))

   #contador de cuantas veces aparece la calificacion
   contador_especifico = 0 

   #funcion para calcular promedio 
   def calcular_promedio(notas):
   
      #calcular el promedio de las notas 
      promedio = sum(notas) / len(notas) if len(notas) > 0 else 0
      return promedio

   #Calcular el promedio de las calificaciones 
   promedio = calcular_promedio(lista_notas)
   print(f"El promedio de las calificaciones es: {promedio}")

   #Solicitar un valor especifico para contar cuantas calificaciones son mayores 
   valor = float(input("Introduce el valor especifico: "))

   # contador de calificaciones mayores que el ingresado
   contador_mayores = 0 
   i = 0 #usamos un indice para recorrer la lisat con el cilo while 

   #Usamos ciclo while para conatr cuantas calificaciones son mayores 
   while i < len (lista_notas):
      calificacion = lista_notas[i]
      if calificacion > valor: 
         contador_mayores +=1
      i  +=1 #incrementamos el indice para pasar a la siguiente calificacion 
      break
      #Imprimimos el numero de calificaciones mayores
   print(f"el numero de notas mayores que {valor} es: {contador_mayores}")

   #contar cuantas veces aparece la califacion 
   for calificacion in lista_notas: 
      if calificacion == calificacion_especifica:
         contador_especifico +=1
   #imprimimos el contador de las calificaciones 
   print(f"nota {calificacion_especifica} aparece {contador_especifico} veces. ")
   print(lista_notas)
except ValueError: 
   print("Ingresa un valor numerico ")