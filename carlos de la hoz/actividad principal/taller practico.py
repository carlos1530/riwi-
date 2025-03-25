#definir las operaciones 
def suma(x, y):
    return x + y 
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y 
def division(x, y): 
    if y == 0: 
        return "error: no se puede dividir entre 0"
    return x / y 

# funcion principal  
def calculadora():
    print("selecciona una operacion: ")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    

    # solicitar la operacion
    operacion = input("ingresa el numero de la oṕeracion (1/2/3/4): ")

   #solicitar los numeos 
    num1 =int (input("ingresa el primer numero: ") )
    num2 =int (input("ingresa el segundo numero: "))

   #realizar la operacion segun la eleccion 
    if operacion == "1":
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif operacion == "2":
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif operacion == "3":
        print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
    elif operacion == "4":
        print(f"{num1} / {num2} = {division(num1, num2)} ") 
    else:
          print("operacion no valida")
    
# ejecutar calculadora
calculadora()
