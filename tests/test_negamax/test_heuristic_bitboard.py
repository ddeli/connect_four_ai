from game_utils_sahand import PLAYER1, PLAYER2, string_to_board, pretty_print_board
from bitstring import board_to_bitstring, bitstring_to_board
from agents.agent_negamax.heuristic_bitboard import right_bit_shifts, pair_strings, and_pairs, or_strings, and_strings, check_three_piece, set_player_strings, get_x_connected_str

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
    string = int('1111111111',2)
    shifted_strings = right_bit_shifts(string, 1,10)
    print()
    for string in shifted_strings:
        print(bin(string))

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

def test_check_three_piece():
    string = int('001011000000011100000001101',2)
    ored_string = check_three_piece(string,'col')
    print()
    print(bin(ored_string))

def test_set_player_strings():
    board = ['111000','000111']
    agent_string, opponent_string, occupied_stirng  = set_player_strings(board,2)
    print()
    print(bin(agent_string))
    print(bin(opponent_string))
    print(bin(occupied_stirng))

def test_get_x_connected_str():
    string = int('000000111100000111100001111',2)
    x_connected_string = get_x_connected_str(string, 4, 'col')
    print()
    print(bin(x_connected_string))


    
