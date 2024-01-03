import numpy as np

from agents.agent_minimax.heuristic import *


def test_get_max_height():
    board_string = ''' 
     - - - - - - - 
    |        X    |
    |    X   X    |
    |    X   X   X|
    |  X X X X   X|
    |X X X X X   X|
    |X X X X X X X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    max_height = get_max_height(board)
    print('n\max height is:\n',max_height)

    assert max_height == 5 

def test_get_pivots():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |      X   X  |
    |X   X X X X  |
    |X X X X X X X|
    |X X X X X X X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    all_pivots = get_pivots(board)
    print('\nall pivots:\n', all_pivots)

    assert np.all(all_pivots == [(2, 1), (2, 6), (3, 0), (3, 1), (3, 2), (3, 4), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])

