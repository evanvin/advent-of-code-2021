def set_up():
    rows = []

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()
            rows.append(list(map(int, list(x))))
    return rows


NEIGH = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def is_safe(m, r, c):
    return r > -1 and r < len(m) and c > -1 and c < len(m[0])


def is_low_point(m, r, c):
    p = m[r][c]

    n_cnt = 0
    h_cnt = 0

    for i in NEIGH:
        rr, cc = r + i[0], c + i[1]

        if is_safe(m, rr, cc):
            n_cnt += 1
            if m[rr][cc] > m[r][c]:
                h_cnt += 1

    return n_cnt == h_cnt


def find_low_points(m):
    pts = []

    for r, _ in enumerate(m):
        for c, _ in enumerate(m[r]):
            if is_low_point(m, r, c):
                pts.append([r, c])

    return pts


def neighbours(point, max_x, max_y):
    return [(point[0], p) for p in (point[1] - 1, point[1] + 1) if 0 <= p < max_x] + [
        (p, point[1]) for p in (point[0] - 1, point[0] + 1) if 0 <= p < max_y
    ]


def part2(data, low_points):
    '''
    Used https://github.com/Rtchaik/AoC-2021/blob/main/Day09/solution.py
    for part 2
    '''
    from functools import reduce
    from operator import mul

    max_x = len(data[0])
    max_y = len(data)
    basins = []
    for point in low_points:
        new = {tuple(point)}
        basin = set()
        while new:
            basin |= new
            new = set().union(*[set(neighbours(p, max_x, max_y)) for p in new]) - basin
            new = {p for p in new if data[p[0]][p[1]] != 9}
        basins.append(len(basin))
    return reduce(mul, sorted(basins, reverse=True)[:3])


def solution():
    rows = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    low_points = find_low_points(rows)
    sum = 0
    for lp in low_points:
        sum += rows[lp[0]][lp[1]] + 1

    print(f"The sum of the risk levels of all low points on the heightmap is {sum}.")

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    print(f"The product of the three largest basins is {part2(rows, low_points)}.")


solution()
