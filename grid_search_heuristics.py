from typing import Callable
from game_utils import GenMove
import numpy as np


def agent_vs_agent(
    generate_move_1: GenMove,
    generate_move_2: GenMove,
    player_1: str = "Player 1",
    player_2: str = "Player 2",
    args_1: tuple = (),
    args_2: tuple = (),
    init_1: Callable = lambda board, player: None,
    init_2: Callable = lambda board, player: None,
):
    import time
    from game_utils import PLAYER1, PLAYER2, PLAYER1_PRINT, PLAYER2_PRINT, GameState, MoveStatus
    from game_utils import initialize_game_state, pretty_print_board, apply_player_action, check_end_state, check_move_status

    players = (PLAYER1, PLAYER2)
    for play_first in (1, -1):
        for init, player in zip((init_1, init_2)[::play_first], players):
            init(initialize_game_state(), player)

        saved_state = {PLAYER1: None, PLAYER2: None}
        board = initialize_game_state()
        gen_moves = (generate_move_1, generate_move_2)[::play_first]
        player_names = (player_1, player_2)[::play_first]
        gen_args = (args_1, args_2)[::play_first]

        playing = True
        while playing:
            for player, player_name, gen_move, args in zip(
                players, player_names, gen_moves, gen_args,
            ):
                t0 = time.time()
                print(pretty_print_board(board))
                print(
                    f'{player_name} you are playing with {PLAYER1_PRINT if player == PLAYER1 else PLAYER2_PRINT}'
                )
                action, saved_state[player] = gen_move(
                    board.copy(),  # copy board to be safe, even though agents shouldn't modify it
                    player, saved_state[player], *args
                )
                print(f'Move time: {time.time() - t0:.3f}s')

                move_status = check_move_status(board, action)
                if move_status != MoveStatus.IS_VALID:
                    print(f'Move {action} is invalid: {move_status.value}')
                    print(f'{player_name} lost by making an illegal move.')
                    playing = False
                    return player, 0
                    #break

                apply_player_action(board, action, player)
                end_state = check_end_state(board, player)

                if end_state != GameState.STILL_PLAYING:
                    print(pretty_print_board(board))
                    if end_state == GameState.IS_DRAW:
                        print('Game ended in draw')
                        return player, 1
                    elif end_state == GameState.IS_WIN:
                        print(
                            f'{player_name} won playing {PLAYER1_PRINT if player == PLAYER1 else PLAYER2_PRINT}'
                        )
                        playing = False
                        return player, 2
                    else: 
                        playing = False
                        return player, 0


if __name__ == "__main__":
   
    from functools import partial
  
    from agents.agent_negamax.negamax_bitstring_heuristics import iterative_deepening_bitstring
    connected_three_pieces=[2, 8, 0]
    connected_two_pieces=[1, 1, 0]
 
    players=['Player_heuristic_21', 'Player_heuristic_81', 'Player_noheuristic_00'] # heuristic_# means that the three piece score is #
    game_score={}
    for i in range(3):
        game_score[players[i]]=[]
    
    for i in range(3):
        iterator=[x for x in range(3) if x != i]
        for j in iterator:
            partial_agent_move1=partial(iterative_deepening_bitstring,three_piece=connected_three_pieces[i], two_piece=connected_two_pieces[i],method='pv')
            partial_agent_move2=partial(iterative_deepening_bitstring,three_piece=connected_three_pieces[j], two_piece=connected_two_pieces[j],method='pv')
        #(board, PLAYER1,threepiece_score=connected_three_pieces[i], twopiece_score=connected_two_pieces[i])
        #(board,PLAYER2,threepiece_score=connected_three_pieces[j], twopiece_score=connected_two_pieces[j])
            output=agent_vs_agent(generate_move_1=partial_agent_move1,generate_move_2=partial_agent_move2 ) 
            if output[0]==1: 
                game_score[players[i]].append(output[1])

                if output[1]==1:
                    game_score[players[j]].append(1)
                else:
                    game_score[players[j]].append(0)
            else:
                game_score[players[j]].append(output[1])
                if output[1]==1:
                    game_score[players[i]].append(1)
                else:
                    game_score[players[i]].append(0)
    print(game_score)
    np.save('connect_four_ai\results\game_score_heuristics.npy', game_score)
        