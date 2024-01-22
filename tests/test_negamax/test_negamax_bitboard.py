import numpy as np
from agents.agent_negamax.negamax_bitstring import Node, iterative_deepening_bitstring
from game_utils_sahand import PLAYER1, PLAYER2, string_to_board
from bitstring import board_to_bitstring, bitstring_to_board


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