from game_utils import initialize_game_state, PLAYER1, PLAYER2, pretty_print_board
from bitstring import board_to_bitstring, connected_four_bitstring, apply_player_action_bitstring, \
    calculate_score_bitstring, \
    bitstring_to_board, check_for_draw_bitstring, check_end_state_bitstring, get_valid_moves_bitstring
from heuristic_bitstring_deniz import evaluate

def test_evaluate_bitstring_board():

        set_board = initialize_game_state()

        set_board[0, 3] = PLAYER1
        set_board[0, 0] = PLAYER2
        set_board[0, 2] = PLAYER1
        set_board[0, 4] = PLAYER1
        set_board[0, 6] = PLAYER1

        print()
        print(pretty_print_board(set_board))
        positions = board_to_bitstring(set_board)
        print(positions)

        evaluate(positions, 1)





