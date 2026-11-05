# Ejercicio 7: Boletos para el concierto
print("Ejercicio 7: Boletos para el concierto")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

artista = input("¿De quién es el concierto? ")
cantidad = int(input("¿Cuántos boletos quieres? "))

for boleto in range(1, cantidad + 1):
    asistente = input("Nombre del asistente para el boleto " + str(boleto) + ": ")

    print("\n--- BOLETO", boleto, "de", cantidad, "---")
    print("Concierto:", artista)
    print("Asistente:", asistente)

print("Se generaron", cantidad, "boletos.")