from enum import Enum
import numpy as np
from typing import Callable, Optional

BOARD_COLS = 7
BOARD_ROWS = 6
BOARD_SHAPE = (6, 7)
INDEX_HIGHEST_ROW = BOARD_ROWS - 1
INDEX_LOWEST_ROW = 0

BoardPiece = np.int8  # The data type (dtype) of the board pieces
NO_PLAYER = BoardPiece(0)  # board[i, j] == NO_PLAYER where the position is empty
PLAYER1 = BoardPiece(1)  # board[i, j] == PLAYER1 where player 1 (player to move first) has a piece
PLAYER2 = BoardPiece(2)  # board[i, j] == PLAYER2 where player 2 (player to move second) has a piece

BoardPiecePrint = str  # dtype for string representation of BoardPiece
NO_PLAYER_PRINT = BoardPiecePrint(' ')
PLAYER1_PRINT = BoardPiecePrint('X')
PLAYER2_PRINT = BoardPiecePrint('O')

PlayerAction = np.int8  # The column to be played

class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0

class MoveStatus(Enum):
    IS_VALID = 1
    WRONG_TYPE = 'Input is not a number.'
    NOT_INTEGER = ('Input is not an integer, or isn\'t equal to an integer in '
                   'value.')
    OUT_OF_BOUNDS = 'Input is out of bounds.'
    FULL_COLUMN = 'Selected column is full.'

class SavedState:
    pass

GenMove = Callable[
    [np.ndarray, BoardPiece, Optional[SavedState]],  # Arguments for the generate_move function
    tuple[PlayerAction, Optional[SavedState]]  # Return type of the generate_move function
]


def initialize_game_state() -> np.ndarray:
    """
    Returns an ndarray, shape BOARD_SHAPE and data type (dtype) BoardPiece, initialized to 0 (NO_PLAYER).
    """
    array = np.zeros(BOARD_SHAPE, BoardPiece)
    return array


def set_board() -> np.ndarray:
    """
    This is a helper function to set a specific board state in main.py at the beginning of a game for debugging purpose

    :return: the selected preconfigured board
    """
    board1 = np.array([
        [1, 2, 1, 2, 2, 1, 1],
        [1, 2, 1, 2, 1, 2, 1],
        [2, 0, 1, 1, 2, 1, 1],
        [1, 0, 2, 1, 2, 2, 2],
        [2, 0, 0, 0, 2, 2, 1],
        [0, 0, 0, 0, 0, 1, 0]], dtype=int)

    board2 = np.array([
        [1, 1, 2, 1, 2, 2, 2],
        [1, 1, 0, 2, 2, 1, 2],
        [1, 1, 0, 2, 2, 0, 2],
        [2, 2, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0]], dtype=int)

    board3 = np.array([
        [2, 1, 1, 2, 0, 1, 0],
        [0, 2, 2, 1, 0, 1, 0],
        [0, 1, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]], dtype=int)

    return board3


def pretty_print_board(board: np.ndarray) -> str:
    """
    Should return `board` converted to a human readable string representation,
    to be used when playing or printing diagnostics to the console (stdout). The piece in
    board[0, 0] of the array should appear in the lower-left in the printed string representation. Here's an example output, note that we use
    PLAYER1_Print to represent PLAYER1 and PLAYER2_Print to represent PLAYER2):
    |==============|
    |              |
    |              |
    |    X X       |
    |    O X X     |
    |  O X O O     |
    |  O O X X     |
    |==============|
    |0 1 2 3 4 5 6 |
    """
    board_head = "|==============|\n"
    board_body = ""
    board_bottom = "|==============|\n" \
                   "|0 1 2 3 4 5 6 |"

    for row in range(board.shape[0] - 1, -1, -1):
        board_body = board_body + "|"
        for col in range(board.shape[1]):
            if board[row, col] == 0:
                board_body = board_body + "  "
            elif board[row, col] == 1:
                board_body = board_body + "X "
            else:
                board_body = board_body + "O "
        board_body = board_body + "|\n"

    complete_board = board_head + board_body + board_bottom

    return complete_board


def string_to_board(pp_board: str) -> np.ndarray:
    """
    Takes the output of pretty_print_board and turns it back into a ndarray.
    This is quite useful for debugging, when the agent crashed, and you have the last
    board state as a string.

    :param pp_board: current board state as string representation
    :return: board: representation of the board state as a nparray
    """

    # Define the mapping of characters to values ('' for empty, 'X' for Player 1, 'O' for Player 2)
    char_to_value = {'': 0, 'X': 1, 'O': 2}

    # Initialize an empty 6x7 Connect Four board
    board = np.zeros((6, 7), dtype=np.int8)
    lines = pp_board.split('\n')[1:7]  # Extract the lines containing the board
    for i, line in enumerate(lines):
        for j, char in enumerate(line[1:14:2]):  # Skip the leading '|'
            if char in char_to_value:
                board[INDEX_HIGHEST_ROW - i, j] = char_to_value[char]
    return board


def apply_player_action(board: np.ndarray, action: PlayerAction, player: BoardPiece):
    """
    Sets board[i, action] = player, where i is the lowest open row. The input
    board should be modified in place, such that it's not necessary to return
    something.

    :param: board: current board state as a ndarray
    :param: action: player move to apply
    :param: player: current player
    """

    for i in range(BOARD_ROWS):
        if board[i, action] == 0:
            board[i, action] = player
            break


def connected_four(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.

    :param: board: current board state as a ndarray
    :param: player: current player
    :return: bool: determines if player has four connected pieces
    """
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i, j] == player:
                # Check horizontal
                if j + 3 < BOARD_COLS:
                    if all(board[i, j + k] == player for k in range(4)):
                        return True
                # Check vertical
                if i + 3 < BOARD_ROWS:
                    if all(board[i + k, j] == player for k in range(4)):
                        return True
                # Check diagonal (up-right)
                if i + 3 < BOARD_ROWS:
                    if j + 3 < BOARD_COLS:
                        if all(board[i + k, j + k] == player for k in range(4)):
                            return True
                # Check diagonal (up-left)
                if i + 3 < BOARD_ROWS:
                    if j - 3 >= 0:
                        if all(board[i + k, j - k] == player for k in range(4)):
                            return True
    return False


def connected_three(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Returns True if there are three adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.

    :param: board: current board state as a ndarray
    :param: player: current player
    :return: bool: determines if player has three connected pieces
    """
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i, j] == player:
                # Check horizontal
                if j + 2 < BOARD_COLS:
                    if all(board[i, j + k] == player for k in range(3)):
                        return True
                # Check vertical
                if i + 2 < BOARD_ROWS:
                    if all(board[i + k, j] == player for k in range(3)):
                        return True
                # Check diagonal (up-right)
                if i + 2 < BOARD_ROWS:
                    if j + 2 < BOARD_COLS:
                        if all(board[i + k, j + k] == player for k in range(3)):
                            return True
                # Check diagonal (up-left)
                if i + 2 < BOARD_ROWS:
                    if j - 2 >= 0:
                        if all(board[i + k, j - k] == player for k in range(3)):
                            return True
    return False


def check_end_state(board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Returns the current game state for the current `player`, i.e. has their last
    action won (GameState.IS_WIN) or drawn (GameState.IS_DRAW) the game,
    or is play still ongoing (GameState.STILL_PLAYING)?

    :param: board: current board state as a nparray
    :param: player: current player
    :return: GameState: Evaluation of the GameState after a move
    """

    if connected_four(board, player):
        return GameState.IS_WIN
    if np.all(board != NO_PLAYER):
        return GameState.IS_DRAW
    return GameState.STILL_PLAYING


def check_move_status(board: np.ndarray, column: any) -> MoveStatus:
    """
    Returns a MoveStatus indicating whether a move is legal or illegal, and why
    the move is illegal.
    Any column type is accepted, but it needs to be convertible to a number
    and must result in a whole number.
    Furthermore, the column must be within the bounds of the board and the
    column must not be full.
    """
    try:
        numeric_column = float(column)
    except ValueError:
        return MoveStatus.WRONG_TYPE

    is_integer = np.mod(numeric_column, 1) == 0
    if not is_integer:
        return MoveStatus.NOT_INTEGER

    column = PlayerAction(column)
    is_in_range = PlayerAction(0) <= column <= PlayerAction(6)
    if not is_in_range:
        return MoveStatus.OUT_OF_BOUNDS

    is_open = board[-1, column] == NO_PLAYER
    if not is_open:
        return MoveStatus.FULL_COLUMN

    return MoveStatus.IS_VALID


def next_player(player: BoardPiece) -> BoardPiece:
    """
    A function to switch the player after each calculation step of the minimax agent
    :param player: current player
    :return: next player
    """
    if player == PLAYER1:
        player = PLAYER2
    elif player == PLAYER2:
        player = PLAYER1
    return player


def calculate_score(board: np.ndarray) -> int:
    """
    A function to evaluate each move and give it a score
    :param board: current game state
    :return: calculated score of a move
    """
    score = 0
    for i in range(6):
        for j in range(7):
            if board[i, j] == NO_PLAYER:
                score += 1
    return score

