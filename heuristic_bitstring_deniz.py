def evaluate(bitstring:list[str], player) -> int:
    return count_two_connected_pieces(bitstring)


def count_two_connected_pieces(positions: list[str]) -> int:
    counter = 0
    score = 0

    binary = int(positions[0], 2)
    m = binary & (binary >> 7)

    print(positions[0])
    print(len(str(bin(m))) - 2)
    print(str(bin(m)))
    print(str(bin(m))[len(str(bin(m))) - 28])
    print("--------------------")
    pos_player = positions[0]
    pos_opponent = positions[1]
    for i in range(len(pos_player) - 1, 0, -1):
        print(pos_player[i])
        if pos_player[i] == '1':
            if i > 7:
                if pos_player[i - 7] == '1':
                    counter = counter + 1
                    if i > 14:
                        if pos_player[i - 14] == '0' and pos_opponent[i - 14] == '0':
                            score = score + 1
                            if i > 21:
                                if pos_player[i - 21] == '1':
                                    score = score + 100
                                if pos_player[i - 21] == '0' and pos_opponent[i - 14] == '0':
                                    score = score + 10
            if i < len(pos_player) - 7:
                if pos_player[i + 7] == '1':
                    counter = counter + 1
                    if i < len(pos_player) - 14:
                        if pos_player[i + 14] == '0' and pos_opponent[i - 14] == '0':
                            score = score + 1
                            if i < len(pos_player) - 21:
                                if pos_player[i + 21] == '1':
                                    score = score + 100
                                if pos_player[i + 21] == '0' and pos_opponent[i - 14] == '0':
                                    score = score + 10

    print("Der Counter ist bei: " + str(counter))
    print("Der Score ist: " + str(score))

    return score

