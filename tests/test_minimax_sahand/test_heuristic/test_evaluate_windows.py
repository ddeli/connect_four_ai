import numpy as np

from agents.agent_minimax.heuristic import *

def test_evaluate_windows_player():
    '''we have tested the score for a ingle window befoer.
    here the main intereset is to see if the max score among windows
    will be returned correctly'''

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

    direction_score = evaluate_windows_player(windows,player)
    print('direction score:',direction_score)

    assert direction_score == [3]

def test_evaluate_windows_opponent():
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

    direction_score = evaluate_windows_opponent(windows,player)
    print('direction score:',direction_score)

    assert direction_score == [-3]
