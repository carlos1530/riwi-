inventario = []

def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. salir")
   
def agregar_producto(nombre,precio,cantidad): 
      producto={
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
      }
      inventario.append(producto)
      print(f"producto {nombre} agregada con exito")

def mostrar_inventario():
     if not inventario:
        print("Inventario vacio")
        return
     print("\nInventario")
     total=0
     for i, prod in enumerate(inventario,1):
         subtotal= prod['precio'] * prod['cantidad']
         total += subtotal
         print(f"{i}. {prod['nombre']} -precio:${prod['precio']: 2f} -cantidad:{prod['cantidad']} -subtotal:${subtotal: 2f}")

     print(f"\nValor total del inventario: ${total:.2f}")

def buscar_producto(nombre): 
        resultados = list(filter(lambda p: p['nombre'].lower() == nombre.lower(), inventario))
        return resultados
def eliminar_producto(nombre):
    global inventario
    resultados = buscar_producto(nombre)
    if resultados:
        inventario = [p for p in inventario if p['nombre'].lower() != nombre.lower()]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print("Producto no encontrado.")
def actualizar_producto(nombre):
    productos = buscar_producto(nombre)
    if productos:
        prod = productos[0]
        print(f"Producto encontrado: {prod}")
        opcion = input("¿Qué desea actualizar? (precio/cantidad): ").strip().lower()
        if opcion == "precio":
            nuevo_precio = float(input("Nuevo precio: "))
            prod["precio"] = nuevo_precio
            print("Precio actualizado.")
        elif opcion == "cantidad":
            nueva_cantidad = int(input("Nueva cantidad: "))
            prod["cantidad"] = nueva_cantidad
            print("Cantidad actualizada.")
        else:
            print("Opción inválida.")
    else:
        print("Producto no encontrado.")

def main(): 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            resultados = buscar_producto(nombre)
            if resultados:
                print(f"Producto encontrado: {resultados[0]}")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "5":
            nombre = input("Nombre del producto a actualizar: ")
            actualizar_producto(nombre)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()