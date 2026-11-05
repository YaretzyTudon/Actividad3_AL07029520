# Ejercicio 11: Buscador de la tienda de sneakers
print("Ejercicio 11: Buscador de la tienda de sneakers")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

inventario = [
    "Nike Air Force 1",
    "Adidas Samba",
    "Nike Dunk",
    "New Balance 550",
    "Puma Suede"
]

busquedas = 0
encontrados = 0

while True:
    modelo = input("\n¿Qué modelo buscas? (escribe salir para terminar): ").strip()

    if modelo.lower() == "salir":
        break

    busquedas += 1

    for producto in inventario:
        if modelo.lower() == producto.lower():
            print("¡Sí está disponible!", producto)
            encontrados += 1
            break
    else:
        print("No encontramos ese modelo.")
        print("Modelos disponibles:")

        for producto in inventario:
            print("-", producto)

print("\n--- RESUMEN ---")
print("Búsquedas realizadas:", busquedas)
print("Modelos encontrados:", encontrados)