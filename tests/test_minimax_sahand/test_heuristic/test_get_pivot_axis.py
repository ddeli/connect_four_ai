import numpy as np

from agents.agent_minimax.heuristic import *

def test_get_pivot_row():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print('pivot point:',pivot)

    print('pivot point value:',board[pivot])

    row_window, position = get_pivot_row(board,pivot)
    print('row_to_extract:',row_window)
    print('position:',position)
    
    assert position == 3
    assert np.all(row_window == [15, 16, 17, 18, 19, 20, 21]) 


def test_get_pivot_col():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    col_window, position = get_pivot_col(board,pivot)
    print('col_to_extract:',col_window)
    print('position:',position)

    assert position == 2
    assert np.all( col_window == [ 4, 11, 18, 25, 32, 39])

def test_get_pivot_diag():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    diag_window, position = get_pivot_diag(board,pivot)
    print('daig_to_extract:',diag_window)
    print('position:',position)

    assert np.all(diag_window == [ 2, 10, 18, 26, 34, 42])
    assert position == 2

def test_get_pivot_opp_diag():
    board = np.arange(1,43).reshape(6,7)
    print('\n',board)

    pivot = (2,3)
    print(pivot)

    print(board[pivot])

    opp_daig_window, position = get_pivot_opp_diag(board,pivot)
    print(opp_daig_window)
    print(position)

    assert np.all(opp_daig_window == [ 6, 12, 18, 24, 30, 36])
    assert position == 2