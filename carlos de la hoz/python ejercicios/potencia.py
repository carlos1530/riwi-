# numero = int(input("ingresa un numero: "))
# exponente = int ( input("ingresa un exponente: ")) 


# resultado = numero ** exponente 
# print (f"{numero} elevado a {exponente} es : {resultado}")


num1=int(input("Ingresa un numero: "))
num2=int(input("Ingresa un segundo numero: "))
num3=int(input("Ingresa un tercer numero: "))

lista =[num1,num2,num3]
nueva_lista=[]

for numero in lista:
   if numero >0:
      numero = numero**3
      nueva_lista.append(numero)
      print(nueva_lista)

      