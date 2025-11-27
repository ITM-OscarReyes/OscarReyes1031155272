from game import get_computer_choice, determine_winner

def main():
    print("\n" + "*" * 45)
    print("      🎮  Piedra, Papel o Tijera  🎮")
    print("*" * 45 + "\n")

    player = input("Elige piedra, papel o tijera: ").lower()

    if player not in ["piedra", "papel", "tijera"]:
        print("Opción inválida")
        return

    computer = get_computer_choice()
    print(f"La computadora eligió: {computer}")

    result = determine_winner(player, computer)

    if result == "empate":
        print("¡Es un empate!")
    elif result == "jugador":
        print("¡Ganaste! 🎉")
    else:
        print("Perdiste 😢")

if __name__ == "__main__":
    main()
