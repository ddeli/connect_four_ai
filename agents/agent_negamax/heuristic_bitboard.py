import numpy as np
from itertools import combinations

Shift_Step = np.int8
Col_Shift = Shift_Step(1)
Row_Shift = Shift_Step(7)
Diagonal_Shift = Shift_Step(8)
Antidiagoanl_Shift = Shift_Step(6)


def right_bit_shifts(string, shift_step, shifts):
    shifted_strings = []
    for shift in range(shifts+1):
        shifted_string = string >> shift_step*shift
        shifted_strings.append(shifted_string)
    print()
    for shift,string in enumerate(shifted_strings):
        print_string_alligned(string,f'shifted {shift_step*shift} to the right')
    return shifted_strings

def OR_strings(strings):
    ORed_string = int('0',2)
    for string in strings:
        ORed_string |= string
    print_string_alligned(ORed_string,'ored string')
    return ORed_string

def AND_strings(strings):
    ANDed_string = strings[0]
    for string in strings:
        ANDed_string &= string
    print_string_alligned(ANDed_string,'anded string')
    return ANDed_string

def set_player_strings(board, agent_piece):
    agent_string, opponent_string = (int(board[0],2), int(board[1],2)) if agent_piece == 1 else (int(board[1],2), int(board[0],2))
    occupied_stirng = agent_string | opponent_string
    return agent_string, opponent_string, occupied_stirng

def get_x_connected_str(string, x, shift_step):
    # if shift_step != Row_Shift: string |= int('0000001000000100000010000001000000100000010000001',2)
    shifted_strings = right_bit_shifts(string,shift_step,x-1)
    x_connected_string = AND_strings(shifted_strings)
    return x_connected_string

def print_string_alligned(string,text=None):
    print(format(bin(string)[2:],'>49'),text)
    return













def and_pairs(string_pairs):
    anded_strings = []
    for pair in string_pairs:
        anded_string = pair[0] & pair[1]
        anded_strings.append(anded_string)
    for string in anded_strings:
        print_string_alligned(string, 'anded pair')
    return anded_strings

def pair_strings(strings):
    string_pairs = combinations(strings,2)
    string_pairs = [pair for pair in string_pairs]
    return string_pairs

def get_three_piece_str(string, shift_step):
    '''
    three_piece_str is bit string that has three sequence of 1s for each window that contains three pieces.
    '''
    shifted_strings = right_bit_shifts(string,shift_step,2)
    string_pairs = pair_strings(shifted_strings)
    anded_strings = and_pairs(string_pairs)
    three_piece_str = or_strings(anded_strings)
    return three_piece_str

def get_three_piece_one_empty_Str(string, occupied_string, shift_step):
    '''
    numberof 1s in the three_piece_one_empty_str determines the number of windows with three piece and one empty space.
    '''
    three_piece_str = get_three_piece_str(string,shift_step)
    four_connected_string = get_x_connected_str(occupied_string, 4, shift_step)
    three_piece_one_empty_str = three_piece_str ^ four_connected_string
    three_piece_one_empty_str = get_x_connected_str(three_piece_one_empty_str,3,shift_step)    
    return three_piece_one_empty_str

    



