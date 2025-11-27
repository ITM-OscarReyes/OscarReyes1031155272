import random

def get_computer_choice():
    return random.choice(["piedra", "papel", "tijera"])

def determine_winner(player, computer):
    if player == computer:
        return "empate"
    elif (
        (player == "piedra" and computer == "tijera") or
        (player == "papel" and computer == "piedra") or
        (player == "tijera" and computer == "papel")
    ):
        return "jugador"
    else:
        return "computadora"
