# Ejercicio 10: Tu playlist en el camión
print("Ejercicio 10: Tu playlist en el camión")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

playlist = [
    "Sofía",
    "Me Acostumbré a lo Bueno II",
    "Está Dañada",
    "Aquí Te Espero",
    "La Curiosidad",
    "Perro Abandonado"
]

print("\n--- MI PLAYLIST ---")

for numero, cancion in enumerate(playlist, start=1):
    print(numero, ".", cancion)

saltar = int(input("¿Qué número de canción quieres saltar? "))
parada = int(input("¿En qué número de canción llegas a tu parada? "))

escuchadas = 0

for numero, cancion in enumerate(playlist, start=1):

    if numero == parada:
        print("Llegaste a tu parada.")
        break

    if numero == saltar:
        print("Saltaste:", cancion)
        continue

    print("Escuchando:", cancion)
    escuchadas += 1

else:
    print("Escuchaste toda la playlist")

print("Canciones escuchadas:", escuchadas)