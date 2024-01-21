from game_utils_sahand import PLAYER1, PLAYER2, string_to_board, pretty_print_board
from bitstring import board_to_bitstring, bitstring_to_board
from agents.agent_negamax.heuristic_bitboard import Col_Shift, Row_Shift, Diagonal_Shift, Antidiagoanl_Shift
from agents.agent_negamax.heuristic_bitboard import get_player_strings, print_string_alligned,count_pattern, evaluate_string, evaluate_boared

def test_evaluate_boared():
    board_string = ''' 
     - - - - - - - 
    |O           O|
    |O         O  |
    |O           X|
    |             |
    |            X|
    |  O O O     X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    evaluate_boared(bit_board, PLAYER1)


def test_evaluate_string():
    board_string = ''' 
     - - - - - - - 
    |  X          |
    |  X          |
    |  O     X    |
    |  X X   X    |
    |             |
    |        X    |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string = get_player_strings(bit_board, PLAYER1)
    evaluate_string(agent_string, empty_string)

def test_count_pattern():
    board_string = ''' 
     - - - - - - - 
    |  X          |
    |  X          |
    |        X    |
    |  X     X    |
    |             |
    |        X    |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    agent_string, opponent_string, occupied_string, empty_string = get_player_strings(bit_board, PLAYER1)
    count_pattern('TFTT',agent_string, empty_string, Col_Shift)

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

    evaluater_string, second_string, occupied_string, empty_string  = get_player_strings(bit_board,evaluater_piece = PLAYER1)

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





    
