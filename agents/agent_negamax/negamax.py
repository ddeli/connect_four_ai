import numpy as np

from typing import Optional, Callable

PlayerView = np.int8
MaxView = PlayerView(1)
MinView = PlayerView(-1)

MaxDepth = 3


class Node():
    instances = {}
    nodenumber = 0
    hitcount = -1
    pv = []
    principle_move_taken = 0

    skip_order = False
    skip_null_window = False
    skip_iterative_deepening = False

    def __init__(self, nodenumber, board=[], depth=None, parent=None, parent_move=None, best_score=None, best_move=None, best_child=None, leaf_score=None):
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

def iterative_deepening(board, maxdepth:int = MaxDepth):
    mindepth = maxdepth if Node.skip_iterative_deepening else 1
    for depth in range(mindepth,maxdepth+1):
        print(f'\n***start analysing depth: {depth} ***')
        Node(Node.nodenumber,board, depth)
        negamax(board,depth)
        Node.pv = []
        get_pv()
        Node.reset()

def negamax(parent_board, depth:int, alpha:float = float('-inf'), beta:float = float('inf'), playerview:PlayerView = MaxView):
    Node.hitcount += 1
    if depth == 0:  
        leaf_score = simplescore(parent_board)*playerview
        Node.instances[Node.nodenumber].leaf_score = leaf_score
        return -leaf_score, Node.nodenumber
    
    best_score = float('-inf')

    best_move = None
    moves = get_valid_moves_bitstring()
    moves = order_moves(moves)
    current_nodenumber = Node.nodenumber
    first_move = True
    for move in moves:
        child_board = parent_board.copy()
        child_board = apply_move(child_board,move)
        Node.nodenumber += 1
        Node(Node.nodenumber, child_board, depth-1, parent=current_nodenumber, parent_move=move)

        if first_move or Node.skip_null_window:
            board_score, child_nodenumber = negamax(child_board,depth-1,-beta, -alpha, -playerview)
        else:
            mark_nodenumber = Node.nodenumber
            board_score, child_nodenumber = negamax(child_board,depth-1,-(alpha+1), -alpha, -playerview)
            if alpha < board_score < beta:
                Node.nodenumber = mark_nodenumber
                board_score, child_nodenumber = negamax(child_board,depth-1,-beta, -alpha, -playerview)

        best_score, best_move = update_bestscore_bestmove(board_score, best_score, move, best_move, current_nodenumber, child_nodenumber)
        prune, alpha, beta = check_prune(board_score, alpha, beta)
        if prune: break
        first_move = False

    return -best_score, current_nodenumber

def update_bestscore_bestmove(board_score:int, best_score:int, move:int, best_move, current_nodenumber:int, child_node_number:int)-> tuple[int,int,list]:    
    if board_score > best_score:
        best_score = board_score
        best_move = move
        Node.instances[current_nodenumber].best_score = best_score
        Node.instances[current_nodenumber].best_move = best_move
        Node.instances[current_nodenumber].best_child = child_node_number
    return best_score, best_move

def check_prune(board_score:int, alpha:float, beta:float):
    prune = False
    alpha = max(alpha,board_score)
    if alpha >= beta: prune = True
    return prune, alpha, beta

def get_pv(nodenumber=0):
    node = Node.instances[nodenumber]
    best_move = node.best_move
    if best_move == None: return
    Node.pv.append(best_move)
    best_child_nodenumber = node.best_child
    get_pv(best_child_nodenumber)

def order_moves(moves):
    if Node.skip_order: return moves
    pv_len = len(Node.pv)
    if Node.principle_move_taken == pv_len: return moves
    current_depth = Node.instances[Node.nodenumber].depth
    best_move_pvindex = pv_len - (current_depth-1)
    if pv_len-1 < best_move_pvindex: return moves
    best_move = Node.pv[best_move_pvindex]
    moves.remove(best_move)
    moves = [best_move] + moves
    Node.principle_move_taken += 1
    return moves

def simplescore(board):
    leaf_nodenumber = Node.nodenumber
    parent_sequence = []
    parent_sequence = get_parent_move_sequence(leaf_nodenumber, parent_sequence)

    if parent_sequence == []: score = 0
    if parent_sequence == [0]: score = 2
    if parent_sequence == [1]: score = 4
    if parent_sequence == [0,0]: score = 90
    if parent_sequence == [0,1]: score = 40
    if parent_sequence == [1,0]: score = 80
    if parent_sequence == [1,1]: score = 60
    if parent_sequence == [0,0,0]: score = 700
    if parent_sequence == [0,0,1]: score = 500
    if parent_sequence == [0,1,0]: score = 300
    if parent_sequence == [0,1,1]: score = 100
    if parent_sequence == [1,0,0]: score = 800
    if parent_sequence == [1,0,1]: score = 600
    if parent_sequence == [1,1,0]: score = 400
    if parent_sequence == [1,1,1]: score = 200
    print(f'leaf node reached; sequence:{parent_sequence}; score:{score}')
    return score

def get_parent_move_sequence(nodenumber,parent_sequence):
    node = Node.instances[nodenumber]
    if node.parent is None: 
        parent_sequence = parent_sequence[::-1]
        return parent_sequence
    parent_move = node.parent_move
    parent_sequence.append(parent_move)
    return get_parent_move_sequence(node.parent, parent_sequence)

def apply_move(board,move):
    board.append(move)
    return board

def get_valid_moves_bitstring():
    moves = [0,1]
    return moves

