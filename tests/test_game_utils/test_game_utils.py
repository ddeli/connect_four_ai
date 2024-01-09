import numpy as np

from game_utils import BoardPiece, \
    NO_PLAYER, PLAYER1, PLAYER2, initialize_game_state, \
    pretty_print_board, string_to_board, apply_player_action, \
    connected_four, check_end_state, GameState, calculate_score, \
    next_player


def test_initialize_game_state():
    ret = initialize_game_state()
    # print(ret)

    assert isinstance(ret, np.ndarray)
    assert ret.dtype == BoardPiece
    assert ret.shape == (6, 7)
    assert np.all(ret == NO_PLAYER)


def test_pretty_print_board_empty():
    ret = initialize_game_state()
    board_print = pretty_print_board(ret)

    empty_board = "|==============|\n" \
                  "|              |\n" \
                  "|              |\n" \
                  "|              |\n" \
                  "|              |\n" \
                  "|              |\n" \
                  "|              |\n" \
                  "|==============|\n" \
                  "|0 1 2 3 4 5 6 |"

    assert board_print == empty_board


def test_pretty_print_board_first_round():
    ret = initialize_game_state()

    ret[0, 0] = 1
    ret[0, 1] = 2

    board_print2 = pretty_print_board(ret)

    second_round_board = "|==============|\n" \
                         "|              |\n" \
                         "|              |\n" \
                         "|              |\n" \
                         "|              |\n" \
                         "|              |\n" \
                         "|X O           |\n" \
                         "|==============|\n" \
                         "|0 1 2 3 4 5 6 |"

    assert board_print2 == second_round_board


def test_string_to_board():
    # Initialize Board
    ret = initialize_game_state()

    print()
    # Add some Player actions
    ret[0, 0] = 1
    ret[1, 0] = 2
    ret[0, 1] = 1
    ret[1, 1] = 2
    ret[0, 2] = 2
    ret[1, 2] = 1
    ret[0, 3] = 2
    ret[1, 3] = 1
    ret[0, 4] = 1
    ret[1, 4] = 2
    ret[0, 5] = 1
    ret[1, 5] = 2
    ret[0, 6] = 1
    ret[1, 6] = 2

    ret[2, 0] = 1
    ret[3, 0] = 2
    ret[2, 1] = 1
    ret[3, 1] = 2

    ret[4, 0] = 1
    ret[5, 0] = 2
    ret[4, 1] = 1
    ret[5, 1] = 2

    print(ret)
    print()

    # Board to string
    board_print = pretty_print_board(ret)

    print(board_print)
    print()

    # String to board
    back_from_string = string_to_board(board_print)
    print(back_from_string)

    # Back and forth transformation should bring the same array
    assert (back_from_string == ret).all()


def test_apply_player_action_legal():
    set_board = initialize_game_state()

    # Add some Player actions manually
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[2, 0] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[4, 0] = PLAYER1
    set_board[5, 0] = PLAYER2

    # Add same Player action with function
    ret = initialize_game_state()
    apply_player_action(ret, np.int8(0), PLAYER1)
    apply_player_action(ret, np.int8(0), PLAYER2)
    apply_player_action(ret, np.int8(0), PLAYER1)
    apply_player_action(ret, np.int8(0), PLAYER2)
    apply_player_action(ret, np.int8(0), PLAYER1)
    apply_player_action(ret, np.int8(0), PLAYER2)

    assert (ret == set_board).all()


def test_connected_four_player1_true():
    set_board = initialize_game_state()
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 3] = PLAYER1

    # print(set_board)

    assert (connected_four(set_board, PLAYER1))


def test_connected_four_player2_true():
    set_board = initialize_game_state()
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    set_board[4, 0] = PLAYER2

    # print(set_board)

    assert (connected_four(set_board, PLAYER2))


def test_connected_four_player1_false():
    set_board = initialize_game_state()
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    assert (connected_four(set_board, PLAYER1)) is False


def test_connected_four_player1_border_bending_false():
    set_board = initialize_game_state()
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER1
    set_board[4, 0] = PLAYER1
    set_board[5, 0] = PLAYER1
    print(set_board)
    assert (connected_four(set_board, PLAYER1)) is False


def test_connected_four_player2_false():
    set_board = initialize_game_state()
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2

    assert (connected_four(set_board, PLAYER2)) is False


def test_check_end_state_win():
    set_board = initialize_game_state()
    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 3] = PLAYER1

    assert check_end_state(set_board, PLAYER1) == GameState.IS_WIN


def test_check_end_state_draw():
    board = np.full((6, 7), 10)

    assert check_end_state(board, PLAYER1) == GameState.IS_DRAW
    assert check_end_state(board, PLAYER2) == GameState.IS_DRAW


def test_check_end_state_still_playing():
    board = initialize_game_state()

    assert check_end_state(board, PLAYER1) == GameState.STILL_PLAYING
    assert check_end_state(board, PLAYER2) == GameState.STILL_PLAYING


def test_next_player_player1_to_player2():
    assert next_player(PLAYER1) == PLAYER2


def test_next_player_player2_to_player1():
    assert next_player(PLAYER2) == PLAYER1


# Test cases for calculate_score
def test_calculate_score_all_cells_empty():
    board = np.array([[0] * 7] * 6)
    expected_score = 42
    assert calculate_score(board) == expected_score


def test_calculate_score_no_empty_cells():
    board = np.array([[1, 2, 1, 2, 1, 2, 1],
                      [2, 1, 2, 1, 2, 1, 2],
                      [1, 2, 1, 2, 1, 2, 1],
                      [2, 1, 2, 1, 2, 1, 2],
                      [1, 2, 1, 2, 1, 2, 1],
                      [2, 1, 2, 1, 2, 1, 2]], dtype=int)
    expected_score = 0
    assert calculate_score(board) == expected_score


def test_calculate_score_one_empty_cell():
    board = np.array([[1, 2, 1, 2, 1, 2, 0],
                      [2, 1, 2, 1, 2, 1, 2],
                      [1, 2, 1, 2, 1, 2, 1],
                      [2, 1, 2, 1, 2, 1, 2],
                      [1, 2, 1, 2, 1, 2, 1],
                      [2, 1, 2, 1, 2, 1, 2]], dtype=int)
    expected_score = 1
    assert calculate_score(board) == expected_score


def test_calculate_score_seven_empty_cells():
    board = np.array([[1, 2, 0, 2, 1, 2, 0],
                      [2, 1, 2, 1, 2, 1, 2],
                      [1, 2, 1, 2, 0, 2, 1],
                      [2, 1, 2, 0, 2, 1, 2],
                      [1, 0, 1, 2, 1, 2, 0],
                      [2, 1, 2, 1, 2, 0, 2]], dtype=int)
    expected_score = 7
    assert calculate_score(board) == expected_score


