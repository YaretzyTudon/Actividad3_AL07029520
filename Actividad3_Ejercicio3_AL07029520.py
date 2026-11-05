
# Ejercicio 3: Desbloquea tu celular
print("Ejercicio 3: Desbloquea tu celular")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520 ")

pin_correcto = "1234"
intentos = 0
desbloqueado = False

while intentos < 3:
    pin = input("Escribe tu PIN: ")

    if pin == pin_correcto:
        print("Celular desbloqueado")
        desbloqueado = True
        break
    else:
        intentos += 1
        print("PIN incorrecto. Te quedan", 3 - intentos, "intentos.")

if not desbloqueado:
    print("Celular bloqueado. Pista: tu PIN tiene 4 números.")
else:
    cambiar = input("¿Quieres cambiar tu PIN? (s/n): ").lower()

    if cambiar == "s":
        nuevo_pin = input("Escribe tu nuevo PIN: ")
        confirmar_pin = input("Confirma tu nuevo PIN: ")

        while nuevo_pin != confirmar_pin:
            print("Los PIN no coinciden. Inténtalo otra vez.")
            nuevo_pin = input("Escribe tu nuevo PIN: ")
            confirmar_pin = input("Confirma tu nuevo PIN: ")

        pin_correcto = nuevo_pin
        print("Tu PIN se cambió correctamente.")
    else:
        print("Conservaste tu PIN actual.")

