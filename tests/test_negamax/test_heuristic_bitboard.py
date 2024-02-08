from game_utils import PLAYER1, PLAYER2, string_to_board, pretty_print_board
from bitstring import board_to_bitstring, bitstring_to_board
from agents.agent_negamax.heuristic_bitboard import Col_Shift, Row_Shift, Diagonal_Shift, Antidiagoanl_Shift, TwoPiece_Score, ThreePiece_Score
from agents.agent_negamax.heuristic_bitboard import get_player_strings, print_string_alligned,count_pattern, evaluate_string, evaluate_board

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

    # for this test to run correctly, make sure the three piece window score is set to 20 and two piece window to 1

    board_score = evaluate_board(bit_board, PLAYER1)
    print(board_score,'board_score')
    assert board_score == ((4*20 + 4*1) - (1*20 + 2*1))


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





    
