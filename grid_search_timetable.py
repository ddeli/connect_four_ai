from typing import Callable
from game_utils import GenMove
import numpy as np
#from connect_four_ai.grid_search_heuristics import agent_vs_agent


def agent_vs_agent_timing(
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
        timetable={}
        timetable[PLAYER1]=[]
        timetable[PLAYER2]=[]
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
                timetable[player].append(time.time()-t0)
                move_status = check_move_status(board, action)
                if move_status != MoveStatus.IS_VALID:
                    print(f'Move {action} is invalid: {move_status.value}')
                    print(f'{player_name} lost by making an illegal move.')
                    playing = False
                    return timetable
                    #break

                apply_player_action(board, action, player)
                end_state = check_end_state(board, player)

                if end_state != GameState.STILL_PLAYING:
                    print(pretty_print_board(board))
                    if end_state == GameState.IS_DRAW:
                        print('Game ended in draw')
                        return timetable
                    elif end_state == GameState.IS_WIN:
                        print(
                            f'{player_name} won playing {PLAYER1_PRINT if player == PLAYER1 else PLAYER2_PRINT}'
                        )
                        playing = False
                        return timetable
                    else: 
                        playing = False
                        return timetable


if __name__ == "__main__":
   
    from functools import partial
  
    from agents.agent_negamax.negamax_bitstring_heuristics import iterative_deepening_bitstring
    
 
    methods=["pv", "ltr", "random", "middle"]    
    game_score={}
    k=0
    game_players={}
    
    for i in range(4):
        iterator=[x for x in range(4) if x != i]
        for j in iterator:
            print(f'game_{k} = {methods[i], methods[j]}')
            game_players[f'game{k}']=[methods[i], methods[j]]

            partial_agent_move1=partial(iterative_deepening_bitstring, three_piece=8, two_piece=1, method=methods[i])
            partial_agent_move2=partial(iterative_deepening_bitstring, three_piece=8, two_piece=1, method=methods[j])
            output=agent_vs_agent_timing(generate_move_1=partial_agent_move1,generate_move_2=partial_agent_move2 ) 
            game_score[f'game{k}']=output
            k+=1
        print(f'game_{k} = {methods[i], methods[j]}')
    print(game_players)  
    np.save(r'connect_four_ai\results\game_players_move_ordering_timetable.npy', game_players)
    print(game_score)
    np.save(r'connect_four_ai\results\game_score_move_ordering_timetable.npy', game_score)
        
# if __name__ == "__main__":
 
#     from functools import partial
   
#     from agents.agent_negamax.negamax_bitstring_heuristics import iterative_deepening_bitstring
    
#     methods=["pv", "ltr", "random", "middle"]
#     game_score={}
#     for i in range(4):
#         game_score[methods[i]]=[]
    
#     for i in range(4):
#         iterator=[x for x in range(4) if x != i]
#         for j in iterator:
#             partial_agent_move1=partial(iterative_deepening_bitstring, method=methods[i])
#             partial_agent_move2=partial(iterative_deepening_bitstring,method=methods[j])
       
#             output=agent_vs_agent(generate_move_1=partial_agent_move1,generate_move_2=partial_agent_move2 ) 
#             if output[0]==1: 
#                 game_score[methods[i]].append(output[1])

#                 if output[1]==1:
#                     game_score[methods[j]].append(1)
#                 else:
#                     game_score[methods[j]].append(0)
#             else:
#                 game_score[methods[j]].append(output[1])
#                 if output[1]==1:
#                     game_score[methods[i]].append(1)
#                 else:
#                     game_score[methods[i]].append(0)
#     print(game_score)
#     np.save('game_score_move_ordering.npy', game_score)
        