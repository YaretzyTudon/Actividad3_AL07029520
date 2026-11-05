# Ejercicio 16: Cambios en tu playlist
print("Ejercicio 16: Cambios en tu playlist")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

playlist = [
    "Sofía",
    "Me Acostumbré a lo Bueno II",
    "Está Dañada",
    "Aquí Te Espero",
    "La Curiosidad"
]

print("\n--- PLAYLIST INICIAL ---")

for numero, cancion in enumerate(playlist, start=1):
    print(numero, ".", cancion)

numero_cancion = int(input("¿Qué número de canción quieres cambiar?: "))

if numero_cancion < 1 or numero_cancion > len(playlist):
    print("Ese número no existe.")

else:
    indice = numero_cancion - 1

    print("Vas a cambiar:", playlist[indice])

    nueva = input("Escribe la nueva canción: ").strip()

    while nueva == "":
        print("La canción no puede estar vacía.")
        nueva = input("Escribe la nueva canción: ").strip()

    if nueva in playlist:
        print("Esa canción ya está en la playlist.")

    else:
        playlist[indice] = nueva
        print("Canción reemplazada.")

        mover = input("¿Quieres moverla al primer lugar? (s/n): ").lower()

        if mover == "s":
            playlist[0], playlist[indice] = playlist[indice], playlist[0]
            print("La canción se movió al primer lugar.")

print("\n--- PLAYLIST FINAL ---")

for numero, cancion in enumerate(playlist, start=1):
    print(numero, ".", cancion)
