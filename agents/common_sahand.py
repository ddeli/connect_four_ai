import numpy as np
from typing import Optional, Callable
from typing import List, Tuple

def is_open_row(board: np.ndarray) -> bool:
    """
    Check if the last row of the board is open (does not contain any non-zero elements).

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    is_open: bool
        True if the last row is open, False otherwise.
    """
    is_open = board[-1, :] == 0
    return is_open