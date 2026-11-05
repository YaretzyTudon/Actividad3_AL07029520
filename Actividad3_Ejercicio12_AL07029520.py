# Ejercicio 12: Alta de productos con folio
print("Ejercicio 12: Alta de productos con folio")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

cantidad = int(input("¿Cuántos productos darás de alta?: "))
valor_total = 0

for numero in range(1, cantidad + 1):
    folio = "SNK" + str(numero)

    print("\n--- PRODUCTO", folio, "---")

    nombre_producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: $"))

    while precio <= 0:
        print("El precio debe ser mayor que 0.")
        precio = float(input("Escribe un precio válido: $"))

    piezas = int(input("Piezas en bodega: "))

    valor_producto = precio * piezas
    valor_total += valor_producto

    print("\n--- FICHA DEL PRODUCTO ---")
    print("Folio:", folio)
    print("Nombre:", nombre_producto)
    print("Precio: $", round(precio, 2))
    print("Piezas:", piezas)
    print("Valor en bodega: $", round(valor_producto, 2))

print("\nValor total del inventario: $", round(valor_total, 2))