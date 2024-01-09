# this file was used to do print outs and sanity check for the heuristic. it is not in use at this point.
import numpy as np

from agents.agent_minimax.heuristic import *

def test_heuristic_1():
    #use this array to test functions in heuristic module
    board = np.arange(1,43).reshape(6,7)
    print(board)

    pivot_point = (4,2)
    print(board[pivot_point])
    return


def test_heuristic_2():
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
    print(board_string)
    print(board)

    pivot = (2,3)
    print(pivot)

    player = 2

    score = evaluate_at_pivot(board,pivot,player)
    print(score)

def test_extract_windows():
    array = [0,1,2,3,4,5,6]
    position = 3
    windows = extract_windows(array,position)
    print(windows)

def test_pivot_row():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    row_window, position = pivot_row(board,pivot)
    print('row_to_extract:',row_window)
    print('position:',position)


def test_pivot_col():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    col_window, position = pivot_col(board,pivot)
    print('col_to_extract:',col_window)
    print('position:',position)


def test_pivot_diag():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    diag_window, position = pivot_diag(board,pivot)
    print('daig_to_extract:',diag_window)
    print('position:',position)

def test_pivot_opp_diag():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    opp_daig_window, position = pivot_opp_diag(board,pivot)
    print(opp_daig_window)
    print(position)

def test_evaluate_window_player_pieces():
    
    window = [1,0,1,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_window_player_pieces(window,player)
    print('window score player peices:',window_score)


def test_evaluate_window_opponent_pieces():
    
    window = [2,0,0,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_window_opponent_pieces(window,player)
    print('window score opponent peices:',window_score)


def test_evaluate_single_direction():
    # This is an example where evaluate_single_directin returns 
    # a score of 2 instead of 3 when we have the break line 
    row_window = [0,1,1,0,1,2,2]
    position = 3
    windows = [
        [0,1,1,0],
        [1,1,0,1],
        [1,0,1,1],
        [0,1,1,2]
    ]

    player = PLAYER1
    print('\nplayer:',player)

    direction_score = evaluate_single_direction(windows,player)
    print('direction score:',direction_score)

def test_evaluate_single_direction_player():
    # This is an example where evaluate_single_directin returns 
    # a score of 2 instead of 3 when we have the break line 
    row_window = [0,1,1,0,1,2,2]
    position = 3
    windows = [
        [0,1,1,0],
        [1,1,0,1],
        [1,0,1,1],
        [0,1,1,2]
    ]

    player = PLAYER1
    print('\nplayer:',player)

    direction_score = evaluate_single_direction_player(windows,player)
    print('direction score:',direction_score)

def test_evaluate_single_direction_opponent():
    # This is an example where evaluate_single_directin returns 
    # a score of 2 instead of 3 when we have the break line 
    row_window = [0,1,1,0,1,2,2]
    position = 3
    windows = [
        [0,1,1,0],
        [1,1,0,1],
        [1,0,1,1],
        [0,1,1,2]
    ]

    player = PLAYER2
    print('\nplayer:',player)

    direction_score = evaluate_single_direction_opponent(windows,player)
    print('direction score:',direction_score)

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

def test_evaluate_diag():
 
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

def test_aggregate_scores():
    all_pivot_scores_player = [0,0,2,2,3,2,2,0]
    all_pivot_scores_opponent = [0,0,-3,-2,-2,-2,0,0]

    board_score = aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent)

    print('board score:',board_score)

def test_get_pivots():
    board_string = ''' 
     - - - - - - - 
    |X            |
    |X X          |
    |X X X        |
    |X X X X      |
    |X X X X X    |
    |X X X X X X  |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    all_pivots = get_pivots(board)
    print('\nall pivots:\n', all_pivots)

def test_evaluate_board():
    board_string = ''' 
     - - - - - - - 
    |X            |
    |X O          |
    |O X O O      |
    |X O X O      |
    |O X O X X    |
    |X O X X X X  |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)
    
    player = PLAYER1

    board_score = evaluate_board(board,player)
    print('board score:',board_score)

