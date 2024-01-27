from agents.agent_negamax.heuristic_bitboard_el import evaluate_board, evaluate_board_simple_heuristic
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


from agents.agent_negamax.negamax_bitstring_el import iterative_deepening_bitstring
connected_three_pieces=[2, 5]
agent_vs_agent(
    generate_move_1=iterative_deepening_bitstring(threepiece_score=2),
    generate_move_2=iterative_deepening_bitstring(threepiece_score=5) )     



