# Ejercicio 9: Torneo de videojuegos
print("Ejercicio 9: Torneo de videojuegos")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

juego = input("Nombre del juego del torneo: ")
cantidad = int(input("¿Cuántos jugadores participan?: "))

total_puntos = 0
finalistas = 0
mejor_puntos = -1
ganador = "Sin participantes"

for jugador in range(1, cantidad + 1):
    gamertag = input("Gamertag del jugador " + str(jugador) + ": ")
    puntos = int(input("Puntos obtenidos: "))

    total_puntos += puntos

    if puntos >= 100:
        print("Pasa a la final")
        finalistas += 1
    else:
        print("Sigue practicando")

    if puntos > mejor_puntos:
        mejor_puntos = puntos
        ganador = gamertag

print("\n--- RESULTADOS DEL TORNEO ---")
print("Juego:", juego)
print("Total de puntos:", total_puntos)
print("Número de finalistas:", finalistas)

if cantidad > 0:
    print("Ganador:", ganador, "con", mejor_puntos, "puntos")
else:
    print("No hubo jugadores.")