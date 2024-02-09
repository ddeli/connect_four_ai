import numpy as np
import random
import copy

from game_utils import PLAYER1, PLAYER2, BoardPiece, GameState, BOARD_COLS
from game_utils import pretty_print_board, check_end_state, apply_player_action
from typing import Optional, Callable
from bitstring import board_to_bitstring, apply_player_action_bitstring, \
    calculate_score_bitstring, bitstring_to_board, check_end_state_bitstring, \
    copy_bitstring_array, get_valid_moves_bitstring
from agents.agent_negamax.heuristic_bitboard import evaluate_board



PlayerView = np.int8
MaxView = PlayerView(1)
MinView = PlayerView(-1)

MaxDepth = 6

class Node():
    agent_piece = None
    opponent_piece = None

    instances = {}
    nodenumber = 0
    hitcount = -1
    pv = []
    principle_move_taken = 0

    skip_order = False
    skip_null_window = False
    skip_iterative_deepening = False

    def __init__(self, nodenumber, board, depth=None, parent=None, parent_move=None, best_score=None, best_move=None, best_child=None, leaf_score=None):
        self.nodenumber = nodenumber
        self.board = board
        self.depth = depth
        self.parent = parent
        self.parent_move = parent_move
        self.best_move = best_move
        self.best_child = best_child
        self.best_score = best_score
        self.leaf_score = leaf_score
        Node.instances[nodenumber] = self
    
    def print_node(self):
        parent = None if self.parent is None else self.parent
        parent_move = None if self.parent_move is None else self.parent_move
        child = None if self.best_child is None else self.best_child
        print(f'''
nodenumber: {self.nodenumber}
board:
{self.board}
depth: {self.depth}
parent: {parent}
parent_move: {parent_move}
best move: {self.best_move}
best child: {child}
best score: {self.best_score}
leaf score: {self.leaf_score}
    ''') 

    @classmethod
    def reset(cls):
        cls.instances = {}
        cls.nodenumber = 0
        cls.principle_move_taken = 0
        cls.hitcount = -1
    
    @classmethod
    def print_class(cls):
        for item in cls.instances: cls.instances[item].print_node()


def iterative_deepening_bitstring(board, agent_piece: BoardPiece,  saved_state = None, maxdepth:int = MaxDepth, three_piece=2, two_piece=1, method="pv"):
    set_players_pieces(agent_piece)
    parent_board = board_to_bitstring(board)
    # parent_board = copy.deepcopy(board)
    mindepth = maxdepth if Node.skip_iterative_deepening else 1
    for depth in range(mindepth, maxdepth+1):
        Node.reset()
        #print(f'\n***start analysing depth: {depth} ***')
        Node(Node.nodenumber, parent_board, depth)
        negamax(parent_board, depth, three_piece=three_piece, two_piece=two_piece,method=method)
        Node.pv = []
        get_pv()
        if depth == maxdepth:
            best_move = Node.pv[0]
            Node.pv = []
            #print(f'best move is *** {best_move} ***')
            return best_move, Node.instances 


def set_players_pieces(agent_piece:BoardPiece):
    """
    Set the agent's and opponent's pieces in the class based on the given agent's piece.

    Parameters:
        agent_piece (BoardPiece): The piece for the agent.

    Returns:
        None
    """
    Node.agent_piece = agent_piece
    Node.opponent_piece = PLAYER2 if agent_piece == PLAYER1 else PLAYER1


def check_terminal(board:list[str,str], playerview:PlayerView) -> tuple[bool,int]:
    """
    Check if the current board state is a terminal state and calculate the terminal score.

    Parameters:
        board (list[str,str]): The game board.
        playerview (PlayerView): The player's view for whom the terminal check is being performed.

    Returns:
        Tuple[bool, int]: A tuple containing a boolean indicating whether the state is terminal and the terminal score.
    """
    # note that playerview is one move ahead of the last player.
    # minimizer checks the result for maximizer's last move and vice versa.
    lastpiece = Node.agent_piece if playerview == MinView else Node.opponent_piece
    terminal = False
    terminal_score = None
    lastmove_result = check_end_state_bitstring(board, lastpiece)
    # from the minimizer's point of view, maximizer's win is alway -1000.
    # the same is true for maximizer's point of view.
    if lastmove_result == GameState.IS_WIN:
        terminal, terminal_score = True, -1000
    elif lastmove_result == GameState.IS_DRAW:
        terminal, terminal_score = True, 0
    return terminal, terminal_score


def get_player_piece(playerview:PlayerView)->BoardPiece:
    """
    Get the player's piece based on the given player view.

    Parameters:
        playerview (PlayerView): The player's view (1 for agent, 2 for opponent).

    Returns:
        playerpiece (BoardPiece): The piece associated with the player (agent or opponent).
    """
    player_piece = Node.agent_piece if playerview == 1 else Node.opponent_piece
    return player_piece


def negamax(parent_board, depth: int, alpha: float = float('-inf'), beta: float = float('inf'), playerview: PlayerView = MaxView, three_piece=2, two_piece=1, method="pv"):
    Node.hitcount += 1

    terminal, terminal_score = check_terminal(parent_board, playerview)
    if terminal:
        return -terminal_score, Node.nodenumber
    elif depth == 0:  
        leaf_score = evaluate_board(parent_board, Node.agent_piece, threepiece_score=three_piece, twopiece_score=two_piece)*playerview
        Node.instances[Node.nodenumber].leaf_score = leaf_score
        return -leaf_score, Node.nodenumber
    
    best_score = float('-inf')

    best_move = None
    moves = get_valid_moves_bitstring(parent_board)
    moves = order_moves(moves, method)
    current_nodenumber = Node.nodenumber
    first_move = True
    for move in moves:
        child_board = copy_bitstring_array(parent_board)
        # child_board = copy.deepcopy(parent_board)
        player_piece = get_player_piece(playerview)
        apply_player_action_bitstring(child_board, move, player_piece)
        Node.nodenumber += 1
        Node(Node.nodenumber, child_board, depth-1, parent=current_nodenumber, parent_move=move)

        if first_move or Node.skip_null_window:
            board_score, child_nodenumber = negamax(child_board, depth-1, -beta, -alpha, -playerview, three_piece=three_piece, two_piece=two_piece, method=method)
        else:
            mark_nodenumber = Node.nodenumber
            board_score, child_nodenumber = negamax(child_board, depth-1, -(alpha+1), -alpha, -playerview, three_piece=three_piece, two_piece=two_piece, method=method)
            if alpha < board_score < beta:
                Node.nodenumber = mark_nodenumber
                board_score, child_nodenumber = negamax(child_board, depth-1, -beta, -alpha, -playerview, three_piece=three_piece, two_piece=two_piece, method=method)

        best_score, best_move = update_bestscore_bestmove(board_score, best_score, move, best_move, current_nodenumber, child_nodenumber)
        prune, alpha, beta = check_prune(board_score, alpha, beta)
        if prune: break
        first_move = False

    return -best_score, current_nodenumber

def update_bestscore_bestmove(board_score:int, best_score:int, move:int, best_move:int, current_nodenumber:int, child_node_number:int)-> tuple[int,int]:
    """
    Update the best score and best move based on the given board score, move, and node numbers.

    Parameters:
        board_score (int): The score of the current board state.
        best_score (int): The current best score.
        move (int): The move associated with the current board state.
        best_move (int): The current best move.
        current_nodenumber (int): The node number of the current board state.
        child_node_number (int): The node number of the child board state.

    Returns:
        Tuple[int, int]: A tuple containing the updated best score and best move.
    """   
    if board_score > best_score:
        best_score = board_score
        best_move = move
        Node.instances[current_nodenumber].best_score = best_score
        Node.instances[current_nodenumber].best_move = best_move
        Node.instances[current_nodenumber].best_child = child_node_number
    return best_score, best_move

def check_prune(board_score:int, alpha:float, beta:float) -> tuple[bool, float, float]:
    """
    Check if pruning is possible based on the given board score, alpha, and beta.

    Parameters:
        board_score (int): The score of the current board state.
        alpha (float): The current alpha value in alpha-beta pruning.
        beta (float): The current beta value in alpha-beta pruning.

    Returns:
        Tuple[bool, float, float]: A tuple containing a boolean indicating whether pruning is possible,
                                   the updated alpha value, and the unchanged beta value.
    """
    prune = False
    alpha = max(alpha,board_score)
    if alpha >= beta: prune = True
    return prune, alpha, beta

def get_pv(nodenumber:int=0):
    """
    Recursively retrieves the principle variation (pv) from a series of recorded nodes. records the principle variation in Node.pv

    Parameters:
        nodenumber (int): The node number to start retrieving the pv from.

    Returns:
        None
    """
    node = Node.instances[nodenumber]
    best_move = node.best_move
    if best_move == None: return
    Node.pv.append(best_move)
    best_child_nodenumber = node.best_child
    get_pv(best_child_nodenumber)

def order_moves(moves: list[int], method: str = "pv"):
    """
    Orders the moves based on the specified method.

    Parameters:
    - moves (List[int]): List of moves to be ordered.
    - method (str, optional): Ordering method. Possible methods are "pv" (principle variation), "ltd"(left to right), "random" and "middle"

    Returns:
    List[int]: Ordered list of moves.
    """
    if Node.skip_order: return moves
    if method == "ltr":
        return moves
    elif method == "random":
        random.shuffle(moves)
        return moves

    elif method == "middle":
        default_ordering = [3, 2, 4, 1, 5, 0, 6]
        moves = [move for move in default_ordering if move in moves]
        return moves
    else:
        pv_length = len(Node.pv)
        if Node.principle_move_taken == pv_length:  return order_moves(moves,'middle')

        best_move = Node.pv[Node.principle_move_taken]
        if best_move in moves:
            moves.remove(best_move) 
            moves = [best_move] + moves

            Node.principle_move_taken += 1
            return moves
        else:
            Node.principle_move_taken = pv_length
            return order_moves(moves,'middle')
