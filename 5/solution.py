def set_up():
    input = []
    top_x, top_y = 0, 0

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip().split(" -> ")

            s = x[0].split(",")
            s[0] = int(s[0])
            s[1] = int(s[1])

            e = x[1].split(",")
            e[0] = int(e[0])
            e[1] = int(e[1])

            x = max(s[0], e[0])
            top_x = top_x if top_x > x else x

            y = max(s[1], e[1])
            top_y = top_y if top_y > y else y

            straight = s[0] == e[0] or s[1] == e[1]

            input.append({"straight": straight, "c": [s, e]})

    return input


def get_diagonal_points(start_x, start_y, end_x, end_y):
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

    result = []
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        result.append([i, j])
    result.append([end_x, end_y])
    return result


def solution():
    coords = set_up()
    all_pts = {}

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    hv_count = 0
    all_count = 0
    for p in coords:
        c = p["c"]
        if p["straight"]:
            # get points

            if c[0][0] == c[1][0]:
                mn, mx = min(c[0][1], c[1][1]), (max(c[0][1], c[1][1])) + 1
                for j in range(mn, mx):
                    t = str(c[0][0]) + "," + str(j)
                    if t not in all_pts:
                        all_pts[t] = 1
                    else:
                        if all_pts[t] < 2:
                            all_pts[t] = 2
                            hv_count += 1
                            all_count += 1
            else:
                mn, mx = min(c[0][0], c[1][0]), (max(c[0][0], c[1][0])) + 1
                for j in range(mn, mx):
                    t = str(j) + "," + str(c[0][1])
                    if t not in all_pts:
                        all_pts[t] = 1
                    else:
                        if all_pts[t] < 2:
                            all_pts[t] = 2
                            hv_count += 1
                            all_count += 1
        # ------------------------------------------------
        # Part 2
        # ------------------------------------------------
        else:
            pts = get_diagonal_points(c[0][0], c[0][1], c[1][0], c[1][1])
            for p in pts:
                t = str(p[0]) + "," + str(p[1])
                if t not in all_pts:
                    all_pts[t] = 1
                else:
                    if all_pts[t] < 2:
                        all_pts[t] = 2
                        all_count += 1

    print(
        f"There were {hv_count} times where at least 2 points overlapped horizontally/vertically."
    )

    print(
        f"There were {all_count} times where at least 2 points overlapped in any direction."
    )


solution()