import random

nRandom = random.randint(0, 100)
intentos = 5

print("ADIVINA EL NÚMERO [0-100]")

while intentos != 0:
    print("Intentos:", intentos)
    dato = input("Ingresa un número: ")
    
    #validación de sólo números
    if not dato.isdigit():
        print("Solo se permiten NÚMEROS")
        continue

    numero = int(dato)
    
    #validación de rangos
    if numero < 0 or numero > 100:
        print("FUERA DE RANGO")
        continue

    if numero == nRandom:
        print("Acertaste!")
        break

    intentos -= 1
    if numero < nRandom:
        print("Incorrecto! Pista: Es mayor")
    else:
        print("Incorrecto! Pista: Es menor")
    
    if intentos == 0:
        print("El número era ", nRandom, ", casi lo logras")