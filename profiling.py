import numpy as np
import cProfile


from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT
from bitstring import board_to_bitstring
from agents.agent_negamax.negamax_bitstring_heuristics import Node
from agents.agent_negamax.negamax_bitstring_heuristics import iterative_deepening_bitstring
                                                              
def string_to_board(pp_board: str):
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

# python -m Profiling.profile_minimax

board_string = ''' 
 - - - - - - - 
|             |
|             |
|             |
|             |
|      O      |
|      X X    |
 - - - - - - -
 0 1 2 3 4 5 6
'''
board = string_to_board(board_string)
bit_board = board_to_bitstring(board)
print()
print(bit_board)

player = PLAYER1

Node.reset()
Node.skip_order = False
Node.skip_null_window = False
Node.skip_iterative_deepening = False

max_depth = 7
agent_piece = PLAYER2

cProfile.run(
    'iterative_deepening_bitstring(board, agent_piece,maxdepth=max_depth)','profile/negmax_all_in_place.prof'
)