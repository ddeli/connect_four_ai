import numpy as np

from agents.agent_minimax.heuristic import *

def test_evaluate_window_player_pieces1():
    window = [1,1,1,0]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [3]

def test_evaluate_window_player_pieces2():
    window = [1,0,1,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [3]

def test_evaluate_window_player_pieces3():
    # this pattern never arises in the single window since it doens't contain a zero.
    window = [1,2,1,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [3]

def test_evaluate_window_player_pieces4():
    window = [1,0,0,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [2]

def test_evaluate_window_player_pieces5():
    window = [0,0,1,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [2]

def test_evaluate_window_player_pieces6():
    window = [1,2,0,1]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [0]

def test_evaluate_window_player_pieces7():
    window = [2,2,0,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_player(window,player)
    print('window score player peices:',window_score)
    assert window_score == [0]


def test_evaluate_window_opponent_pieces1():
    window = [1,1,1,0]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_opponent(window,player)
    print('window score player peices:',window_score)
    assert window_score == [0]

def test_evaluate_window_opponent_pieces2():
    window = [2,2,2,0]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_opponent(window,player)
    print('window score player peices:',window_score)
    assert window_score == [-3]

def test_evaluate_window_opponent_pieces3():
    window = [2,0,2,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_opponent(window,player)
    print('window score player peices:',window_score)
    assert window_score == [-3]

def test_evaluate_window_opponent_pieces4():
    window = [0,0,2,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_opponent(window,player)
    print('window score player peices:',window_score)
    assert window_score == [-2]

def test_evaluate_window_opponent_pieces5():
    window = [1,0,2,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_opponent(window,player)
    print('window score player peices:',window_score)
    assert window_score == [0]

def test_evaluate_window_opponent_pieces6():
    window = [2,0,0,2]
    print('\nwindow:',window)

    player = PLAYER1
    print('\nplayer:',player)

    window_score = evaluate_single_window_opponent(window,player)
    print('window score player peices:',window_score)
    assert window_score == [-2]