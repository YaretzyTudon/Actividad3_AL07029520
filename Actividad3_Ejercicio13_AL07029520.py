
# Ejercicio 13: Mis juegos favoritos
print("Ejercicio 13: Mis juegos favoritos")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

juegos = [
    "Minecraft",
    "Roblox",
    "Fortnite",
    "Block Blast",
    "The Sims"
]

print("Primer juego:", juegos[0])
print("Último juego:", juegos[-1])
print("Tercer juego:", juegos[2])

print("Cantidad de juegos:", len(juegos))

print("\n--- LISTA NUMERADA ---")

for numero, juego in enumerate(juegos, start=1):
    print(numero, ".", juego)

lugar = int(input("Elige un número del 1 al 5: "))

if lugar >= 1 and lugar <= 5:
    print("El juego que elegiste es:", juegos[lugar - 1])
else:
    print("Número no válido.")
