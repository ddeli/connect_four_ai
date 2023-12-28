import numpy as np
import random

from game_utils import BoardPiece, PlayerAction, SavedState, NO_PLAYER
from typing import Optional


def generate_move_random(
    board: np.ndarray, player: BoardPiece, saved_state: Optional[SavedState]
) -> tuple[PlayerAction, Optional[SavedState]]:
    """
    A function to randomly valid a valid move

    :param board: current game state as ndarray representation
    :param player: current player
    :param saved_state: optional parameter
    :return: next random move, saved_state
    """
    # Check for valid moves and save them in an array
    valid_moves = []
    for i in range(7):
        if board[5, i] == NO_PLAYER:
            valid_moves.append(i)

    # Generate Randon Column in bounds
    ran_index = random.randint(0, len(valid_moves)-1)
    action = valid_moves[ran_index]

    return action, saved_state