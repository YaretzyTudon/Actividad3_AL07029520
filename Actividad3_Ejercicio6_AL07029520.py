# Ejercicio 6: Validar los datos de una alta
print("Ejercicio 6: Validar los datos de una alta")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

nombre_producto = input("Nombre del producto: ").strip()

while nombre_producto == "":
    print("El nombre no puede estar vacío.")
    nombre_producto = input("Escribe el nombre del producto: ").strip()

precio = float(input("Precio del producto: $"))

while precio <= 0:
    print("El precio debe ser mayor que cero.")
    precio = float(input("Escribe un precio válido: $"))

piezas = int(input("Piezas en bodega: "))

while piezas < 0:
    print("Las piezas no pueden ser negativas.")
    piezas = int(input("Escribe una cantidad válida: "))

print("\nCategorías: 1. Tenis  2. Ropa  3. Accesorios")
categoria = input("Elige la categoría: ")

while categoria not in ("1", "2", "3"):
    print("Categoría no válida.")
    categoria = input("Elige 1, 2 o 3: ")

if categoria == "1":
    nombre_categoria = "Tenis"
elif categoria == "2":
    nombre_categoria = "Ropa"
else:
    nombre_categoria = "Accesorios"

print("\n--- FICHA DEL PRODUCTO ---")
print("Nombre:", nombre_producto)
print("Precio: $", round(precio, 2))
print("Piezas:", piezas)
print("Categoría:", nombre_categoria)

guardar = input("¿Guardar? (s/n): ").lower()

while guardar not in ("s", "n"):
    print("Respuesta no válida.")
    guardar = input("Escribe s o n: ").lower()

if guardar == "s":
    print("Producto guardado")
else:
    print("Alta cancelada")