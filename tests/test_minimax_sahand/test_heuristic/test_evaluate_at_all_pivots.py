import numpy as np

from agents.agent_minimax.heuristic import *

def test_evlaute_at_all_pivots():
    
    board_string = ''' 
     - - - - - - - 
    |  O       X  |
    |    O   X    |
    |        O O  |
    |    X X O    |
    |  O   X   X  |
    |O     X     X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    player = PLAYER1

    pivot_1 = (3,3)
    pivot_2 = (1,2)
    all_pivots = [pivot_1,pivot_2]

    all_pivot_scores_player, all_pivot_scores_opponent = evlaute_at_all_pivots(board,all_pivots,player)
    print('player score at all pivots:',all_pivot_scores_player)
    print('opponent scores at all pivots:', all_pivot_scores_opponent)

    assert np.all(all_pivot_scores_player == [0, 3, 3, 0, 2, 0, 0, 0])
    assert np.all(all_pivot_scores_opponent == [-2, 0, 0, -3, 0, 0, 0, 0])
