import numpy as np

from agents.agent_minimax.heuristic import *

def test_evaluate_board():
    '''
    notes for later improvement:
    1- this board is an example that shows the benefit of evaluating each axis separately and returning
    acores of each pivot in four arrays of length four.
    this helps to check for example that X can reach a tow-way-win by placing a piece on (3,4).
    although I have not implement this scenario in score aggregate function (due to lack of time),
    it shows the reason why the evalutation algorithem is designed this way.
    2- another point is, although player O doesn't have an immediate two-way-win state, the agent
    avoids this board becasue O has two connected threes on the board. this should be improved by checking
    the immediate pivots first and weight them differently. (not done yet due to time limit)
    summary: it is rational to weight the X position better than O. but the agent doesn't due to design of
    evalutation algorithem. However, the algorithem is working as expected.
    '''
    board_string = ''' 
     - - - - - - - 
    |X            |
    |X O          |
    |O X O O      |
    |X O X O      |
    |O X O X X    |
    |X O X X X X  |
     - - - - - - -
     0 1 2 3 4 5 6
    '''
    board = string_to_board(board_string)
    print('\n',board)
    
    player = PLAYER1

    board_score = evaluate_board(board,player)
    print('board score:',board_score)

    assert board_score == -500

