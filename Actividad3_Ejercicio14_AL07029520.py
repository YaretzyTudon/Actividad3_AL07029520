# Ejercicio 14: Altas en el inventario
print("Ejercicio 14: Altas en el inventario")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

inventario = []

producto = input("Escribe un producto (o fin para terminar): ").strip()

while producto.lower() != "fin":

    if producto == "":
        print("El producto no puede estar vacío.")

    elif producto in inventario:
        print("Ese producto ya existe.")

    else:
        inventario.append(producto)
        print("Producto agregado.")
        print("Llevas", len(inventario), "productos.")

    producto = input("Escribe otro producto (o fin para terminar): ").strip()

print("\n--- INVENTARIO FINAL ---")

if len(inventario) == 0:
    print("No agregaste productos")

else:
    for numero, producto in enumerate(inventario, start=1):
        print(numero, ".", producto)
