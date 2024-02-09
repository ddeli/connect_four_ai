from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT, pretty_print_board
from bitstring import board_to_bitstring, bitstring_to_board
from agents.agent_negamax.heuristic_bitboard import Col_Shift, Row_Shift, Diagonal_Shift, Antidiagoanl_Shift
from agents.agent_negamax.heuristic_bitboard import get_player_strings, print_string_alligned,count_pattern, evaluate_string, evaluate_board
import numpy as np

def string_to_board(pp_board: str):
    """
    Takes the output of pretty_print_board and turns it back into an ndarray.
    This is quite useful for debugging, when the agent crashed and you have the last
    board state as a string.

    Parameters
    ----------
    pp_board : str
        The string representation of a game board as produced by pretty_print_board.

    Returns
    -------
    board_array: numpy.ndarray
        A NumPy array representing the game board.
    """

    board_array_of_string = pp_board.split('|')[1::2]
    board_array_of_string =np.array([[i for i in row] for row in board_array_of_string])[:,::2]

    board_array = np.zeros(board_array_of_string.shape)
    board_array[board_array_of_string==PLAYER1_PRINT] = PLAYER1
    board_array[board_array_of_string==PLAYER2_PRINT] = PLAYER2
    board_array = board_array[::-1]
    return board_array

def test_evaluate_boared():
    board_string = ''' 
     - - - - - - - 
    |             |
    |      X      |
    |             |
    |  X         X|
    |X O O O     X|
    |X O X X X   X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    threepiece_score = 2
    twopiece_score = 1
    board_score = evaluate_board(bit_board, PLAYER1, threepiece_score, twopiece_score)
    print(board_score,'board_score')
    assert board_score == ((4*threepiece_score + 4*twopiece_score) - (1*threepiece_score + 2*twopiece_score))


def test_evaluate_string():
    board_string = ''' 
     - - - - - - - 
    |             |
    |      X      |
    |             |
    |  X         X|
    |X O O O     X|
    |X O X X X   X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string = get_player_strings(bit_board, PLAYER1)
    n_two_piece_window, n_three_piece_window = evaluate_string(agent_string, empty_string)
    assert n_two_piece_window == 4
    assert n_three_piece_window == 4

def test_count_pattern_TTFT_diag():
    board_string = ''' 
     - - - - - - - 
    |  X          |
    |X            |
    |      X      |
    |             |
    |  X          |
    |X     X      |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string = get_player_strings(bit_board, PLAYER1)
    counted = count_pattern('TTFT',agent_string, empty_string, Diagonal_Shift)
    print(counted,'counted')
    assert counted == 1

def test_count_pattern_TTFF_hor():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |  O O        |
    |  X X        |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string = get_player_strings(bit_board, PLAYER1)
    counted = count_pattern('TTFF',agent_string, empty_string, Row_Shift)
    print(counted,'counted')
    assert counted == 1

def test_count_pattern_TTFF_vert():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |    X   O    |
    |    X   O    |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string = get_player_strings(bit_board, PLAYER1)
    counted = count_pattern('TTFF',agent_string, empty_string, Col_Shift)
    print(counted,'counted')
    assert counted == 1

def test_get_player_strings():
    board_string = ''' 
     - - - - - - - 
    |O           X|
    |O           O|
    |O           X|
    |X            |
    |X            |
    |X            |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string  = get_player_strings(bit_board,agent_piece= PLAYER1)
    assert bin(agent_string) == bin(0b1110000000000000000000000000000000000000000001010)
    assert bin(opponent_string) == bin(0b0001110000000000000000000000000000000000000000100)
    assert bin(occupied_string) == bin(0b1111111000000100000010000001000000100000010001111)
    assert bin(empty_string) == bin(0b111111011111101111110111111011111101110000)

def test_board_to_bitstring():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |X X X X      |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    bit_board = board_to_bitstring(board)
    print(bit_board)

def test_bitstring_to_board():
    bit_board = ['0100100010010001001000100100010010001001000100100', '1000010100001010000101000010100001010000101000010']
    board = bitstring_to_board(bit_board,2)
    string_board = pretty_print_board(board)
    print(string_board)





    
