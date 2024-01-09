import numpy as np

from agents.agent_minimax.minimax import *

def test_get_valid_moves():
    board_string = ''' 
     - - - - - - - 
    |X     O   O  |
    |X O   O   O  |
    |O X O O   O  |
    |X O X O   O  |
    |O X O X X O  |
    |X O X X X X  |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    valid_moves = get_valid_moves(board)
    print(valid_moves)
    assert np.all(valid_moves == [1,2,4,6])

    