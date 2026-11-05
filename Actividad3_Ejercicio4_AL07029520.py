
# Ejercicio 4: La caja registradora de la cafetería
print("Ejercicio 4: La caja registradora de la cafetería")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

total = 0
cantidad_productos = 0

producto = input("Nombre del producto (o escribe fin): ").lower()

while producto != "fin":
    precio = float(input("Precio del producto: $"))
    cantidad = int(input("¿Cuántas piezas quiere?: "))

    subtotal = precio * cantidad
    total += subtotal
    cantidad_productos += cantidad

    print("Subtotal: $", round(subtotal, 2))
    producto = input("Otro producto (o escribe fin): ").lower()

print("\n--- TICKET ---")
print("Cantidad de productos:", cantidad_productos)

if total >= 200:
    total -= 20
    print("Se aplicó un descuento de $20.")

print("Total a pagar: $", round(total, 2))

pago = float(input("¿Con cuánto paga?: $"))

while pago < total:
    print("El dinero no alcanza. Faltan $", round(total - pago, 2))
    pago = float(input("Ingresa un pago suficiente: $"))

cambio = pago - total
print("Cambio: $", round(cambio, 2))
print("Gracias por su compra.")
