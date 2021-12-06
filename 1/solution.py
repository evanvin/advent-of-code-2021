def solution():
    depths = []
    count = 0
    last = None

    # Part 1
    with open("input.txt") as file:
        for line in file:
            x = int(line.rstrip())
            if last and x > last:
                count += 1
            last = x
            depths.append(x)

    print(
        f"There are {count} measurements that are larger than the previous measurement."
    )

    count = 0
    last = None

    # Part 2
    groupings = [sum(depths[i : i + 3]) for i in range(0, len(depths) - 2)]
    for g in groupings:
        if last and g > last:
            count += 1
        last = g

    print(f"There are {count} sums that are larger than the previous sum.")


solution()
