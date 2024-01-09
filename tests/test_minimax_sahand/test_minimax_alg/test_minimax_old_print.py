# This file along with the minimax_old_print_test in the agent_minimax folder was used during
# minimimax agent implementation to do print out and sanity checks step by step.
# board inputs were changed and the evaluate function in the agent_minimax was manipulated to predict
# the prints and do sanity checks.
# minimax function was initially named iterate_states and then was renamed to minimax() 

import numpy as np

from game_utils import *
from agents.common import *
from agents.agent_minimax.minimax import *


def test_minimax_1():
    board_string = ''' 
    - - - - - - - 
    |             |
    |             |
    |        O    |
    |O O   X X X  |
    |X O   X O X  |
    |X X O X O O X|
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    return

def test_get_valid_moves():
    board_string = ''' 
     - - - - - - - 
    |        O    |
    |        O    |
    |        O    |
    |O O   X X X  |
    |X O   X O X  |
    |X X O X O O X|
     - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    valid_moves = get_valid_moves(board)
    print(valid_moves)
    return

def test_iterate_states():
    board_string = ''' 
    - - - - - - - 
    |    O O O O O|
    |    O O O O O|
    |    O O O O O|
    |O O O O O O O|
    |O O O O O O O|
    |O O O O O O O|
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    # board_copy = board.copy() it is not necessary if you are suare you are making a copy in the agent before applying actions there
    
    player = PLAYER1
    depth = DEPTH
    alpha = float('-inf')
    beta = float('inf')

    score = minimax(board,player, depth,alpha, beta, maximizing_player = True, i=np.array([0]))
    print('\nOriginal\n'
        ,pretty_print_board(board))
    print('score is :',score)
    return

def test_generate_move_minimax():
    board_string = ''' 
    - - - - - - - 
    |    O O O O O|
    |    O O O O O|
    |    O O O O O|
    |O O O O O O O|
    |O O O O O O O|
    |O O O O O O O|
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    # board_copy = board.copy() it is not necessary if you are suare you are making a copy in the agent before applying actions there
    best_move, best_eval = generate_move_minimax(board,player = PLAYER2, saved_state=None)
    print('best columns to take is:',best_move,
          f'best board score is:', best_eval)
    return

def test_generate_move_minimax_zero():
    board_string = ''' 
    - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
    - - - - - - -
    0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    # board_copy = board.copy() it is not necessary if you are suare you are making a copy in the agent before applying actions there
    best_move = generate_move_minimax(board,player = PLAYER2, saved_state=None)
    print('best columns to take is:',best_move)
    return


    