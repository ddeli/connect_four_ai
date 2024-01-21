import numpy as np
from itertools import combinations

Shift_Step = np.int8
Col_Shift = Shift_Step(1)
Row_Shift = Shift_Step(7)
Diagonal_Shift = Shift_Step(8)
Antidiagoanl_Shift = Shift_Step(6)

def get_player_strings(board, evaluater_piece):
    '''
    gets the board representation and returns agent_string, opponent_string, occupied_string, empty_string.
    opponent_string and occupied_string include the virtual row as well since they are used to check for empty places.
    we don't want to count the virtual row as empty spaces.
    '''
    evaluater_string, second_string = (int(board[0],2), int(board[1],2)) if evaluater_piece == 1 else (int(board[1],2), int(board[0],2))
    second_string |= int('0000001000000100000010000001000000100000010000001',2)

    occupied_string = evaluater_string | second_string

    all_one_string = (1 << 49) -1
    empty_string = occupied_string ^ all_one_string

    print_string_alligned(evaluater_string,'evaluater_string')
    print_string_alligned(second_string,'second_string')
    print_string_alligned(occupied_string,'occupied_string')
    print_string_alligned(empty_string,'empty_string')
    return evaluater_string, second_string, occupied_string, empty_string

def left_bit_shifts(string, shift_step, shifts):
    '''
    returns a list of 'shifts' shifted strings each one shifted 'shift_step'
    '''
    shifted_strings = []
    for shift in range(shifts+1):
        shifted_string = string << shift_step*shift
        shifted_strings.append(shifted_string)
    print()
    for shift,string in enumerate(shifted_strings):
        print_string_alligned(string,f'shifted {shift_step*shift} to the left')
    return shifted_strings

def OR_strings(strings):
    ORed_string = int('0',2)
    for string in strings:
        ORed_string |= string
    print_string_alligned(ORed_string,'ORed_string')
    return ORed_string

def AND_strings(strings):
    ANDed_string = strings[0]
    for string in strings:
        ANDed_string &= string
    print_string_alligned(ANDed_string,'ANDed_string')
    return ANDed_string

def get_x_connected_str(string, x, shift_step):
    shifted_strings = left_bit_shifts(string,shift_step,x-1)
    x_connected_string = AND_strings(shifted_strings)
    return x_connected_string

def print_string_alligned(string,text=None):
    print(format((bin(string)[2:]).zfill(49),'>59'),text)
    return