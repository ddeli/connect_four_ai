import numpy as np
from itertools import combinations

Orentation_Shift = np.int8
Col_Shift = Orentation_Shift(1)
Row_Shift = Orentation_Shift(7)
Diagonal_Shift = Orentation_Shift(8)
Antidiagoanl_Shift = Orentation_Shift(6)


def count_pattern(pattern, agent_string, empty_string, oreintation_shift):
    string = agent_string if pattern[3] == 'T' else empty_string

    for i in pattern[-2::-1]:
        if i == 'T':
            string = (string << oreintation_shift) & agent_string
        if i == 'F':
            string = (string << oreintation_shift) & empty_string
    print_string_alligned(string,'string')
    count = bin(string).count('1')
    print(count,'count')
    return count

def count_FFTT(agent_string, empty_string, oreintation_shift):
    a = (agent_string << oreintation_shift) & agent_string
    b = (a << oreintation_shift) & empty_string
    c = (b << oreintation_shift) & empty_string
    print_string_alligned(c,'c')
    return c

def count_FTFT(agent_string, empty_string, oreintation_shift):
    a = (agent_string << oreintation_shift) & empty_string
    b = (a << oreintation_shift) & agent_string
    c = (b << oreintation_shift) & empty_string
    print_string_alligned(c,'c')
    return c

def count_TFFT(agent_string, empty_string, oreintation_shift):
    a = (agent_string << oreintation_shift) & empty_string
    b = (a << oreintation_shift) & empty_string
    c = (b << oreintation_shift) & agent_string
    print_string_alligned(c,'c')
    return c

def count_TFTF(agent_string, empty_string, oreintation_shift):
    a = (empty_string << oreintation_shift) & agent_string
    b = (a << oreintation_shift) & empty_string
    c = (b << oreintation_shift) & agent_string
    print_string_alligned(c,'c')
    return c

def count_TTFF(agent_string, empty_string, oreintation_shift):
    a = (empty_string << oreintation_shift) & empty_string
    b = (a << oreintation_shift) & agent_string
    c = (b << oreintation_shift) & agent_string
    print_string_alligned(c,'c')
    return c

def count_TTTF(agent_string, empty_string, oreintation_shift):
    a = (empty_string << oreintation_shift) & agent_string
    b = (a << oreintation_shift) & agent_string
    c = (b << oreintation_shift) & agent_string
    print_string_alligned(c,'c')
    return c

def count_TTFT(agent_string, empty_string, oreintation_shift):
    a = (agent_string << oreintation_shift) & empty_string
    b = (a << oreintation_shift) & agent_string
    c = (b << oreintation_shift) & agent_string
    print_string_alligned(c,'c')
    return c

def count_TFTT(agent_string, empty_string, oreintation_shift):
    a = (agent_string << oreintation_shift) & agent_string
    b = (a << oreintation_shift) & empty_string
    c = (b << oreintation_shift) & agent_string
    print_string_alligned(c,'c')
    return c

def count_FTTT(agent_string, empty_string, oreintation_shift):
    a = (agent_string << oreintation_shift) & agent_string
    b = (a << oreintation_shift) & agent_string
    c = (b << oreintation_shift) & empty_string
    print_string_alligned(c,'c')
    return c

def evaluate_string(board, evaluater_piece, oreintation_shift):
    print('*** setting player strings ***')
    evaluater_string, second_string, occupied_string, empty_string = get_player_strings(board, evaluater_piece)

    # get a list of shifted strings of the evaluater
    print('*** shifting evaluater strings ***')
    evaluater_shifted = left_bit_shifts(evaluater_string, shift_step=oreintation_shift, shifts=2)

    # get ORed string of the evaluter shifter once and twice
    evaluter_shifted1_Ored = OR_strings(evaluater_shifted[:2])
    evaluter_shifted2_Ored = OR_strings(evaluater_shifted[:3])

    # get a list of shifted strings of the second string
    print('*** shifting seconder strings ***')
    seconder_shifted = left_bit_shifts(second_string, shift_step=oreintation_shift, shifts=2)
    seconder_shifted.append(second_string >> oreintation_shift)
    for shift,string in enumerate(seconder_shifted):
        print_string_alligned(string,f'seconder shift element{shift}')
    
    # check for connected four in the occupied string
    print('*** checking connected four in occupied_string ***')
    occupied_connected_four_str = get_x_connected_str(occupied_string, 4, oreintation_shift)

    # getting TFTT and TTFT strings
    TFTT_TTFT_str = get_pattern_str(evaluter_shifted1_Ored,occupied_connected_four_str,x_connect=5,shift_step=oreintation_shift)
    return

def get_pattern_str(Ored_string, empty_checker_string,x_connect,shift_step):
    empty_checked_stirng = get_a_butnot_b(Ored_string, empty_checker_string)
    print_string_alligned(empty_checked_stirng,'empty_checked_stirng')
    pattern_string = get_x_connected_str(empty_checked_stirng,x_connect,shift_step)
    print_string_alligned(pattern_string,'pattern_string')
    return pattern_string

def get_a_butnot_b(a,b):
    a_butnot_b = (a ^ b) & a
    return a_butnot_b

def get_player_strings(board, agent_piece):
    agent_string, opponent_string = (int(board[0],2), int(board[1],2)) if agent_piece == 1 else (int(board[1],2), int(board[0],2))

    occupied_string = agent_string | opponent_string
    occupied_string |= int('0000001000000100000010000001000000100000010000001',2)

    all_one_string = (1 << 49) -1
    empty_string = occupied_string ^ all_one_string

    print_string_alligned(agent_string,'agent_string')
    print_string_alligned(opponent_string,'second_string')
    print_string_alligned(occupied_string,'occupied_string')
    print_string_alligned(empty_string,'empty_string')
    return agent_string, opponent_string, occupied_string, empty_string

def left_bit_shifts(string, shift_step, shifts):
    '''
    returns a list of 'shifts' shifted strings each one shifted 'shift_step'
    '''
    shifted_strings = []
    for shift in range(shifts+1):
        shifted_string = string << int(shift_step*shift)
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
    print(format((bin(string)[2:]).zfill(70),'>70'),text)
    return