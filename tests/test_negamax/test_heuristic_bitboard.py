from game_utils_sahand import PLAYER1, PLAYER2, string_to_board, pretty_print_board
from bitstring import board_to_bitstring, bitstring_to_board
from agents.agent_negamax.heuristic_bitboard import Col_Shift, Row_Shift, Diagonal_Shift, Antidiagoanl_Shift
from agents.agent_negamax.heuristic_bitboard import left_bit_shifts, OR_strings, AND_strings,\
                                                    get_player_strings, get_x_connected_str, print_string_alligned,\
                                                    evaluate_string, get_a_butnot_b


def test_evaluate_strings():
    board_string = ''' 
     - - - - - - - 
    |             |
    |O            |
    |X            |
    |X            |
    |O            |
    |X            |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    evaluate_string(bit_board,PLAYER1)

def test_get_a_butnot_b():
    a = int('11111',2)
    b = int('00010',2)
    a_butnot_b = get_a_butnot_b(a,b)
    print()
    print(bin(a_butnot_b))

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

def test_left_bit_shifts():
    string = int('000111100',2)
    shifted_strings = left_bit_shifts(string, 1,4)


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

def test_right_bit_shifts():
    string = int('000111100',2)
    shifted_strings = right_bit_shifts(string, 1,4)
    # print()
    # for string in shifted_strings:
    #     print(bin(string))

def test_pair_strings():
    strings = [int('101',2),int('010',2),int('111',2)]
    string_pairs = pair_strings(strings)
    print()
    for string in string_pairs:
        print(string)

def test_and_pairs():
    strings = [int('101',2),int('010',2),int('111',2)]
    string_pairs = pair_strings(strings)
    anded_strings = and_pairs(string_pairs)
    print()
    for string in anded_strings:
        print(bin(string))

def test_or_string():
    strings = [int('111000000',2),int('000111000',2),int('000000111',2)]
    ored_string = or_strings(strings)
    print()
    print(bin(ored_string))

def test_and_strings():
    # strings = [int('111000000',2),int('000111000',2),int('000000111',2)]
    strings = [int('111000000',2)]
    anded_string = and_strings(strings)
    print()
    print(bin(anded_string))

def test_get_three_piece_str():
    string = int('001011000000011100000001101',2)
    ored_string = get_three_piece_str(string,'col')
    print()
    print(bin(ored_string))

def test_get_x_connected_str():
    string = int('000000111100000111100001111',2)
    x_connected_string = get_x_connected_str(string, 4, 'col')
    print()
    print(bin(x_connected_string))

def test_get_three_piece_one_empty_Str():
    board_string = ''' 
     - - - - - - - 
    |             |
    |            X|
    |            X|
    |             |
    |            X|
    |             |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    bit_board = board_to_bitstring(board)
    print(bit_board)

    agent_string, opponent_string, occupied_string = set_player_strings(bit_board,1)
    three_piece_one_empty_str = get_three_piece_one_empty_Str(agent_string,occupied_string,Col_Shift)
    print()
    print(bin(three_piece_one_empty_str))

def test_count_connected_five():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |O O O X O X X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    bit_board = board_to_bitstring(board)
    print(bit_board)

    agent_string, opponent_string, occupied_string = set_player_strings(bit_board,1)
    count_connected_five(agent_string,occupied_string,Row_Shift)






    
