from enum import Enum
import numpy as np

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

def initialize_game_state() -> np.ndarray:
    """
    Returns an ndarray, shape BOARD_SHAPE and data type (dtype) BoardPiece, initialized to 0 (NO_PLAYER).

    Returns
    -------
    board: numpy.ndarray[BoardPiece]
        An ndarray representing the game board with shape BOARD_SHAPE and dtype BoardPiece,
        initialized to 0 (NO_PLAYER).
    """
    board = np.zeros(BOARD_SHAPE,BoardPiece)
    return board

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

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    board_p: str
        A string representation of the game board for display.
    """

    board_p = np.full((board.shape),NO_PLAYER_PRINT)
    board_p[board==PLAYER1] = PLAYER1_PRINT
    board_p[board==PLAYER2 ] = PLAYER2_PRINT
    board_p = board_p[::-1]
    board_p = ' - - - - - - - \n' + '\n'.join(['|'+' '.join(row)+'|' for row in board_p]) + '\n - - - - - - -'+'\n 0 1 2 3 4 5 6'


    return board_p

def string_to_board(pp_board: str) -> np.ndarray:
    """
    Takes the output of pretty_print_board and turns it back into an ndarray.
    This is quite useful for debugging, when the agent crashed and you have the last
    board state as a string.

    Parameters
    ----------
    pp_board : str
        The string representation of a game board as produced by pretty_print_board.

    Returns
    -------
    board_array: numpy.ndarray
        A NumPy array representing the game board.
    """

    board_array_of_string = pp_board.split('|')[1::2]
    board_array_of_string =np.array([[i for i in row] for row in board_array_of_string])[:,::2]

    board_array = np.zeros(board_array_of_string.shape)
    board_array[board_array_of_string==PLAYER1_PRINT] = PLAYER1
    board_array[board_array_of_string==PLAYER2_PRINT] = PLAYER2
    board_array = board_array[::-1]
    return board_array

def apply_player_action(board: np.ndarray, action: PlayerAction, player: BoardPiece) -> np.ndarray:
    """
    Sets board[i, action] = player, where i is the lowest open row. Raises a ValueError
    if action is not a legal move. If it is a legal move, the modified version of the
    board is returned and the original board should remain unchanged (i.e., either set
    back or copied beforehand).

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    action : PlayerAction
        The column where the player wants to place their piece.
    player : BoardPiece
        The player making the move.

    Returns
    -------
    board: numpy.ndarray
        The modified game board after applying the player's action.
    """

    i = np.count_nonzero(board[:,action])
    board[i,action] = player
    return board

def connected_four(board: np.ndarray, player: BoardPiece) -> bool:
    """
    Returns True if there are four adjacent pieces equal to `player` arranged
    in either a horizontal, vertical, or diagonal line. Returns False otherwise.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    player : BoardPiece
        The peice for the player that made the last move.

    Returns
    -------
    bool
        True if there are four consecutive pieces of the specified player, False otherwise.
    """
    # Check horizontal (rows)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS-3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical (columns)
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS-3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (positive)
    for row in range(BOARD_ROWS-3):
        for col in range(BOARD_COLS-3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (negative)
    for row in range(BOARD_ROWS-3):
        for col in range(BOARD_COLS-3):
            if all(board[:,::-1][row + i][col + i] == player for i in range(4)):
                return True

    return False

def check_end_state(board: np.ndarray, player: BoardPiece) -> GameState:
    """
    Returns the current game state for the current `player`, i.e. has their last
    action won (GameState.IS_WIN) or drawn (GameState.IS_DRAW) the game,
    or is play still on-going (GameState.STILL_PLAYING)?

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    player : BoardPiece
        The player for whom the end state is checked.

    Returns
    -------
    GameState
        The current game state for the specified player:
        - GameState.IS_WIN if the player has won.
        - GameState.IS_DRAW if the game is a draw.
        - GameState.STILL_PLAYING if the game is still ongoing.
    """
    if connected_four(board,player):
        return(GameState.IS_WIN)
    elif np.count_nonzero(board) == BOARD_ROWS * BOARD_COLS:
        return(GameState.IS_DRAW)   
    else:
        return(GameState.STILL_PLAYING)

class MoveStatus(Enum):
    IS_VALID = 1
    WRONG_TYPE = 'Input is not a number.'
    NOT_INTEGER = ('Input is not an integer, or isn\'t equal to an integer in '
                   'value.')
    OUT_OF_BOUNDS = 'Input is out of bounds.'
    FULL_COLUMN = 'Selected column is full.'

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

# Week 2
from typing import Callable, Optional

class SavedState:
    pass


GenMove = Callable[
    [np.ndarray, BoardPiece, Optional[SavedState]],  # Arguments for the generate_move function
    tuple[PlayerAction, Optional[SavedState]]  # Return type of the generate_move function
]