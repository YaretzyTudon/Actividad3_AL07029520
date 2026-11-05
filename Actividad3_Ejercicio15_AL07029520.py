
# Ejercicio 15: Bajas en el inventario
print("Ejercicio 15: Bajas en el inventario")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

inventario = [
    "Nike Air Force 1",
    "Adidas Samba",
    "Nike Dunk",
    "New Balance 550",
    "Puma Suede"
]

while True:
    print("\n--- INVENTARIO ---")

    for numero, producto in enumerate(inventario, start=1):
        print(numero, ".", producto)

    numero_borrar = int(input("Número del producto a eliminar (0 para terminar): "))

    if numero_borrar == 0:
        break

    if numero_borrar < 1 or numero_borrar > len(inventario):
        print("Ese número no existe")

    else:
        producto = inventario[numero_borrar - 1]

        confirmar = input(
            "¿Seguro que quieres eliminar " + producto + "? (s/n): "
        ).lower()

        if confirmar == "s":
            del inventario[numero_borrar - 1]
            print("Producto eliminado.")
        else:
            print("Eliminación cancelada.")

    if len(inventario) == 0:
        print("El inventario quedó vacío.")
        break

print("\nProductos que quedaron:", len(inventario))
