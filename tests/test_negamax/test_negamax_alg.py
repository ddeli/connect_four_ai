import numpy as np

from agents.agent_negamax.negamax import *

def test_negamax():
    board = np.array([1])

    alpha = float('-inf')
    beta = float('inf')

    depth = 3
    score = negamax(board, depth, alpha, beta, MaxPlayer)
    print('\nbest score is:', score)

def test_gen_move_negamax():
    board = np.array([1])

    move = gen_move_negamax(board,depth=3)
    print('\nBest move is:', move)

    iterative_deepening_move(board)

def test_get_pv():
    board = np.array([1])

    get_pv()
    print(pv)

def test_order_moves():
    moves = [0,1]
    pv[:] = [1,1]

    Nodes[0] = Node(0,depth=1)
    nodenumber[0] = 0
    moves = order_moves(moves)
    print(f'\nordered move:',moves)

def test_get_parent_move_sequence():

    Nodes[0] = Node(0,depth=3,parent=None,parent_move=None)
    Nodes[4] = Node(4,depth=2,parent=Nodes[0],parent_move=1)
    Nodes[6] = Node(6,depth=1,parent=Nodes[4],parent_move=4)
    Nodes[10] = Node(10,depth=0, parent=Nodes[6], parent_move=3)

    get_parent_move_sequence(Nodes[10])
    print(parent_sequence)

def test_simplescore():
    board = np.array([1])


    Nodes[0] = Node(0,depth=3,parent=None,parent_move=None)
    Nodes[4] = Node(4,depth=2,parent=Nodes[0],parent_move=1)
    Nodes[6] = Node(6,depth=1,parent=Nodes[4],parent_move=4)
    Nodes[10] = Node(10,depth=0, parent=Nodes[6], parent_move=3)
    nodenumber[0] = 10
    score = simplescore(board)
    print('\nsoce is:',score)

def test_iterative_deepening():
    board = []
    Node.skip_order = False
    Node.skip_null_window = False
    Node.skip_iterative_deepening = False

    iterative_deepening(board)

