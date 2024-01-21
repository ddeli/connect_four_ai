import numpy as np
from itertools import combinations

Orentation_Shift = np.int8
Col_Shift = Orentation_Shift(1)
Row_Shift = Orentation_Shift(7)
Diagonal_Shift = Orentation_Shift(8)
Antidiagoanl_Shift = Orentation_Shift(6)


def count_pattern(pattern, evaluater_string, empty_string, oreintation_shift):
    string = evaluater_string if pattern[3] == 'T' else empty_string

    for i in pattern[-2::-1]:
        if i == 'T':
            string = (string << oreintation_shift) & evaluater_string
        if i == 'F':
            string = (string << oreintation_shift) & empty_string
    print_string_alligned(string,'string')
    count = bin(string).count('1')
    print(count,'count')
    return count

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

def print_string_alligned(string,text=None):
    print(format((bin(string)[2:]).zfill(70),'>70'),text)
    return