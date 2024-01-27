from typing import Callable

from agents.agent_minimax.minimax_bitstring import generate_move_minimax_bitstring
from game_utils import GenMove
from agents.agent_human_user import user_move
# from agents.agent_random import generate_move_random
# from agents.agent_minimax import generate_move_minimax
# from agents.agent_negamax import negamax_move
from agents.agent_negamax.negamax_bitstring_el import negamax_move_bitstring


def agent_vs_agent(
    generate_move_1: GenMove,
    generate_move_2: GenMove = user_move,
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
                
                action, saved_state[player] = gen_move(
                    board.copy(),  # copy board to be safe, even though agents shouldn't modify it
                    player, saved_state[player], *args
                )

                move_status = check_move_status(board, action)
                if move_status != MoveStatus.IS_VALID:
                    print(f'Move {action} is invalid: {move_status.value}')
                    print(f'{player_name} lost by making an illegal move.')
                    return 0

                apply_player_action(board, action, player)
                end_state = check_end_state(board, player)

                if end_state != GameState.STILL_PLAYING:
                    if end_state == GameState.IS_DRAW:
                        print('Game ended in draw')
                        return 1
                    else: 
                        print(
                            f'{player_name} won playing {PLAYER1_PRINT if player == PLAYER1 else PLAYER2_PRINT}'
                        )
                        if end_state==GameState.IS_WIN:
                            return 2
                        else:
                            return 0
                        
                    


# if __name__ == "__main__":
#     # human_vs_agent(user_move)
#     # human_vs_agent(generate_move_random)
#     # human_vs_agent(generate_move_minimax)
#     # human_vs_agent(generate_move_minimax_bitstring)
#     # human_vs_agent(negamax_move)
#     human_vs_agent(negamax_move_bitstring)
