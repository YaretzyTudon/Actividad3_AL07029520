# Ejercicio 18: Mini CRUD completo
print("Ejercicio 18: Mini CRUD completo")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula:AL07029520")

productos = ["Tenis deportivos", "Sudadera"]

while True:
    print("\n===== MINI CRUD =====")
    print("1. Altas")
    print("2. Bajas")
    print("3. Cambios")
    print("4. Consultas")
    print("5. Imprimir")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ").strip()

        if producto == "":
            print("El producto no puede estar vacío.")
        elif producto in productos:
            print("Ese producto ya existe.")
        else:
            productos.append(producto)
            print("Producto agregado.")

    elif opcion == "2":
        if len(productos) == 0:
            print("La lista está vacía.")
        else:
            for numero, producto in enumerate(productos, start=1):
                print(numero, ".", producto)

            numero = int(input("Número del producto a borrar: "))

            if numero < 1 or numero > len(productos):
                print("Ese número no existe.")
            else:
                confirmar = input(
                    "¿Seguro que quieres borrar " +
                    productos[numero - 1] + "? (s/n): "
                ).lower()

                if confirmar == "s":
                    del productos[numero - 1]
                    print("Producto eliminado.")
                else:
                    print("Baja cancelada.")

    elif opcion == "3":
        if len(productos) == 0:
            print("La lista está vacía.")
        else:
            for numero, producto in enumerate(productos, start=1):
                print(numero, ".", producto)

            numero = int(input("Número del producto a cambiar: "))

            if numero < 1 or numero > len(productos):
                print("Ese número no existe.")
            else:
                nuevo = input("Escribe el nuevo nombre: ").strip()

                while nuevo == "":
                    print("El nombre no puede estar vacío.")
                    nuevo = input("Escribe el nuevo nombre: ").strip()

                if nuevo in productos:
                    print("Ese producto ya existe.")
                else:
                    productos[numero - 1] = nuevo
                    print("Producto actualizado.")

    elif opcion == "4":
        consulta = input("¿Qué producto buscas?: ").strip()

        if consulta in productos:
            print("Sí está en el inventario.")
        else:
            print("No está en el inventario.")

    elif opcion == "5":
        if len(productos) == 0:
            print("La lista está vacía.")
        else:
            print("\n--- INVENTARIO ---")

            for numero, producto in enumerate(productos, start=1):
                print(numero, ".", producto)

            print("Total de productos:", len(productos))

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")
