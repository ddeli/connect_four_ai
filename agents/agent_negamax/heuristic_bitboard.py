import numpy as np
from itertools import combinations
from game_utils import BoardPiece

Orentation_Shift = np.int8
Col_Shift = Orentation_Shift(1)
Row_Shift = Orentation_Shift(7)
Diagonal_Shift = Orentation_Shift(8)
Antidiagoanl_Shift = Orentation_Shift(6)
Window_Score = np.int8
TwoPiece_Score = Window_Score(1)
ThreePiece_Score = Window_Score(20)

def evaluate_board(board: tuple[str,str], agent_piece:BoardPiece, threepiece_score: Window_Score = 2, twopiece_score: Window_Score = 1) ->int:
    """
    Evaluates the given game board for giventhe agent's piece 
    by counting occurrences of two-piece and three-piece windows for each player.

    Parameters:
    - board (Tuple[str, str]): A tuple of two strings representing the binary board states for each player.
    - agent_piece (BoardPiece): An integer (1 or 2) representing the agent's piece on the board.
    - threepiece_score (Window_Score): an integer representing the value of window of length four with three same piece and one empty space
    - twopiece_score (Window_Score): an integer representing the value of a window of length four with two same piece and two empty space

    Returns:
    int: The score of the board based on the occurrences of two-piece and three-piece windows for each player.
    """
    if threepiece_score==0 and twopiece_score==0: return 0
    
    agent_string, opponent_string, _, empty_string = get_player_strings(board, agent_piece)
    agent_string, opponent_string, _, empty_string = get_player_strings(board, agent_piece)

    # print('*** evaluating agent board ***')
    agent_two_piece, agent_three_piece = evaluate_string(agent_string, empty_string)
    # print('*** evaluating opponnent board ***')
    opponent_two_piece, opponent_three_piece = evaluate_string(opponent_string,empty_string)

    board_score = (agent_two_piece - opponent_two_piece) * twopiece_score \
                + (agent_three_piece - opponent_three_piece) * threepiece_score
    # print(board_score, 'board score')
    return board_score

def evaluate_string(evaluater_string:int, empty_string:int)->tuple[int,int]:
    """
    Evaluates the given evaluator string against predefined patterns to count occurrences 
    of two-piece and three-piece windows.

    Parameters:
    - evaluater_string (int): Binary representation of the evaluator string.
    - empty_string (int): Binary representation of the empty string.

    Returns:
    Tuple[int, int]: A tuple containing two integers:
        - n_two_piece_window: The count of two-piece windows in the evaluated string.
        - n_three_piece_window: The count of three-piece windows in the evaluated string.
    """
    orientation_shifts = [Col_Shift,Row_Shift,Diagonal_Shift,Antidiagoanl_Shift]
    n_two_piece_window = 0
    n_three_piece_window = 0
    for orientation_shift in orientation_shifts:
        if orientation_shift == Col_Shift:
            two_piece_patterns = ['TTFF']
            three_piece_patterns = ['TTTF']
        else:
            two_piece_patterns = ['FFTT','FTFT','FTTF','TFTF','TTFF','TFFT']
            three_piece_patterns = ['FTTT','TFTT','TTFT','TTTF']

        # print(f'*** evaluating orientation {orientation_shift} ***')  
        for pattern in two_piece_patterns:
            # print(f'*** evaluating pattern {pattern} ***')
            n_two_piece_window += count_pattern(pattern, evaluater_string,empty_string,orientation_shift) 
        # print(f'*** evaluating orientation {orientation_shift} ***')  
        for pattern in three_piece_patterns:
            # print(f'*** evaluating pattern {pattern} ***')
            n_three_piece_window += count_pattern(pattern, evaluater_string,empty_string,orientation_shift)
    
    # print(n_two_piece_window,'n_two_piece_window')
    # print(n_three_piece_window,'n_three_piece_window')
    
    return n_two_piece_window, n_three_piece_window

def count_pattern(pattern:str, evaluater_string:int, empty_string:int, oreintation_shift:Orentation_Shift)->int:
    """
    Counts the number of occurrences of a specified pattern in a given string and in a specific orientation.

    Parameters:
    - pattern (str): A string representing the pattern to be counted.
                    for example the pattern TTFT for piece X will be 'XX X'.
                    'T' indicates matching bits in the evaluator string,
                    'E' indicates matching bits in the empty string.
    - evaluater_string (int): Binary representation of the evaluator string.
    - empty_string (int): Binary representation of the empty string.
    - orientation_shift (int): The number of positions to shift the pattern during comparison which determined the orirentaiton of the pattern.

    Returns:
    int: The count of occurrences of the specified pattern in the evaluated string.
    """
    string = evaluater_string if pattern[3] == 'T' else empty_string

    for i in pattern[-2::-1]:
        if i == 'T':
            string = (string << oreintation_shift) & evaluater_string
        else:
            string = (string << oreintation_shift) & empty_string
    # print_string_alligned(string,'string')
    count = bin(string).count('1')
    # print(count,f'counted {pattern} and orientation {oreintation_shift}')
    return count

def get_player_strings(board: tuple[str, str], agent_piece: BoardPiece)-> tuple[int, int, int, int]:
    """
    Extracts each player's string from the given game board and calculates strings representing the occupied places and empty places.

    Parameters:
    - board (Tuple[str, str]): A tuple of two strings representing the binary board states for each player.
    - agent_piece (BoardPiece): An integer (1 or 2) representing the agent's piece on the board.

    Returns:
    Tuple[int, int, int, int]: A tuple containing four integers:
        - agent_string: Binary representation of the agent's piece on the board.
        - opponent_string: Binary representation of the opponent's piece on the board.
        - occupied_string: Binary representation of the occupied positions on the board.it assumes the virtual top row as occupied as well.
        - empty_string: Binary representation of the empty positions on the board.
    """
    agent_string, opponent_string = (int(board[0],2), int(board[1],2)) if agent_piece == 1 else (int(board[1],2), int(board[0],2))

    occupied_string = agent_string | opponent_string
    occupied_string |= int('0000001000000100000010000001000000100000010000001',2)

    all_one_string = (1 << 49) -1
    empty_string = occupied_string ^ all_one_string

    # print_string_alligned(agent_string,'agent_string')
    # print_string_alligned(opponent_string,'second_string')
    # print_string_alligned(occupied_string,'occupied_string')
    # print_string_alligned(empty_string,'empty_string')
    return agent_string, opponent_string, occupied_string, empty_string

def print_string_alligned(string:int,text:str=None)->None:
    """
    This is just a function for printing strings for sanity checks and debugging.
    Prints the binary representation of an integer in a right-aligned format, 
    followed by an optional text.

    Parameters:
    - string (int): The integer to be converted to binary and printed.
    - text (str, optional): Additional text to be printed next to the binary representation.

    Returns:
    None
    """
    print(format((bin(string)[2:]).zfill(70),'>70'),text)
    return