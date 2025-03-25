# El programa que vas a desarrollar en este entrenamiento debe:

#     Determinar el estado de aprobación:
#         Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#         Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
#     Calcular el promedio:
#         Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#         Calcular y mostrar el promedio de las calificaciones en la lista
#     Contar calificaciones mayores:
#         Preguntar al usuario por un valor específico
#         Contar cuántas calificaciones en la lista son mayores que este valor
#     Verificar y contar calificaciones específicas:
#         Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#         Calcular y mostrar el promedio de las calificaciones en la lista

# Paso 1 	Análisis del problema y listado de tareas: Lee en detalle y comprende todos los requisitos que debes cumplir para resolverlo correctamente. Crea una lista de las tareas que tu programa debe realizar. Esto te ayudará a mantenerte enfocado y organizado durante el desarrollo.
# Paso 2 	Diseño del programa: Planifica cómo vas a implementar cada función y tarea utilizando estructuras condicionales y bucles. Diseña el flujo lógico de tu programa.
# Paso 3 	Implementación de la Solución:

#     Entrada de datos:
#         Solicita al usuario ingresar una calificación numérica y valida la entrada
#         Permite al usuario ingresar una lista de calificaciones y un valor específico para comparar
#     Condicionales:
#         Utiliza if, if-else e if-elif-else para determinar el estado de aprobación y mostrar mensajes adecuados
#     Cálculo del promedio:
#         Implementa un ciclo for para recorrer la lista de calificaciones y calcular el promedio
#     Conteo de calificaciones mayores:
#         Usa un ciclo while para contar cuántas calificaciones son mayores que el valor especificado
#     Verificación y conteo:
#         Emplea un ciclo for para verificar la presencia de una calificación específica y contar cuántas veces aparece, utilizando break y continue para controlar el flujo

 



while True:
    try: 
        Calificacion_1=float(input("------Ingrese una calificacion del periodo 1 -------- :  "))
        if  Calificacion_1<0 or Calificacion_1>100:
            print("---------Por favor ingrese un numero entre estos rangos (0-100)---------" )
            raise ValueError
    
        if Calificacion_1<= 60 and Calificacion_1>0 :
            print("Esta nota esta reprobada")
        if Calificacion_1<=100 and Calificacion_1>60:
            print("Usted aprobo esta nota")
        break
    except ValueError :
        print("Por favor ingrese un numero valido")
        
   
    
while True:
    try: 
        Calificacion_2=float(input("------Ingrese una calificacion del periodo 2------- :  "))
        if  Calificacion_2<0 or Calificacion_2>100:
            print("---------Por favor ingrese un numero entre estos rangos (0-100)---------" )
            raise ValueError
    
        if Calificacion_2<= 60 and Calificacion_2>0 :
            print("Esta nota esta reprobada")
        if Calificacion_2<=100 and Calificacion_2>60:
            print("Usted aprobo esta nota")
        break
    except ValueError :
        print("Por favor ingrese un numero valido")
        
        
        
while True:
    try: 
        Calificacion_3=float(input("------Ingrese una calificacion del periodo 3------ :  "))
        if  Calificacion_3<0 or Calificacion_3>100:
            print("---------Por favor ingrese un numero entre estos rangos (0-100)---------" )
            raise ValueError
    
        if Calificacion_3<= 60 and Calificacion_3>0 :
            print("Esta nota esta reprobada")
        if Calificacion_3<=100 and Calificacion_3>60:
            print("Usted aprobo esta nota")
        break
    except ValueError :
        print("Por favor ingrese un numero valido")
        
        
   
    
Lista_calificacione= [Calificacion_1,Calificacion_2,Calificacion_3]

print(f"Sus 3 calificaciones son las siguientes:{Lista_calificacione}")
       
suma=0
for i in Lista_calificacione:
    suma += i

promedio= suma/len(Lista_calificacione)

print(f"El promedio de sus calificaciones es: {promedio}")
    
 
Numero_mayor= float(input(  "indique que numero quiere verificar en la lista:  "))     

while True:




    





 




  