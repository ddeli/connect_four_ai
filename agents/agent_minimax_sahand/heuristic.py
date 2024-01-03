import numpy as np

from game_utils import *
from agents.common_sahand import *
from typing import Optional, Callable
from typing import List, Tuple

def evaluate_board(board: np.ndarray, player: int) -> int:
    """
    Evaluate the overall score for the game board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    player : int
        The player for whom the scores are evaluated.

    Returns
    -------
    board_score: int
        The aggregated score for the game board.
    """
    all_pivots = get_pivots(board)
    all_pivot_scores_player, all_pivot_scores_opponent = evlaute_at_all_pivots(board,all_pivots,player)
    board_score = aggregate_scores(all_pivot_scores_player, all_pivot_scores_opponent)
    return board_score

def aggregate_scores(all_pivot_scores_player: List[int], all_pivot_scores_opponent: List[int]) -> int:
    """
    Aggregate scores based on player and opponent scores at all pivots.

    Parameters
    ----------
    all_pivot_scores_player : List[int]
        A list containing player scores at all specified pivots.
    all_pivot_scores_opponent : List[int]
        A list containing opponent scores at all specified pivots.

    Returns
    -------
    board_score: int
        The aggregated score for the game board.
    """
    threes_player = all_pivot_scores_player.count(3)
    twos_player = all_pivot_scores_player.count(2)
    threes_opponent = all_pivot_scores_opponent.count(-3)
    twos_opponent = all_pivot_scores_opponent.count(-2)

    if threes_player > 1 and threes_opponent <= 1: board_score = 500
    elif threes_player <= 1 and threes_opponent > 1: board_score = -500
    else: board_score = (threes_player - threes_opponent) * 15 + \
                        (twos_player - twos_opponent) * 10
        
    return board_score
    

def evlaute_at_all_pivots(board: np.ndarray, all_pivots: List[Tuple[int, int]], player: int) -> Tuple[List[int], List[int]]:
    """
    Evaluate scores for the player and opponent at all specified pivots on the game board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    all_pivots : List[Tuple[int, int]]
        A list of tuples representing pivot coordinates (row, column) in the board.
    player : int
        The player for whom the scores are evaluated.

    Returns
    -------
    all_pivot_scores_player: List[int]
        all scores for the agent's pieces one for each axes of each pivot point.
    all_pivot_scores_opponent: List[int]
        all scores for the opponent pieces one for each axes of each pivot point.
    """
    all_pivot_scores_player = []
    all_pivot_scores_opponent = []

    for pivot in all_pivots:
        pivot_score_player, pivot_score_opponent =  evaluate_at_pivot(board,pivot,player)      
        all_pivot_scores_player = all_pivot_scores_player + pivot_score_player
        all_pivot_scores_opponent = all_pivot_scores_opponent + pivot_score_opponent

    return all_pivot_scores_player, all_pivot_scores_opponent


def evaluate_at_pivot(board: np.ndarray, pivot: Tuple[int, int], player: int) -> Tuple[List[int], List[int]]:
    """
    Evaluate the scores for the player and opponent at the specified pivot on all axes.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.
    player : int
        The player for whom the scores are evaluated.

    Returns
    -------
    pivot_score_player: List[int]
        an array of length 4 for corresponding to evaluation for the agent's pieces at each axis.
    pivot_score_opponent: list[int]
        an array of length 4 for corresponding to evaluation for the agent's pieces at each axis.
    Tuple[List[int], List[int]]
    """
    row_score_player, row_score_opponent = evaluate_row(board,pivot,player)
    col_score_player, col_score_opponent = evaluate_col(board,pivot,player)
    diag_score_player, diag_score_opponent  = evaluate_diag(board,pivot,player)
    opp_diag_score_player, opp_diag_score_opponent  = evaluate_opp_diag(board,pivot,player)

    pivot_score_player = row_score_player + col_score_player + diag_score_player + opp_diag_score_player
    pivot_score_opponent = row_score_opponent +col_score_opponent + diag_score_opponent +opp_diag_score_opponent
    
    return pivot_score_player, pivot_score_opponent

def evaluate_row(board: np.ndarray, pivot_point: Tuple[int, int], player: int) -> Tuple[List[int], List[int]]:
    """
    Evaluates scores of the windows of length 4 containing the pivot and constituting the row containing the pivot.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot_point : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.
    player : int
        The maximizing player.

    Returns
    -------
    row_score_player: List[int]
        the maximum score that can be assigned to agent's pieces on the pivot row.

    row_score_opponent: List[int]
        the maximum score that can be assigned to players pieces on the pivot row.
    """
    array,position = get_pivot_row(board,pivot_point)
    windows_row = extract_windows(array,position)
    row_score_player = evaluate_windows_player(windows_row,player)
    row_score_opponent = evaluate_windows_opponent(windows_row,player)
    return row_score_player,row_score_opponent

def get_pivot_row(board: np.ndarray, pivot: Tuple[int, int]) -> Tuple[np.ndarray, int]:
    """
    Get the row window containing the pivot and position of the pivot in the window.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.

    Returns
    -------
    row_window: numpy.ndarray
        the row axes containing the pivot point.
    position: int
        the position of the pivot point on the return array.
    """
    row_window = board[pivot[0]]
    position = pivot[1]
    return row_window,position

def evaluate_col(board: np.ndarray, pivot_point: Tuple[int, int], player: int) -> Tuple[List[int], List[int]]:
    """
    Evaluates scores of the windows of length 4 containing the pivot and constituting the column containing the pivot.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot_point : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.
    player : int
        The maximizing player.

    Returns
    -------
    col_score_player: List[int]
        the maximum score that can be assigned to agent's pieces on the pivot column.

    col_score_opponent: List[int]
        the maximum score that can be assigned to players pieces on the pivot column.
    """
    array,position = get_pivot_col(board,pivot_point)
    windows_col = extract_windows(array,position)
    col_score_player = evaluate_windows_player(windows_col,player)
    col_score_opponent = evaluate_windows_opponent(windows_col,player)
    return col_score_player,col_score_opponent

def get_pivot_col(board: np.ndarray, pivot: Tuple[int, int]) -> Tuple[np.ndarray, int]:
    """
    Get the column window containing the poivot and position of the pivot in the window.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.

    Returns
    -------
    col_window: numpy.ndarray
        the column axes containing the pivot point.
    position: int
        the position of the pivot point on the return array.
    """
    col_window = board[:,pivot[1]]
    position = pivot[0]
    return col_window,position

def evaluate_diag(board: np.ndarray, pivot_point: Tuple[int, int], player: int) -> Tuple[List[int], List[int]]:
    """
    Evaluates scores of the windows of length 4 containing the pivot and constituting the diagonal containing the pivot.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot_point : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.
    player : int
        The maximizing player.

    Returns
    -------
    daig_score_player: List[int]
        the maximum score that can be assigned to agent's pieces on the pivot diagonal.

    diag_score_opponent: List[int]
        the maximum score that can be assigned to players pieces on the pivot diagonal.
    """
    array,position = get_pivot_diag(board,pivot_point)
    windows_diag = extract_windows(array,position)
    diag_score_player = evaluate_windows_player(windows_diag,player)
    diag_score_opponent = evaluate_windows_opponent(windows_diag,player)
    return diag_score_player,diag_score_opponent

def get_pivot_diag(board: np.ndarray, pivot: Tuple[int, int]) -> Tuple[np.ndarray, int]:
    """
    Get the diagonal window containing the pivot point and position of the pivot point on the window.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.

    Returns
    -------
    daig_window: numpy.ndarray
        the diagonal axes containing the pivot point.
    position: int
        the position of the pivot point on the return array.
    """
    diag_window = np.diag(board,pivot[1]-pivot[0])
    position = min(pivot)
    return diag_window,position

def evaluate_opp_diag(board: np.ndarray, pivot_point: Tuple[int, int], player: int) -> Tuple[List[int], List[int]]:
    """
    Evaluates scores of the windows of length 4 containing the pivot and constituting the opposite diagonal containing the pivot.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot_point : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.
    player : int
        The maximizing player.

    Returns
    -------
    opp_diag_score_player: List[int]
        the maximum score that can be assigned to agent's pieces on the pivot opposite diagonal.

    opp_diag_score_opponent: List[int]
        the maximum score that can be assigned to players pieces on the pivot opposite diagonal.
    """
    array,position = get_pivot_opp_diag(board,pivot_point)
    windows_opp_diag = extract_windows(array,position)
    opp_diag_score_player = evaluate_windows_player(windows_opp_diag,player)
    opp_diag_score_opponent = evaluate_windows_opponent(windows_opp_diag,player)
    return opp_diag_score_player,opp_diag_score_opponent

def get_pivot_opp_diag(board: np.ndarray, pivot: Tuple[int, int]) -> Tuple[np.ndarray, int]:
    """
    Get the opposite diagonal window containing the pivot point and position of the pivot point in the window.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    pivot : Tuple[int, int]
        A tuple representing the pivot coordinates (row, column) in the board.

    Returns
    -------
    opp_daig_window: numpy.ndarray
        the opposite diagonal axes containing the pivot point.
    position: int
        the position of the pivot point on the return array.
    """
    borad_flipped = np.fliplr(board)
    pivot = pivot[0],6-pivot[1]
    opp_daig_window = np.diag(borad_flipped,pivot[1]-pivot[0])
    position = min(pivot)
    return opp_daig_window,position


def extract_windows(array: list,pivot_position: int) -> list:
    """
    Extract sliding windows of length 4 from the given array around the pivot position.

    Parameters
    ----------
    array : List[int]
        A list of integers representing a sequence.
    pivot_position : int
        The position of the pivot around which windows are extracted.

    Returns
    -------
    windows: List[List[int]]
        A list containing windows of length 4 extracted from the array such that they all contain the pivot point.
    """
    start = max(0,pivot_position-3)
    last_window = len(array)-3
    end = min(pivot_position+1,last_window)
    windows = []
    for w in range(start,end):
        window = list(array[w:w+4])
        windows.append(window)
    return windows

def evaluate_windows_player(windows: List[List[int]], player: int) -> List[int]:
    """
    Evaluate the score of multiple windows for the player.

    Parameters
    ----------
    windows : List[List[int]]
        A list of windows, where each window is a list of pieces on the game board.
    player : int
        The player for whom the windows are evaluated.

    Returns
    -------
    direction_score: List[int]
        A list containing the maximum score among all evaluated windows for the specified player.
    """
    windows_score = [0]
    for window in windows:
        window_score = evaluate_single_window_player(window,player)
        windows_score = windows_score + window_score
    direction_score = [max(windows_score)]
    return direction_score

def evaluate_windows_opponent(windows: List[List[int]], player: int) -> List[int]:
    """
    Evaluate the score of multiple windows for the opponent player.

    Parameters
    ----------
    windows : List[List[int]]
        A list of windows, where each window is a list of pieces on the game board.
    player : int
        The opponent player for whom the windows are evaluated.

    Returns
    -------
    direction_score: List[int]
        A list containing the minimum score among all evaluated windows for the opponent player.
    """
    windows_score = [0]
    for window in windows:
        window_score = evaluate_single_window_opponent(window,player)
        windows_score = windows_score + window_score
    direction_score = [min(windows_score)]
    return direction_score

def evaluate_single_window_player(window: List[int], player: int) -> List[int]:
    """
    Evaluate the score of a single window for the player/agent.

    Parameters
    ----------
    window : List[int]
        A window of pieces on the game board.
    player : int
        The player for whom the window is evaluated.

    Returns
    -------
    window_score: List[int]
        A list containing the score of the window for the specified player.
    """
    window_score = [0]
    n_pieces = window.count(player)
    n_zeros = window.count(0)

    if n_pieces == 3: window_score = [3]
    elif n_pieces == 2 and n_zeros == 2: window_score = [2]
    return window_score

def evaluate_single_window_opponent(window: List[int], player: int) -> List[int]:
    """
    Evaluate the score of a single window for the opponent player.

    Parameters
    ----------
    window : List[int]
        A window of pieces on the game board.
    player : int
        The player for whom the window is evaluated.

    Returns
    -------
    window_score: List[int]
        A list containing the score of the window for the opponent player.
    """
    window_score = [0]
    n_pieces = window.count(player)
    n_zeros = window.count(0)

    if n_pieces == 0 and n_zeros == 1: window_score = [-3]
    elif n_pieces == 0 and n_zeros == 2: window_score = [-2]
    return window_score

def get_pivots(board: np.ndarray) -> List[Tuple[int, int]]:
    """
    Get the coordinates of all available pivot positions in the board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    all_pivots: List[Tuple[int, int]]
        A list of (row, column) tuples representing the coordinates of available pivot positions.
    """
    pivot_board = board.copy()

    max_height = get_max_height(pivot_board)

    max_heigh_pivot = pivot_board[:max_height+1,:]

    all_pivots = list(zip(*np.where(max_heigh_pivot == 0)))
    return all_pivots

def get_max_height(board: np.ndarray) -> int:
    """
    Get the maximum height among the free columns in the board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    max_height: int
        The maximum height among the free columns.
    """
    col_heights = [np.count_nonzero(board[:,i]) for i in range(BOARD_COLS)]
    col_heights = np.array(col_heights)
    is_open = is_open_row(board)
    free_col_heights = col_heights[is_open]
    max_height = max(free_col_heights)
    return max_height






    
    