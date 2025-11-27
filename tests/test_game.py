import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from game import determine_winner


def test_empate():
    assert determine_winner("piedra", "piedra") == "empate"
    assert determine_winner("papel", "papel") == "empate"
    assert determine_winner("tijera", "tijera") == "empate"

def test_jugador_gana():
    assert determine_winner("piedra", "tijera") == "jugador"
    assert determine_winner("papel", "piedra") == "jugador"
    assert determine_winner("tijera", "papel") == "jugador"

def test_computadora_gana():
    assert determine_winner("tijera", "piedra") == "computadora"
    assert determine_winner("piedra", "papel") == "computadora"
    assert determine_winner("papel", "tijera") == "computadora"
