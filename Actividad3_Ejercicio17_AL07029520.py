
# Ejercicio 17: Consultas en el inventario
print("Ejercicio 17: Consultas en el inventario")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: Al07029520")

inventario = [
    "Nike Air Force 1",
    "Adidas Samba",
    "Nike Dunk",
    "New Balance 550",
    "Puma Suede",
    "Converse Chuck Taylor"
]

while True:
    print("\n--- MENÚ DE CONSULTAS ---")
    print("1. Buscar por nombre")
    print("2. Buscar por primera letra")
    print("3. ¿Cuántos productos hay?")
    print("4. Regresar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        modelo = input("Escribe el modelo que buscas: ").strip()

        if modelo.lower() in [p.lower() for p in inventario]:
            for numero, producto in enumerate(inventario, start=1):
                if producto.lower() == modelo.lower():
                    print("El modelo está en el lugar", numero)
        else:
            print("Ese modelo no está en el inventario.")

    elif opcion == "2":
        letra = input("Escribe una letra: ").lower()
        encontrados = 0

        for producto in inventario:
            if producto.lower().startswith(letra):
                print(producto)
                encontrados += 1

        print("Modelos encontrados:", encontrados)

    elif opcion == "3":
        print("Cantidad de productos:", len(inventario))

    elif opcion == "4":
        print("Regresando...")
        break

    else:
        print("Opción no válida.")
