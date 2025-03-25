print("Bienvenidos a smartcak ")

# Marcamos el nombre del producto 
nombre_producto = input("Nombre del producto: ")

#Sacamos el precio Unitario, cantidad y descuento 
while True:
    try:
        precio_unitario = float(input("Precio unitario: "))
        if precio_unitario <= 0:
            print("El precio debe ser positivo.")
        else:
            break
    except ValueError:
        print("Precio inválido.")

while True:
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        else:
            break
    except ValueError:
        print("Cantidad inválida.")

while True:
    try:
        descuento = float(input("Descuento (%): "))
        if 0 <= descuento <= 100:
            break
        else:
            print("El descuento debe estar entre 0 y 100.")
    except ValueError:
        print("Descuento inválido.")

#REALIZAMOS LA OPERACION 
costo_sin_descuento = precio_unitario * cantidad

costo_total = costo_sin_descuento * descuento / 100

#Imprimo el resultado 
print(f"Producto: {nombre_producto}")
print(f"Costo sin descuento: ${costo_sin_descuento: }")
print(f"Costo final: ${costo_total: }")

print("Gracias por su compra ")


