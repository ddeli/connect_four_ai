from itertools import combinations

def right_bit_shifts(string, shift_step, shifts):
    shifted_strings = []
    for shift in range(shifts+1):
        shifted_string = string >> shift_step*shift
        shifted_strings.append(shifted_string)
    return shifted_strings

def pair_strings(strings):
    string_pairs = combinations(strings,2)
    string_pairs = [pair for pair in string_pairs]
    return string_pairs

def and_pairs(string_pairs):
    anded_strings = []
    for pair in string_pairs:
        anded_string = pair[0] & pair[1]
        anded_strings.append(anded_string)
    return anded_strings

def or_strings(strings):
    ored_string = int('0',2)
    for string in strings:
        ored_string |= string
    return ored_string

def and_strings(strings):
    anded_string = strings[0]
    for string in strings:
        anded_string &= string
    return anded_string

def check_three_piece(string, orientatoin):
    shift_step = 1 if orientatoin == 'col' else 0
    shifted_strings = right_bit_shifts(string,shift_step,2)
    string_pairs = pair_strings(shifted_strings)
    anded_strings = and_pairs(string_pairs)
    ored_string = or_strings(anded_strings)
    return ored_string

def set_player_strings(board, agent_piece):
    agent_string, opponent_string = (int(board[0],2), int(board[1],2)) if agent_piece == 1 else (int(board[1],2), int(board[0],2))
    occupied_stirng = agent_string | opponent_string
    return agent_string, opponent_string, occupied_stirng

def get_x_connected_str(string, x, orientation):
    shift_step = 1 if orientation == 'col' else 0
    shifted_strings = right_bit_shifts(string,shift_step,x-1)
    x_connected_string = and_strings(shifted_strings)
    return x_connected_string

    



