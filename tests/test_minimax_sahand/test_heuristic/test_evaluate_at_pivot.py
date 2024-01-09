import numpy as np

from agents.agent_minimax.heuristic import *

def test_evaluate_at_pivot():
    
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
    pivot = (3,3)
    print(board[pivot])

    pivot_score_player, pivot_score_opponent = evaluate_at_pivot(board,pivot,player)
    print('player score at pivot:',pivot_score_player)
    print('opponent score at pivot:', pivot_score_opponent)

    assert pivot_score_player == [0,3,3,0]
    assert pivot_score_opponent == [-2,0,0,-3]