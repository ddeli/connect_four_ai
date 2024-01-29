from connect_four_ai.agents.agent_negamax.heuristic_bitboard import evaluate_board, evaluate_board_simple_heuristic
import numpy as np
import copy
from play import agent_vs_agent
from game_utils import PLAYER1, PLAYER2, BoardPiece, GameState, BOARD_COLS
from game_utils import pretty_print_board, check_end_state, apply_player_action
from typing import Optional, Callable
from bitstring import (
    board_to_bitstring,
    apply_player_action_bitstring,
    calculate_score_bitstring,
    bitstring_to_board,
    check_end_state_bitstring,

    copy_bitstring_array,
    get_valid_moves_bitstring,
)
# in the play function we should make sure to return who won, which player won ex. score[player]=score
# {Player1={2, 1, 3,...}, }
# 

from connect_four_ai.agents.agent_negamax.negamax_bitstring import iterative_deepening_bitstring
connected_three_pieces=[2, 5, 0]
connected_two_pieces=[1, 1, 0]
for i in range(3):
    iterator=[x for x in range(3) if x != i]
    for j in iterator:
        output=agent_vs_agent(generate_move_1=iterative_deepening_bitstring(threepiece_score=connected_three_pieces[i], twopiece_score=connected_two_pieces[i]),
        generate_move_2=iterative_deepening_bitstring(threepiece_score=connected_three_pieces[j], twopiece_score=connected_two_pieces[j]) )     



