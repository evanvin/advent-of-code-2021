class BreakIt(Exception):
    pass


HORZ_WIN = [-1, -1, -1, -1, -1]


def set_up():
    numbers = []
    boards = []
    current_board = []

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()

            if "," in x:
                # call numbers
                numbers = list(map(int, x.split(",")))
            elif len(x) < 1:
                if len(current_board) > 0:
                    boards.append(current_board)
                    current_board = []
            else:
                map_obj = map(int, x.split())
                current_board.extend(list(map_obj))
        boards.append(current_board)

        return numbers, boards


def the_sum(aList):
    s = 0
    for x in aList:
        if x > 0:
            s = s + x
    return s


def is_board_winner(board):
    # check horizontal wins
    for i in range(5):
        if board[i::5] == HORZ_WIN:
            return the_sum(board)

    # check vertical wins
    for i in range(0, len(board), 5):
        if board[i : i + 5] == HORZ_WIN:
            return the_sum(board)

    return None


def print_board(b):
    for i in range(0, len(b), 5):
        print(b[i : i + 5])


def solution():
    numbers, boards = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    numbers, boards = set_up()
    winners = []
    last_winner_score = 0

    for n in numbers:
        for idx, b in enumerate(boards):
            if idx not in winners:
                boards[idx] = [x if x != n else -1 for x in boards[idx]]
                c = is_board_winner(boards[idx])
                if c:
                    winners.append(idx)
                    last_winner_score = c * n
                    print(
                        f"Board #{idx+1} has won on number {n}, and the final score is {c*n}. Sum of unmarked is {c}."
                    )


solution()