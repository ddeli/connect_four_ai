from game_utils import initialize_game_state, PLAYER1, PLAYER2, pretty_print_board
from bitstring import board_to_bitstring, connected_four_bitstring, apply_player_action_bitstring, calculate_score_bitstring, \
    bitstring_to_board, check_for_draw_bitstring, check_end_state_bitstring


def test_board_to_bitstring():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    # set_board[4, 0] = PLAYER2
    # set_board[0, 3] = PLAYER1

    print()
    print(pretty_print_board(set_board))
    positions = board_to_bitstring(set_board)
    print(positions)
    position1Dec = int(positions[0], 2)
    print(position1Dec)
    print()
    print(int(bin(position1Dec)[2:]))

    position1 = position1Dec

    m = position1 & (position1 >> 1)
    if m & (m >> 2):
        print("True")
    else:
        print("False")


def test_connect_four_bitstring_player1_false():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    # set_board[4, 0] = PLAYER2
    # set_board[0, 3] = PLAYER1

    print()
    print(pretty_print_board(set_board))
    positions = board_to_bitstring(set_board)
    print(positions)
    # binary = int(positions[0], 2)
    # print(binary)
    # print(int(bin(binary)[2:]))
    # print(connect_four_bitstring(binary))

    assert (connected_four_bitstring(positions, PLAYER1)) is False


def test_connect_four_bitstring_player2_false():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    # set_board[4, 0] = PLAYER2
    # set_board[0, 3] = PLAYER1

    print()
    print(pretty_print_board(set_board))
    positions = board_to_bitstring(set_board)
    print(positions)
    # binary = int(positions[1], 2)
    # print(binary)
    # print(int(bin(binary)[2:]))
    # print(connect_four_bitstring(binary))

    assert (connected_four_bitstring(positions, PLAYER2)) is False


def test_connect_four_bitstring_player2_overlap_false():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER2
    set_board[3, 0] = PLAYER2
    set_board[0, 1] = PLAYER2
    set_board[4, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[5, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    # set_board[4, 0] = PLAYER2
    # set_board[0, 3] = PLAYER1

    print()
    print(pretty_print_board(set_board))
    positions = board_to_bitstring(set_board)
    print(positions)
    # binary = int(positions[1], 2)
    # print(binary)
    # print(int(bin(binary)[2:]))
    # print(connect_four_bitstring(binary))

    assert (connected_four_bitstring(positions, PLAYER2)) is False


def test_connect_four_bitstring_player1_true():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    # set_board[4, 0] = PLAYER2
    set_board[0, 3] = PLAYER1

    print()
    print(pretty_print_board(set_board))
    positions = board_to_bitstring(set_board)
    print(positions)
    # binary = int(positions[1], 2)
    # print(binary)
    # print(int(bin(binary)[2:]))
    # print(connect_four_bitstring(binary))

    assert (connected_four_bitstring(positions, PLAYER1)) is True


def test_connect_four_bitstring_player2_true():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    set_board[4, 0] = PLAYER2
    # set_board[0, 3] = PLAYER1

    print()
    print(pretty_print_board(set_board))
    positions = board_to_bitstring(set_board)
    print(positions)
    # binary = int(positions[1], 2)
    # print(binary)
    # print(int(bin(binary)[2:]))
    # print(connect_four_bitstring(binary))

    assert (connected_four_bitstring(positions, PLAYER2)) is True


def test_bitstring_to_board():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    set_board[4, 0] = PLAYER2

    print()
    print(set_board)
    print(pretty_print_board(set_board))
    print(board_to_bitstring(set_board))

    bitstring = board_to_bitstring(set_board)
    print(bitstring)

    re_board = bitstring_to_board(bitstring, 1) + bitstring_to_board(bitstring, 2)

    print(pretty_print_board(re_board))

    assert (re_board == set_board).all()


def test_calculate_score_bitstring():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    set_board[4, 0] = PLAYER2

    bitstring = board_to_bitstring(set_board)

    score = calculate_score_bitstring(bitstring)
    print()
    print(score)

    assert (score == 34)


def test_apply_player_action_bitstring():
    set_board = initialize_game_state()

    set_board[0, 0] = PLAYER1
    set_board[1, 0] = PLAYER2
    set_board[0, 1] = PLAYER1
    set_board[2, 0] = PLAYER2
    set_board[0, 2] = PLAYER1
    set_board[3, 0] = PLAYER2
    set_board[0, 5] = PLAYER1
    set_board[4, 0] = PLAYER2
    set_board[5, 0] = PLAYER2

    bitstring = board_to_bitstring(set_board)
    print()
    print(pretty_print_board(set_board))
    print()
    print(bitstring)

    apply_player_action_bitstring(bitstring, 0, PLAYER2)
    print(bitstring)

    re_board = bitstring_to_board(bitstring, 1) + bitstring_to_board(bitstring, 2)
    print(re_board)
    # bitstring to pretty print
    print(pretty_print_board(bitstring_to_board(bitstring, 1) + bitstring_to_board(bitstring, 2)))


def test_apply_player_action_bitstring_empty_board():
    set_board = initialize_game_state()

    bitstring = board_to_bitstring(set_board)
    print()
    print(pretty_print_board(set_board))
    print()
    print(bitstring)

    apply_player_action_bitstring(bitstring, 0, PLAYER1)
    for i in range(10):
        new_bitstring = apply_player_action_bitstring(bitstring, 0, PLAYER1)

    print(bitstring)

    re_board = bitstring_to_board(bitstring, 1) + bitstring_to_board(bitstring, 2)
    print(re_board)
    # bitstring to pretty print
    print(pretty_print_board(bitstring_to_board(bitstring, 1) + bitstring_to_board(bitstring, 2)))



def test_check_for_draw_bitstring():
    binary = ['1111110111111011111101111110111111011111101111110', '1111110111111011111101111110111111011111101111110']

    draw = check_for_draw_bitstring(binary)

    assert (draw == True)


def test_check_endstate_bitstring():
    binary = ['1111110111111011111101111110111111011111101111110', '1111110111111011111101111110111111011111101111110']
    print(check_end_state_bitstring(binary, PLAYER1))
