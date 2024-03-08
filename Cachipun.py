from random import choice
# Import random 
# random choice

condicion = True
print("Bienvenidos al juego del   CA CHI PUN  hombre versus máquina \n ")

while condicion:
    
    jugador = input("Ingrese su elección [piedra, papel, tijera, salir]: ").lower()
    if jugador == "tijera" or jugador == "papel" or jugador == "piedra":
        computadora = choice (["papel", "piedra", "tijera"])
        
        print(f"La computadora jugó: {computadora}")
        if jugador == computadora:
            print(" HAS EMPATADO \n")
        elif jugador == "tijera" and computadora == "papel":
            print(" HAS GANADO \n")
        elif jugador == "papel" and computadora == "piedra":
            print(" HAS GANADO \n")
        elif jugador == "piedra" and computadora == "tijera":
            print(" HAS GANADO \n")
        else:
            print("La computadora Gana \n")
    elif jugador == "salir" :
        print("JUEGO TERMINADO..... \n")
        condicion = False       
    else:
        print("La opción ingresada no es valida ...... ")
        print("Ejecución Terminada \n")



