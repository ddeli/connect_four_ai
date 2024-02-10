
import numpy as np
import random
import time
from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT
from bitstring import board_to_bitstring, check_for_draw_bitstring
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


def test_all_in_place():
    """
    this is used for step by step sanity checks and debugging.
    also for timing the agent in different scenarios and for different inputs.
    """
    board_string = ''' 
     - - - - - - - 
    |O O X X O X X|
    |X X O X X X O|
    |O X X X O O X|
    |X O O O X X O|
    |O O X X O O X|
    |O O O X X O O|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    bit_board = board_to_bitstring(board)
    print()
    print(bit_board)

    draw = check_for_draw_bitstring(bit_board)
    print(f'game is draw? {draw}')

    Node.reset()
    Node.skip_order = False
    Node.skip_null_window = False
    Node.skip_iterative_deepening = False

    max_depth = 2
    agent_piece = PLAYER2
    start_time = time.time()
    best_move, Node.instances = iterative_deepening_bitstring(board, agent_piece,maxdepth=max_depth)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(board_string)
    print(f'player: {agent_piece}')
    print(f'iterative deepening: {Node.skip_iterative_deepening}')
    print(f'Null Window: {Node.skip_null_window}')
    print(f'elapsed time is {elapsed_time}')
    print(f'Nodenumber is {Node.nodenumber}')
    print(f'Nodes visited are {Node.hitcount}')
    print(f'max depth is {max_depth}')