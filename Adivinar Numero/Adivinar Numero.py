import random

numero_adivinar = random.randint(1, 100)
intentos = 0

print("Adivina el número entre 1 y 100.")

while True:
    intentos += 1

    intento_usuario = int(input("Intento " + str(intentos) + ": "))

    if intento_usuario < numero_adivinar:
        print("Es mayor que", intento_usuario)
    elif intento_usuario > numero_adivinar:
        print("Es menor que", intento_usuario)
    else:
        print("Correcto. ¡Adivinaste en", intentos, "intentos!")
        break