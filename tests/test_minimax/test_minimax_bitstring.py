import numpy as np

from agents.agent_minimax.minimax_bitstring import generate_move_minimax_bitstring
from game_utils import PLAYER1, PLAYER2, pretty_print_board


def test_generate_move_minimax_player1_win():

    board = np.array([
        [1, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 1, 2, 2],
        [1, 2, 1, 1, 2, 1, 1],
        [2, 1, 2, 1, 2, 2, 2],
        [1, 2, 1, 2, 1, 0, 0],
        [2, 1, 0, 0, 0, 0, 0]], dtype=int)

    print()
    print(pretty_print_board(board))

    player1_move_to_win = 3
    next_move = generate_move_minimax_bitstring(board, PLAYER1, saved_state=None)[0]

    assert(next_move == player1_move_to_win)


def test_generate_move_minimax_player2_win():
    board = np.array([
        [1, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 1, 2, 2],
        [1, 2, 1, 1, 2, 1, 1],
        [2, 1, 2, 1, 2, 2, 2],
        [1, 1, 2, 2, 1, 0, 0],
        [2, 1, 0, 0, 0, 0, 0]], dtype=int)

    print()
    print(board)

    player2_move_to_win = 4

    next_move = generate_move_minimax_bitstring(board, PLAYER2, saved_state=None)[0]

    assert (next_move == player2_move_to_win)


def test_generate_move_minimax_player1_block():
    board = np.array([
        [1, 1, 1, 2, 0, 0, 1],
        [2, 2, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]], dtype=int)

    print()
    print(board)

    player1_move_to_block = 2

    next_move = generate_move_minimax_bitstring(board, PLAYER1, saved_state=None)[0]

    assert (next_move == player1_move_to_block)


def test_generate_move_minimax_player2_block():
    board = np.array([
        [2, 2, 2, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]], dtype=int)

    print()
    print(board)

    player1_move_to_block = 2

    next_move = generate_move_minimax_bitstring(board, PLAYER2, saved_state=None)[0]

    assert (next_move == player1_move_to_block)
