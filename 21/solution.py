IN = {"example": [3, 7], "input": [3, 8]}


def rotate_array(arr):
    return arr[3:] + arr[:3]


def solution():
    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    die = [n for n in range(1, 101)]
    players = IN.get("input")
    scores = [0, 0]
    turn = 0
    die_thrown = 0

    while scores[0] < 1000 and scores[1] < 1000:
        players[turn] = (players[turn] + sum(die[:3])) % 10
        scores[turn] += players[turn] + 1
        die_thrown += 3
        turn ^= 1
        die = rotate_array(die)

    print(f"Part one answer is {min(scores)*die_thrown} .")

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------

    # print(f"After 256 days, there are {sum(fish+babes)} lanternfish.")


solution()
