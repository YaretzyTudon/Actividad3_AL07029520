
# Ejercicio 5: El menú de tu proyecto CRUD
print("Ejercicio 5: El menú de tu proyecto CRUD")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

sistema = input("Escribe el nombre de tu sistema: ")
operaciones = 0

while True:
    print("\n---", sistema, "---")
    print("1. Altas")
    print("2. Bajas")
    print("3. Cambios")
    print("4. Consultas")
    print("5. Imprimir")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Elegiste Altas.")
        operaciones += 1
    elif opcion == "2":
        print("Elegiste Bajas.")
        operaciones += 1
    elif opcion == "3":
        print("Elegiste Cambios.")
        operaciones += 1
    elif opcion == "4":
        print("Elegiste Consultas.")
        operaciones += 1
    elif opcion == "5":
        print("Elegiste Imprimir.")
        operaciones += 1
    elif opcion == "6":
        confirmar = input("¿Seguro que quieres salir? (s/n): ").lower()

        while confirmar not in ("s", "n"):
            print("Respuesta no válida.")
            confirmar = input("Escribe s o n: ").lower()

        if confirmar == "s":
            print("Operaciones realizadas:", operaciones)
            print("Saliendo del sistema...")
            break
        else:
            print("Regresando al menú.")
    else:
        print("Opción no válida")
