def solution():
    input = []

    horizontal = 0
    depth = 0
    depth_2 = 0
    aim = 0

    # Part 1
    with open("input.txt") as file:
        for line in file:
            x = line.rstrip().split(" ")
            dir = int(x[1])

            if x[0][0] == 'f':
                horizontal += dir
                depth_2 += dir * aim
            elif x[0][0] == 'u':
                depth -= dir
                aim -= dir
            else:
                depth += dir
                aim += dir

            input.append(x)

    print(
        f"The submarine ends at {horizontal} horizontal and {depth} depth. The output for day 2 puzzle 1 is {horizontal*depth}"
    )

    # Part 2
    print(
        f"The submarine ends at {horizontal} horizontal, {depth_2} depth, and {aim} aim. The output for day 2 puzzle 2 is {horizontal*depth_2}"
    )


solution()