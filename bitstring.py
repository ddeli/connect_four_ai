import numpy as np

from game_utils import BoardPiece, PlayerAction, BOARD_COLS, BOARD_ROWS


def board_to_bitstring(board: np.ndarray) -> str:
    """
    A function to convert a given board as numpy.ndarray to a bitstring representation for PLAYER1 and PLAYER2

    :param board: current game state as numpy.ndarray
    :return: bitstring_array: a bitstring representation for
    PLAYER1 (bitstring_array[0]) and PLAYER2 (bitstring_array[1])
    """
    bitstring_array = ['', '']

    for col in range(6):

        for row in range(6):
            if board[row, col] == 1:
                bitstring_array[0] += '1'
                bitstring_array[1] += '0'
            elif board[row, col] == 2:
                bitstring_array[0] += '0'
                bitstring_array[1] += '1'
            elif board[row, col] == 0:
                bitstring_array[0] += '0'
                bitstring_array[1] += '0'
        bitstring_array[0] += '0'
        bitstring_array[1] += '0'
    return bitstring_array


def connect_four_bitstring(binary_str: str, player: BoardPiece) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.

    :param: board: current board state as a ndarray
    :param: player: current player
    :return: bool: determines if player has four connected pieces
    """
    binary = int(binary_str[player-1], 2)

    # Horizontal check
    m = binary & (binary >> 7)
    if m & (m >> 14):
        return True  # Diagonal \
    m = binary & (binary >> 6)
    if m & (m >> 12):
        return True  # Diagonal /
    m = binary & (binary >> 8)
    if m & (m >> 16):
        return True
    # Vertical
    m = binary & (binary >> 1)
    if m & (m >> 2):
        return True

    return False


def make_move_bitstring(binary_array: str, action: PlayerAction, player: BoardPiece) -> str:
    if player == 1:
        binary_player = binary_array[0]
        binary_opponent = binary_array[1]
    else:
        binary_player = binary_array[1]
        binary_opponent = binary_array[0]
    for i in range(0, 6):
        if binary_player[action*7+5-i] == '0' and binary_opponent[action*7+5-i] == '0':
            string_list = list(binary_player)
            string_list[action*7+5-i] = '1'
            modified_binary = ''.join(string_list)
            binary_array[player - 1] = modified_binary
            break
    return binary_array


def calculate_score_bitstring(binary_array: str) -> int:

    score = 0
    for player in range(0, 2):
        for bit in binary_array[player]:
            if bit == '1':
                score += 1
    return BOARD_COLS*BOARD_ROWS-score


def bitstring_to_board(binary_array: str, player: BoardPiece) -> np.ndarray:

    if player == 1:
        binary = binary_array[0]
    else:
        binary = binary_array[1]

    board = np.zeros((6, 7), dtype=np.int8)
    split_array = []
    for i in range(0, len(binary), 7):
        split_array.append(binary[i: i + 6])

    for i, line in enumerate(split_array[::-1]):
        for j, char in enumerate(line):
            if char == '1' and player == 1:
                board[j, 5 - i] = 1
            if char == '1' and player == 2:
                board[j, 5 - i] = 2

    return board
