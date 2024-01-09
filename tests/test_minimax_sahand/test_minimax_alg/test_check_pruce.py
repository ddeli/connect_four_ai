import numpy as np

from agents.agent_minimax.minimax import *

def test_check_prune_maximizer():
    alpha = float('-inf')
    beta = 3

    board_score = 5
    maximizing_player = True

    alpha, beta, prune = check_prune(board_score, alpha, beta, maximizing_player)
    print('\nalpha:', alpha)
    print('beta:', beta)
    print('prune:', prune)

    assert alpha == 5
    assert beta == 3
    assert prune == True

def test_check_not_prune_maximizer():
    alpha = 3
    beta = float('inf')

    board_score = -6
    maximizing_player = True

    alpha, beta, prune = check_prune(board_score, alpha, beta, maximizing_player)
    print('\nalpha:', alpha)
    print('beta:', beta)
    print('prune:', prune)

    assert alpha == 3
    assert beta == float('inf')
    assert prune == False

def test_check_prune_minimizer():
    alpha = 3
    beta = float('inf')

    board_score = -4
    maximizing_player = False

    alpha, beta, prune = check_prune(board_score, alpha, beta, maximizing_player)
    print('\nalpha:', alpha)
    print('beta:', beta)
    print('prune:', prune)

    assert alpha == 3
    assert beta == -4
    assert prune == True

def test_check_not_prune_minimizer():
    alpha = float('-inf')
    beta = float('inf')

    board_score = 3
    maximizing_player = False

    alpha, beta, prune = check_prune(board_score, alpha, beta, maximizing_player)
    print('\nalpha:', alpha)
    print('beta:', beta)
    print('prune:', prune)

    assert alpha == float('-inf')
    assert beta == 3
    assert prune == False

