# this file along with test_minimax_old_print.py in test_minimax_alg folder was used to do sanity
# checks by predicting and printing outcomes. 
import numpy as np

from game_utils import *
from agents.agent_minimax.heuristic import *
from typing import Optional, Callable

DEPTH = 3

def generate_move_minimax(board: np.ndarray, 
                         player: BoardPiece, 
                         saved_state: Optional[SavedState]) -> tuple[PlayerAction, Optional[SavedState]]:
    depth = DEPTH
    best_move = None
    max_score = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    valid_moves = get_valid_moves(board)

    for move in valid_moves:
        new_board = board.copy()
        new_board = apply_player_action(new_board, move, player)
        board_score = iterate_states(new_board,player, depth-1,alpha,beta, maximizing_player= False)
        if board_score > max_score:
            max_score = board_score
            best_move = move
        alpha = max(alpha,board_score)
        if beta <= alpha:
            break
    return best_move , max_score

def iterate_states(board,player, depth,alpha, beta, maximizing_player = True, i=np.array([0])):
    opponent = PLAYER2 if player == PLAYER1 else PLAYER1
    
    valid_moves = get_valid_moves(board)

    if depth == 0 or len(valid_moves) == 0: # depth =0 means there has been x=depth moves carried out
        board_score = evaluate(i)
        print(f'\ndepth 0 reached for {i}:',
              f'\nboard score is: {board_score}\n',
              pretty_print_board(board))
        i += 1
        return board_score


    if maximizing_player == True:
        max_score = float('-inf')
        for move in valid_moves:
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,player)
            board_score = iterate_states(new_board,player, depth-1,alpha,beta,False,i)
            max_score = max(max_score,board_score)
            alpha = max(alpha,board_score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = float('inf')
        for move in valid_moves:
            new_board = board.copy() # copy should be done inside the loop becasue ... don't move it out
            new_board = apply_player_action(new_board,move,opponent)
            board_score = iterate_states(new_board, player, depth-1,alpha,beta,True,i)
            min_score = min(min_score,board_score)
            beta = min(beta,board_score)
            if beta <= alpha:
                    break
        return min_score
    
    
def evaluate(i):
    score = [-1,3,5,-6,-4]
    if i == [0]:
        return score[i[0]]
    if i == [1]:
        return score[i[0]]
    if i == [2]:
        return score[i[0]]
    if i == [3]:
        return score[i[0]]
    if i == [4]:
        return score[i[0]]
    if i == [5]:
        return score[i[0]]
    if i == [6]:
        return score[i[0]]
    if i == [7]:
        return score[i[0]]

def get_valid_moves(board: np.ndarray):
    is_open = board[-1, :] == 0
    possible_moves = np.arange(BOARD_COLS)
    valid_moves = possible_moves[is_open]
    return valid_moves

def is_open_col(board):
    is_open = board[-1, :] == 0
    return is_open

def get_free_row(board):
    # remember to check for legal moves first.
    free_row = [np.count_nonzero(board[:,i]) for i in range(7)]
    return free_row