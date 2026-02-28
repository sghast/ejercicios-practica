jugadas_ganadoras = {
    "piedra" : "tijera",
    "papel" : "piedra",
    "tijera" : "papel"
}

ganador = False

while not ganador:
    jugador1 = input("[Jugador 1] Escriba su opción (piedra, papel o tijera): ").lower()
    jugador2 = input("[Jugador 2] Escriba su opción (piedra, papel o tijera): ").lower()

    if jugador1 not in jugadas_ganadoras or jugador2 not in jugadas_ganadoras:
        print("Alguna entrada es inválida, vuelve a intentarlo")
        continue
    
    if jugador1 == jugador2:
        print("Empate!")
        ganador = False
    elif jugadas_ganadoras[jugador1] == jugador2:
        print("Jugador 1 gana!")
        ganador = True
    else:
        print("Jugador 2 gana!")
        ganador = True