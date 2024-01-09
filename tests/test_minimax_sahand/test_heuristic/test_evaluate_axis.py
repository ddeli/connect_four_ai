import numpy as np

from agents.agent_minimax.heuristic import *

def test_evaluate_row():
    # note that evaluate_row returns 3 only once although there is
    # two sequence of three. but their value is the same. 
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |X X X   X X X|
    |             |
    |             |
    |             |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    player = PLAYER1
    pivot = (3,3)

    row_score_player,row_score_opponent = evaluate_row(board,pivot,player)
    print('\nplayer row score:',row_score_player)
    print('opponent row score:',row_score_opponent)

    assert row_score_player == [3]
    assert row_score_opponent == [0]

def test_evaluate_col():
 
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |      O      |
    |      O      |
    |      X      |
    |      O      |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    player = PLAYER1
    pivot = (4,3)
    print(board[pivot])

    col_score_player,col_score_opponent = evaluate_col(board,pivot,player)
    print('\nplayer col score:',col_score_player)
    print('opponent col score:',col_score_opponent)

    assert col_score_player == [0]
    assert col_score_opponent == [-2]

def test_evaluate_diag():
    # The diagonal is flipped here because of the convention.
 
    board_string = ''' 
     - - - - - - - 
    |  O       X  |
    |    O   X    |
    |             |
    |    X   O    |
    |  O       X  |
    |O           X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    player = PLAYER1
    pivot = (3,3)
    print(board[pivot])

    diag_score_player,diag_score_opponent = evaluate_diag(board,pivot,player)
    print('\nplayer diag score:',diag_score_player)
    print('opponent diag score:',diag_score_opponent)

    assert diag_score_player == [3]
    assert diag_score_opponent == [0]

def test_evaluate_opp_diag():
 
    board_string = ''' 
     - - - - - - - 
    |  O       X  |
    |    O   X    |
    |             |
    |    X   O    |
    |  O       X  |
    |O           X|
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    player = PLAYER1
    pivot = (3,3)
    print(board[pivot])

    opp_diag_score_player,opp_diag_score_opponent = evaluate_opp_diag(board,pivot,player)
    print('\nplayer diag score:',opp_diag_score_player)
    print('opponent diag score:',opp_diag_score_opponent)

    assert opp_diag_score_player == [0]
    assert opp_diag_score_opponent == [-3]