
# Ejercicio 2: Menú de la Cafetería Cute
print("Ejercicio 2: Menú de la Cafetería Cute")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: TU_MATRICULA")

while True:
    print("\n--- CAFETERÍA CUTE ---")
    print("1. Ver bebidas")
    print("2. Ver postres")
    print("3. Ver horario")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Bebidas: café, chocolate y frappé.")
    elif opcion == "2":
        print("Postres: pastel, galletas y brownies.")
    elif opcion == "3":
        print("Horario: lunes a sábado, de 8:00 a 20:00.")
    elif opcion == "4":
        print("Gracias por visitar Cafetería Cute.")
        break
    else:
        print("Opción no válida")
