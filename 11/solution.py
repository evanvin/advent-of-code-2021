import copy


def set_up():
    rows = []

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()
            l = list(map(int, list(x)))
            l.insert(0, -2)
            l.append(-2)
            rows.append(l)

    rows.insert(0, [-2] * 12)
    rows.append([-2] * 12)

    return rows


def print_matrix(m):
    for i in range(1, len(m) - 1):
        print(*m[i][1:11])


def count_and_clear_flashes(m):
    count = 0
    for r in range(1, len(m) - 1):
        for c in range(1, len(m) - 1):
            if m[r][c] > 9:
                m[r][c] = 0
                count += 1
    return m, count


def one_step(m):
    # obligatory +1
    for r in range(1, len(m) - 1):
        for c in range(1, len(m) - 1):
            m[r][c] += 1

    # check flashes
    f = [[False for _ in range(12)] for _ in range(12)]
    for _ in range(10):
        for r in range(1, len(m) - 1):
            for c in range(1, len(m) - 1):
                if m[r][c] > 9 and not f[r][c]:
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if a == 0 and b == 0:
                                continue
                            if m[r + a][c + b] != -2:
                                m[r + a][c + b] += 1
                    f[r][c] = True

    return count_and_clear_flashes(m)


def solution():
    rows = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    total_flashes = 0
    for _ in range(100):
        rows, step_cnt = one_step(rows)
        total_flashes += step_cnt

    print(
        f"After 100 steps, there were a total of {total_flashes} dumbo octopus flashes."
    )

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    rows = set_up()
    step_flashes = 0
    count = 0
    while step_flashes != 100:
        rows, step_flashes = one_step(rows)
        count += 1

    print(f"It took {count} steps for all the dumbo octopus to flash at once.")


solution()
