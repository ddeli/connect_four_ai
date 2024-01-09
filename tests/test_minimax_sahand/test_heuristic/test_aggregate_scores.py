import numpy as np

from agents.agent_minimax.heuristic import *

def test_aggregate_scores1():
    all_pivot_scores_player = [0,0,2,3,3,2,2,0]
    all_pivot_scores_opponent = [0,0,-3,-2,-2,-2,0,0]

    board_score = aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent)

    print('board score:',board_score)
    assert board_score == 500

def test_aggregate_scores2():
    all_pivot_scores_player = [0,0,2,3,2,2,2,0]
    all_pivot_scores_opponent = [0,0,-3,-3,-2,-2,0,0]

    board_score = aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent)

    print('board score:',board_score)
    assert board_score == -500

def test_aggregate_scores3():
    all_pivot_scores_player = [0,0,2,3,3,2,2,0]
    all_pivot_scores_opponent = [0,0,-3,-3,-2,-2,0,0]

    board_score = aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent)

    print('board score:',board_score)
    assert board_score == 10