import copy


def set_up():
    dots, folds = [], []
    max_x, max_y = 0, 0

    with open("input.txt") as file:
        for line in file:
            l = line.rstrip()
            if "," in l:
                t = l.split(",")
                x = int(t[0])
                max_x = max(x, max_x)

                y = int(t[1])
                max_y = max(y, max_y)

                dots.append([x, y])
            elif "=" in l:
                f = l[11:].split("=")
                folds.append([f[0], int(f[1])])

    paper = [
        ["#" if [x, y] in dots else "." for x in range(max_x + 1)]
        for y in range((max_y + 1))
    ]

    return paper, folds


def print_matrix(m):
    print("-----------------------------------------------------------------------------")
    for i in m:
        x = [" " if x == "." else x for x in i]
        print(*x)
    print("-----------------------------------------------------------------------------")


def fold(p, f):
    count = 0

    out = []

    if f[0] == 'y':
        out = copy.deepcopy(p[: f[1]])
        bottom = copy.deepcopy(p[f[1] + 1 :])

        for idx, row in enumerate(bottom):
            for i in range(len(out[0])):
                if row[i] == "#":
                    out[len(out) - idx - 1][i] = "#"
    else:
        out = [[b for b in a[: f[1]]] for a in p]
        right = [[b for b in a[f[1] + 1 :]] for a in p]

        for idx, row in enumerate(right):
            for i in range(len(right[0])):
                if row[i] == "#":
                    out[idx][len(out[0]) - i - 1] = "#"
    # count #'s
    for x in range(len(out)):
        for y in range(len(out[0])):
            if out[x][y] == "#":
                count += 1

    return out, count


def solution():
    paper, folds = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    paper, count = fold(paper, folds[0])

    print(f"There are a total of {count} visible dots after the first fold.")

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    for f in folds[1:]:
        paper, count = fold(paper, f)

    print_matrix(paper)
    print(f"The code is output above...")


solution()
