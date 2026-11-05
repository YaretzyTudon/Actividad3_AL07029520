
# Ejercicio 1: Inicia sesión en Roblox
print("Ejercicio 1: Inicia sesión en Roblox")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: TU_MATRICULA")

usuario_correcto = "jugador123"
contrasena_correcta = "roblox2026"
sesion_iniciada = False

while not sesion_iniciada:
    usuario = input("Escribe tu usuario: ")
    contrasena = input("Escribe tu contraseña: ")

    if usuario == usuario_correcto:
        if contrasena == contrasena_correcta:
            print("¡Bienvenido a Roblox!")
            print("Cargando tus juegos...")
            sesion_iniciada = True
        else:
            print("La contraseña es incorrecta")
    else:
        print("Ese usuario no existe")
