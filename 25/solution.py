from input import INPUT, EXAMPLE_1, EXAMPLE_2


def step_one(m):
    moves = 0
    skips = []
    prev = []

    # east
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == ">" and [i, j] not in skips:
                check = (j + 1) if (j + 1) < len(m[0]) else 0
                if m[i][check] == "." and [i, check] not in prev:
                    m[i][j] = "."
                    m[i][check] = ">"
                    prev.append([i, j])
                    skips.append([i, check])
                    moves += 1

    skips = []
    prev = []

    # south
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "v" and [i, j] not in skips:
                check = (i + 1) if (i + 1) < len(m) else 0
                if m[check][j] == "." and [check, j] not in prev:
                    m[i][j] = "."
                    m[check][j] = "v"
                    prev.append([i, j])
                    skips.append([check, j])
                    moves += 1

    return m, moves


def print_matrix(m):
    for i in range(0, len(m)):
        print(*m[i])


def solution():
    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    moves = 1
    steps = 0

    m = INPUT

    while moves > 0:
        m, moves = step_one(m)
        steps += 1
    print_matrix(m)

    print(f"It took {steps} steps for the sea cucumbers to stop moving.")


solution()
