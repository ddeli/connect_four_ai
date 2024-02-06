import numpy as np
import matplotlib.pyplot as plt


game_players=np.load(r'connect_four_ai\results\game_players_move_ordering_timetable.npy', allow_pickle=True).item() #ended up not needing this
game_timetable=np.load(r'connect_four_ai\results\game_score_move_ordering_timetable.npy',allow_pickle=True).item()

methods=["pv", "ltr", "random", "middle"]    
k=0
player_game_timetable={}
for i in methods:
    player_game_timetable[i]=[]
for i in range(4):
    iterator=[x for x in range(4) if x != i]
    for j in iterator:
        player1, method1=1, methods[i]
        player2, method2=2, methods[j]
        player_game_timetable[method1].append(game_timetable[f'game{k}'][player1])
        player_game_timetable[method2].append(game_timetable[f'game{k}'][player2])
        k+=1

for i in range(len(player_game_timetable['pv'])):
    plt.plot(player_game_timetable['pv'][i], color='red')
    plt.plot(player_game_timetable['ltr'][i], color='pink')
    plt.plot(player_game_timetable['random'][i], color='gray')
    plt.plot(player_game_timetable['middle'][i], color='skyblue')

plt.xlabel('agent move #')
plt.ylabel('move time (s)')
plt.xticks(range(0,20,5))
plt.suptitle('Comparing move time for agent with different move orders')
plt.legend(['principle-of-variation', 'left-to-right', 'random', 'middle'])
plt.show()
plt.savefig(r'connect_four_ai\results\Figure_1.png')



plt.suptitle('Move time for agent with different move orders')
for i in range(len(player_game_timetable['pv'])):
    plt.subplot(2,2,1)
    plt.plot(player_game_timetable['pv'][i], color='red')
    #plt.xlabel('agent move #')
    plt.ylabel('move time (s)')
    plt.xticks(range(0,20,5))
    plt.ylim(0,9)
    plt.legend(['principle-of-variation'], fontsize=8)
    plt.subplot(2,2,2)
    plt.plot(player_game_timetable['ltr'][i], color='pink')
    #plt.xlabel('agent move #')
    #plt.ylabel('move time (s)')
    plt.xticks(range(0,20,5))
    plt.ylim(0,9)
    plt.legend(['left-to-right'], fontsize=8)
    plt.subplot(2,2,3)
    plt.plot(player_game_timetable['middle'][i], color='skyblue')
    plt.xlabel('agent move #')
    plt.ylabel('move time (s)')
    plt.xticks(range(0,20,5))
    plt.ylim(0,9)
    plt.legend(['middle'], fontsize=8)
    plt.subplot(2,2,4)
    plt.plot(player_game_timetable['random'][i], color='gray')
    plt.xlabel('agent move #')
    #plt.ylabel('move time (s)')
    plt.xticks(range(0,20,5))
    plt.ylim(0,9)
    plt.legend(['random'], fontsize=8)

plt.show()
plt.savefig(r'connect_four_ai\results\Figure_2.png')
