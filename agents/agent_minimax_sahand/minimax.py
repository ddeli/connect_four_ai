 
import numpy as np

from game_utils import *
from agents.agent_minimax.heuristic import *
from agents.common import *
from typing import Optional, Callable

DEPTH = 4

def generate_move_minimax(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    """
    Generate the best move using the minimax algorithm.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    player : BoardPiece
        the BoardPiece that the agent is playing with.
    saved_state : Optional[SavedState]
        An optional saved state.

    Returns
    -------
    best_move: PlayerAction
        the action that agent will take.
    saved_state: Optional[SavedState]

    """
    depth = DEPTH
    best_move = None
    max_score = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    valid_moves = get_valid_moves(board)

    for move in valid_moves:
        new_board = board.copy()
        new_board = apply_player_action(new_board, move, player)
        board_score = minimax(new_board,player, depth-1,alpha,beta, maximizing_player= False)
        if board_score > max_score:
            max_score = board_score
            best_move = move
        alpha = max(alpha,board_score)
        if beta <= alpha:
            break
    return best_move, saved_state

def minimax(
    board: np.ndarray, 
    player: int, 
    depth: int, 
    alpha: float, 
    beta: float, 
    maximizing_player: bool = True
) -> float:
    """
    Recursive function to evaluate possible states in the minimax algorithm.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.
    player : int
        Specifies agent's piece
    depth : int
        The remaining depth for recursive evaluation.
    alpha : float
        Alpha value for alpha-beta pruning.
    beta : float
        Beta value for alpha-beta pruning.
    maximizing_player : bool, optional
        Indicates whether the current player is maximizing or minimizing.

    Returns
    -------
    board_score: float
        The score for the current state.
    """
    opponent = PLAYER2 if player == PLAYER1 else PLAYER1

    player_state = check_end_state(board,player)
    opponent_state = check_end_state(board,opponent)

    if player_state == GameState.IS_WIN: return 1000
    elif opponent_state == GameState.IS_WIN: return -1000
    elif player_state == GameState.IS_DRAW: return 0
    elif depth == 0: # depth =0 means there has been x=depth moves carried out
        board_score = evaluate_board(board,player)
        return board_score

    valid_moves = get_valid_moves(board)

    if maximizing_player == True:
        max_score = float('-inf')
        for move in valid_moves:
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,player)
            board_score = minimax(new_board,player, depth-1,alpha,beta,False)
            max_score = max(max_score,board_score)
            alpha = max(alpha,board_score)
            alpha, beta, prune = check_prune(board_score, alpha, beta, maximizing_player)
            if prune: break
        return max_score
    else:
        min_score = float('inf')
        for move in valid_moves:
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,opponent)
            board_score = minimax(new_board, player, depth-1,alpha,beta,True)
            min_score = min(min_score,board_score)
            alpha, beta, prune = check_prune(board_score, alpha, beta, maximizing_player)
            if prune: break
        return min_score

def check_prune(board_score: int, alpha: int, beta: int, maximizing_player: bool) -> Tuple[int, int, bool]:
    """
    Check if pruning is possible based on the current board score, alpha, beta, and the maximizing player.

    Parameters
    ----------
    board_score : int
        The score of the game board.
    alpha : int
        The alpha value for alpha-beta pruning.(the best alternative for miximizer)
    beta : int
        The beta value for alpha-beta pruning.
    maximizing_player : bool
        Indicates whether the current player is maximizing or minimizing. (the best alternative for minimizer)

    Returns
    -------
    alpha: int
        updated value of the alpha
    
    beta: int
        updated value of the beta
    prune: bool
    Tuple[int, int, bool]
        a boolean indicating whether pruning is possible.
    """
    prune = False
    if maximizing_player:
        alpha = max(alpha,board_score)
    else:
        beta = min(beta,board_score)
    
    if beta <= alpha: prune = True
    return alpha, beta, prune     

def get_valid_moves(board: np.ndarray) -> List[int]:
    """
    Get valid moves for the current state of the game board.

    Parameters
    ----------
    board : numpy.ndarray
        2D array representing the game board.

    Returns
    -------
    valid_moves: List[int]
        A list of valid moves represented by column indices.
    """
    is_open = board[-1, :] == 0
    possible_moves = np.arange(BOARD_COLS)
    valid_moves = possible_moves[is_open]
    return valid_moves