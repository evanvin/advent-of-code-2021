def set_up():
    rows = []

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()
            rows.append(list(x))
    return rows


L, R = ["[", "(", "{", "<"], ["]", ")", "}", ">"]
corrupt_costs = {"]": 57, ")": 3, "}": 1197, ">": 25137}
autocomplete_costs = {"[": 2, "(": 1, "{": 3, "<": 4}


def solution():
    rows = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    syntax_error_score = 0
    autocomplete_scores = []

    for row in rows:
        stack = []
        corrupted = False
        for c in row:
            if c in L:
                stack.append(c)
            else:
                if len(stack) > 0:
                    l = L.index(stack[-1])
                    r = R.index(c)

                    if l == r:
                        stack.pop()
                    else:
                        syntax_error_score += corrupt_costs.get(c)
                        corrupted = True
                        break

                else:
                    print("ran out of chars")
                    pass
        # ------------------------------------------------
        # Part 2
        # ------------------------------------------------
        if not corrupted:
            autocomplete_score = 0
            for _ in range(len(stack)):
                autocomplete_score *= 5
                autocomplete_score += autocomplete_costs.get(stack.pop())
            autocomplete_scores.append(autocomplete_score)

    print(f"The total syntax error score is {syntax_error_score}")

    autocomplete_scores.sort()
    print(
        f"The middle autocomplete score is {autocomplete_scores[int(len(autocomplete_scores)/2)]}"
    )


solution()
