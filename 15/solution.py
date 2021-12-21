import sys


def set_up():
    mx = []
    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()
            mx.append(list(map(int, list(x))))
    return mx


# Naive recursive function to find the minimum cost to reach
# cell (m, n) from cell (0, 0)
def find_min_cost(cost, m=None, n=None):

    # initialize m and n
    if not m and not n:
        m, n = len(cost), len(cost[0])

    # base case
    if not cost or not len(cost):
        return 0

    # base case
    if n == 0 or m == 0:
        return sys.maxsize

    # if we are in the first cell (0, 0)
    if m == 1 and n == 1:
        return cost[0][0]

    # include the current cell's cost in the path and recur to find the minimum
    # of the path from the adjacent left cell and adjacent top cell.
    return (
        min(find_min_cost(cost, m - 1, n), find_min_cost(cost, m, n - 1))
        + cost[m - 1][n - 1]
    )


def solution():
    mx = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    min_cost = find_min_cost(mx)

    print(
        f"The lowest total risk path is {min}, and subtracting the first spot once is {min_cost-mx[0][0]} ."
    )

    # # ------------------------------------------------
    # # Part 2
    # # ------------------------------------------------
    # for f in folds[1:]:
    #     paper, count = fold(paper, f)

    # print_matrix(paper)
    # print(f"The code is output above...")


solution()
