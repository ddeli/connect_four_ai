import numpy as np

from game_utils import BoardPiece, PlayerAction, SavedState, NO_PLAYER, GameState
from game_utils import apply_player_action, next_player, calculate_score, check_end_state
from typing import Optional

# Global counter variables for debugging and profiling

counter_moves = 0
counter_alpha_beta_cut = 0

# Function to call the minimax algorithm


def generate_move_minimax(
        board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState]) -> tuple[PlayerAction, SavedState]:
    """
    This Function calls the actual minimax algorithm by passing all needed parameter to the minimiax function

    :param board: representation of the current game state
    :param player: current player
    :param saved_state: optional parameter for next moves
    :return: action: the column of the calculated best next move
    :return: SaveState (Optional)
    """
    global counter_moves
    counter_moves = 0
    global counter_alpha_beta_cut
    counter_alpha_beta_cut = 0
    [score, action] = minimax(board, player, True, -10000, 10000, 6, saved_state)

    # Some console prints for debugging only

    # print("Final Score: ")
    # print(score)
    # print("Next Move on Column: ")
    # print(action)
    # print("Number of simulated rounds: ")
    # print(counter_moves)
    # print("Number of Alpha-Beta Cuts: ")
    # print(counter_alpha_beta_cut)
    return action, saved_state


# Global counter functions for debugging and profiling
def increment_counter_moves():
    global counter_moves
    counter_moves += 1


def increment_counter_alpha_beta_cut():
    global counter_alpha_beta_cut
    counter_alpha_beta_cut += 1


# Implementation of the minimax algorithm
def minimax(board: np.ndarray, player: BoardPiece, is_maximizing: bool, alpha: int, beta: int, depth: int,
            saved_state: Optional[SavedState]
            ) -> tuple[int, int]:
    """
    This is the actual implementation of the minimax algorithm based on the alph-beta pruning

    :param board: representation of the current game state as a np.ndarray
    :param player: current player
    :param is_maximizing:
    :param alpha: parameter for the Pruning mechanism which can only manipulated by player1
    :param beta: parameter for the Pruning mechanism which can only manipulated by player2
    :param depth: indicates how many rounds should be simulated with the algorithm
    :param saved_state: Optional Parameter
    :return score: the calculated score of the simulated move
    :return action: the calculated next move
    """
    # increment_counter_moves()
    best_move = 0

    for i in range(7):
        col = np.int8((i+3) % 7)  # shift first move 4th column to increase winning chances
        if board[5, col] == NO_PLAYER:

            new_board = np.copy(board)
            apply_player_action(new_board, col, player)
            game_state_check = check_end_state(new_board, player)

            if game_state_check != GameState.STILL_PLAYING:
                if game_state_check == GameState.IS_DRAW:
                    return 0, col
                if game_state_check == GameState.IS_WIN:
                    action = col
                    if is_maximizing:
                        score = calculate_score(new_board) * (
                                    depth + 1)  # Plus 1 to prevent the score to be 0 at depth 0
                    else:
                        score = calculate_score(new_board) * -1 * (depth + 1)
                    return score, action

            if depth == 0:
                action = col
                score = 0
                return score, action

            # Recursive calling of the minimax() function
            [score, action] = minimax(new_board, next_player(player), not is_maximizing, alpha, beta, depth - 1,
                                      saved_state)
            if is_maximizing:
                if score > alpha:
                    alpha = score
                    best_move = col
                    if alpha >= beta:
                        # increment_counter_alpha_beta_cut()
                        break
            else:
                if score < beta:
                    beta = score
                    best_move = col
                    if beta <= alpha:
                        # increment_counter_alpha_beta_cut()
                        break
    if is_maximizing:
        return alpha, best_move
    else:
        return beta, best_move
