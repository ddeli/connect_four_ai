from typing import Callable
from game_utils import GenMove
import numpy as np
from connect_four_ai.grid_search_heuristics import agent_vs_agent


        
if __name__ == "__main__":
 
    from functools import partial
   
    from agents.agent_negamax.negamax_bitstring_heuristics import iterative_deepening_bitstring
    
    methods=["pv", "ltr", "random", "middle"]
    game_score={}
    for i in range(4):
        game_score[methods[i]]=[]
    
    for i in range(4):
        iterator=[x for x in range(4) if x != i]
        for j in iterator:
            partial_agent_move1=partial(iterative_deepening_bitstring, three_piece=8, two_piece=1, method=methods[i])
            partial_agent_move2=partial(iterative_deepening_bitstring,three_piece=8, two_piece=1, method=methods[j])
       
            output=agent_vs_agent(generate_move_1=partial_agent_move1,generate_move_2=partial_agent_move2 ) 
            if output[0]==1: # the output[0] is the agent who last placed the move for win or draw
                # if it was agent 1 then it is the agent that loops over i
                game_score[methods[i]].append(output[1])

                if output[1]==1: # if game is draw then agent2 also gets score 1, else agent1 has won the game
                    game_score[methods[j]].append(1)
                else: # agent1 won the game so agent2 gets zero points
                    game_score[methods[j]].append(0)
            else: # same as before but we check if agent2 played the last piece that led to win or draw
                game_score[methods[j]].append(output[1])
                if output[1]==1:
                    game_score[methods[i]].append(1)
                else:
                    game_score[methods[i]].append(0)
    print(game_score)
    np.save(r'connect_four_ai\results\game_score_move_ordering.npy', game_score)
        