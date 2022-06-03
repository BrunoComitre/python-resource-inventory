import pytest
from code_game.mygame import game

"""
O teste é formado por 3 etapas:
(GWT):
- Give : dado um valor para testar
- When : quando o teste é executado
- Then : então o resultado esperado é obtido

(AAA):
- Arrange : dado um valor para testar
- Act : quando o teste é executado
- Assert : então o resultado esperado é obtido

xUnit Patterns - Gerard Meszaros : Livro
4 Step Testings:
- Setup - Dado : que prepara(montamos) o ambiente para o teste
- Exercise - Quando : que executa(chamamos as coisas) o teste
- Verify - Então : que verifica o resultado
- TearDown - Desmonta tudo antes que seja tarde : que limpa o ambiente
"""

@pytest.mark.smoke
def test_my_game() -> None:
    assert True

@pytest.mark.number
def test_when_game_received_one_then_should_be_return_one() -> None:
    """ Long Version
    - Game - SUT - System Under Test"""
    input_data = 1  # dado/given
    expected = 1  # dado/given
    result = game(input_data)  # quando/when
    assert result == expected  # então/then

@pytest.mark.number
def test_when_game_received_two_then_should_be_return_two() -> None:
    """ Minimal Version
    TDD - Kent Back - One-Step Test
    """
    assert game(1) == 1

@pytest.mark.number
def test_when_game_received_return_two_then_shoul_be_return_two() -> None:
    assert game(2) == 2

@pytest.mark.chesse
def test_when_game_received_three_then_shoul_be_return_cheese() -> None:
    assert game(3) == 'cheese'

@pytest.mark.guava
def test_when_game_received_five_then_shoul_be_return_guava() -> None:
    assert game(5) == 'guava'

@pytest.mark.guava
def test_when_game_received_ten_then_shoul_be_return_guava() -> None:
    assert game(10) == 'guava'

@pytest.mark.guava
def test_when_game_received_twenty_then_shoul_be_return_guava() -> None:
    assert game(20) == 'guava'

@pytest.mark.wip
def test_when_game_received_five_then_shoul_be_return_Romeo_and_Juliet() -> None:
    assert game(105) == 'Romeo and Juliet'

@pytest.mark.parameterization
@pytest.mark.parametrize('received', [5, 10, 20, 25, 35])
def test_game_should_be_return_multiple_five(received) -> None:
    assert game(received) == 'guava'

@pytest.mark.parameterization
@pytest.mark.parametrize('received', [3, 6, 9, 12])
def test_game_should_be_return_multiple_three(received) -> None:
    assert game(received) == 'cheese'

@pytest.mark.parameterization
@pytest.mark.parametrize('send, received', [(1, 1), (2, 2), (3, 'cheese'), (4, 4), (5, 'guava')])
def test_game_should_be_return_multiple_three_and_five(send, received) -> None:
    assert game(send) == received
