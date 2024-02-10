'''
this test file is only used for the negamax_tree and is used for sanity checks and performance trakcing using a predetermined tree of nodes.
'''


import numpy as np
import random
from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT
from bitstring import board_to_bitstring

from agents.agent_negamax.negamax_tree import Node, iterative_deepening_bitstring


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

def test_all_in_place():
    """
    this is used for step by step sanity checks and debugging
    """
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |  X X   X    |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    Node.reset()
    Node.skip_order = False
    Node.skip_null_window = True
    Node.skip_iterative_deepening = False

    iterative_deepening_bitstring(board, agent_piece=PLAYER1)