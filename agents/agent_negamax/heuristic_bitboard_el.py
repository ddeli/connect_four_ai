import numpy as np
from itertools import combinations

Orentation_Shift = np.int8
Col_Shift = Orentation_Shift(1)
Row_Shift = Orentation_Shift(7)
Diagonal_Shift = Orentation_Shift(8)
Antidiagoanl_Shift = Orentation_Shift(6)
Window_Score = np.int8
# TwoPiece_Score = Window_Score(1)
# ThreePiece_Score = Window_Score(20)


def evaluate_board_simple_heuristic(
    board, agent_piece, threepiece_score: np.int8 = 2, twopiece_score: np.int8 = 1
):
    # check the output of the original function and here we can use denises code for finding 4 conceced pieces
    # if conncet_4_our_player: return 1000
    # else: return -1000
    return 1


def evaluate_board(
    board, agent_piece, threepiece_score: np.int8 = 2, twopiece_score: np.int8 = 1
):
    agent_string, opponent_string, _, empty_string = get_player_strings(
        board, agent_piece
    )

    # print('*** evaluating agent board ***')
    agent_two_piece, agent_three_piece = evaluate_string(agent_string, empty_string)
    # print('*** evaluating opponnent board ***')
    opponent_two_piece, opponent_three_piece = evaluate_string(
        opponent_string, empty_string
    )

    board_score = (agent_two_piece - opponent_two_piece) * twopiece_score + (
        agent_three_piece - opponent_three_piece
    ) * threepiece_score
    # print(board_score, 'board score')
    return board_score


def evaluate_string(evaluater_string, empty_string):
    orientation_shifts = [Col_Shift, Row_Shift, Diagonal_Shift, Antidiagoanl_Shift]
    n_two_piece_window = 0
    n_three_piece_window = 0
    for orientation_shift in orientation_shifts:
        if orientation_shift == Col_Shift:
            two_piece_patterns = ["TTFF"]
            three_piece_patterns = ["TTTF"]
        else:
            two_piece_patterns = ["FFTT", "FTFT", "FTTF", "TFTF", "TTFF", "TFFT"]
            three_piece_patterns = ["FTTT", "TFTT", "TTFT", "TTTF"]

        # print(f'*** evaluating orientation {orientation_shift} ***')
        for pattern in two_piece_patterns:
            # print(f'*** evaluating pattern {pattern} ***')
            n_two_piece_window += count_pattern(
                pattern, evaluater_string, empty_string, orientation_shift
            )
        # print(f'*** evaluating orientation {orientation_shift} ***')
        for pattern in three_piece_patterns:
            # print(f'*** evaluating pattern {pattern} ***')
            n_three_piece_window += count_pattern(
                pattern, evaluater_string, empty_string, orientation_shift
            )

    # print(n_two_piece_window,'n_two_piece_window')
    # print(n_three_piece_window,'n_three_piece_window')

    return n_two_piece_window, n_three_piece_window


def count_pattern(pattern, evaluater_string, empty_string, oreintation_shift):
    string = evaluater_string if pattern[3] == "T" else empty_string

    for i in pattern[-2::-1]:
        if i == "T":
            string = (string << oreintation_shift) & evaluater_string
        else:
            string = (string << oreintation_shift) & empty_string
    # print_string_alligned(string,'string')
    count = bin(string).count("1")
    # print(count,f'counted {pattern} and orientation {oreintation_shift}')
    return count


def get_player_strings(board, agent_piece):
    agent_string, opponent_string = (
        (int(board[0], 2), int(board[1], 2))
        if agent_piece == 1
        else (int(board[1], 2), int(board[0], 2))
    )

    occupied_string = agent_string | opponent_string
    occupied_string |= int("0000001000000100000010000001000000100000010000001", 2)

    all_one_string = (1 << 49) - 1
    empty_string = occupied_string ^ all_one_string

    # print_string_alligned(agent_string,'agent_string')
    # print_string_alligned(opponent_string,'second_string')
    # print_string_alligned(occupied_string,'occupied_string')
    # print_string_alligned(empty_string,'empty_string')
    return agent_string, opponent_string, occupied_string, empty_string


def print_string_alligned(string, text=None):
    print(format((bin(string)[2:]).zfill(70), ">70"), text)
    return
