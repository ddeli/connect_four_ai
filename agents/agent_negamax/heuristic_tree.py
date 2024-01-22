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

def apply_move(child_board, move, playerview:PlayerView):
    if playerview == MaxView: child_board[0].append(move)
    else: child_board[1].append(move)
    return child_board