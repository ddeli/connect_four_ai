import numpy as np
import random
from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT
from bitstring import board_to_bitstring
from agents.agent_negamax.negamax_bitstring_heuristics import Node
from agents.agent_negamax.negamax_bitstring_heuristics import iterative_deepening_bitstring, order_moves, get_pv

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

def test_get_pv():
    desinged_pv = [3,6,2]
    Node(nodenumber=0, board=[], depth=3, parent=None, parent_move=None, best_move=3, best_child=1)
    Node(nodenumber=1, board=[], depth=2, parent=0, parent_move=3, best_move=6, best_child=3)
    Node(nodenumber=3, board=[], depth=1, parent=1, parent_move=6, best_move=2, best_child=9)
    Node(nodenumber=9, board=[], depth=0, parent=3, parent_move=2, best_move=None, best_child=None)

    get_pv()
    print(Node.pv)

    assert Node.pv == desinged_pv


def test_order_moves_pv():
    Node.pv[:] = [1,3,4,5]
    Node.principle_move_taken = 0

    moves = [0,1,2,3,5]
    print('\navaialbel moves:', moves)
    moves_1 = order_moves(moves)
    print(f'ordered move:',moves_1)
    

    moves = [0,1,2,3,5]
    print('\navaialbel moves:', moves)
    moves_2 = order_moves(moves)
    print(f'ordered move:',moves_2)

    moves = [0,1,2,3,5]
    print('\navaialbel moves:', moves)
    moves_3 = order_moves(moves)
    print(f'ordered move:',moves_3)

    moves = [0,1,2,3,5]
    print('\navaialbel moves:', moves)
    moves_4 = order_moves(moves)
    print(f'ordered move:',moves_4)

    moves = [0,1,2,3,5]
    print('\navaialbel moves:', moves)
    random.seed(0)
    moves_5 = order_moves(moves,'random')
    print(f'ordered move:',moves_5)
    
    assert moves_1 == [1, 0, 2, 3, 5]
    assert moves_2 == [3, 0, 1, 2, 5]
    assert moves_3 == [3, 2, 1, 5, 0]
    assert moves_4 == [3, 2, 1, 5, 0]
    assert moves_5 == [2, 1, 0, 5, 3]

def test_all_in_place():
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

    Node.skip_order = False
    Node.skip_null_window = False
    Node.skip_iterative_deepening = False

    iterative_deepening_bitstring(board, agent_piece=PLAYER1)