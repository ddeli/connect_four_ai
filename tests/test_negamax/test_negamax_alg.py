import numpy as np

from agents.agent_negamax.negamax import *
from game_utils_sahand import PLAYER1, PLAYER2, string_to_board

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
    Node.pv[:] = [1,3]
    Node.principle_move_taken = 0

    moves = [0,1,2,3]
    print('\navaialbel moves:', moves)
    moves = order_moves(moves)
    print(f'ordered move:',moves)

    moves = [0,1,2,3]
    print('\navaialbel moves:', moves)
    moves = order_moves(moves)
    print(f'ordered move:',moves)

    moves = [0,1,2,3]
    print('\navaialbel moves:', moves)
    moves = order_moves(moves)
    print(f'ordered move:',moves)

    moves = [0,1,2,3]
    print('\navaialbel moves:', moves)
    moves = order_moves(moves)
    print(f'ordered move:',moves)

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
    board = [[],[]]
    Node.skip_order = False
    Node.skip_null_window = False
    Node.skip_iterative_deepening = False

    iterative_deepening(board, agent_piece=PLAYER1)

def test_get_valid_moves():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    valid_moves = get_valid_moves(board)
    print(valid_moves)
    assert np.all(valid_moves == [1,2,4,6])

def test_iterative_deepening_numpy_board():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |             |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)
    Node.skip_order = True
    Node.skip_null_window = True
    Node.skip_iterative_deepening = False

    iterative_deepening(board, agent_piece=PLAYER1)

def test_check_temrminal():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |  O O O O    |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)

    set_players_pieces(agent_piece=PLAYER2)
    playerview = MinView
    terminal, terminal_score = check_terminal(board,playerview)
    print(f'terminal: {terminal} and terminal_score: {terminal_score}')

def test_set_players_pieces():
    agent_piece = PLAYER2
    set_players_pieces(agent_piece)
    print('agent_piece:', Node.agent_piece)
    print('opponent_piece:', Node.opponent_piece)

def test_get_player_piece():
    agent_piece = PLAYER2
    set_players_pieces(agent_piece)
    playerview = -1
    player_piece = get_player_piece(playerview)
    print('player piece:', player_piece)

def test_all_in_place():
    board_string = ''' 
     - - - - - - - 
    |             |
    |             |
    |             |
    |             |
    |             |
    |    X X X    |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)
    Node.skip_order = False
    Node.skip_null_window = False
    Node.skip_iterative_deepening = False

    iterative_deepening(board, agent_piece=PLAYER1)




