datos_personas = [("Diego", "Teran", 15), ("Brayan", "sainea", 22), ("edinson", "Avellaneda", 60), ("Carlos", "De La Hoz", 30)]

for nombre, apellido, edad in datos_personas:
    if edad < 18:
        continue
    if edad > 60:
        print("Se encontró una persona mayor de 60 años.")
        break
    print(f"{nombre} {apellido}, Edad: {edad}")
