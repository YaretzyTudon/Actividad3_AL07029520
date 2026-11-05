# Ejercicio 8: Revisa tu gamertag
print("Ejercicio 8: Revisa tu gamertag")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

gamertag = input("Escribe tu gamertag: ")

vocales = 0
numeros = 0
caracteres = 0

for letra in gamertag:
    print("Carácter:", letra)
    caracteres += 1

    if letra.lower() in "aeiouáéíóú":
        vocales += 1

    if letra.isdigit():
        numeros += 1

print("Vocales:", vocales)
print("Números:", numeros)
print("Caracteres en total:", caracteres)

if numeros == 0:
    print("Agrégale un número para que sea único")