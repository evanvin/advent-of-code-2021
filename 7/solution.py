def set_up():
    loc = {}
    nums = []

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()
            nums = list(map(int, x.split(",")))

    loc = {i: 0 for i in range(min(nums), max(nums) + 1)}

    return loc, nums


def triangular_number(n):
    if n == 0:
        return 0

    i = n
    while True:
        if i == 1:
            return n
        i -= 1
        n += i


def solution():
    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    loc, nums = set_up()
    for n in nums:
        for k in loc.keys():
            loc[k] += abs(k - n)

    lowest_idx = min(loc, key=loc.get)
    print(
        f"The crab submarines should move to with the lowest total fuel cost of {loc[lowest_idx]} is position {lowest_idx}."
    )

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    loc, nums = set_up()
    cache = {}
    for n in nums:
        for k in loc.keys():
            dist = abs(k - n)
            cost = 0
            if dist in cache:
                cost = cache[dist]
            else:
                tn = triangular_number(dist)
                cache[dist] = tn
                cost = tn
            loc[k] += cost

    lowest_idx = min(loc, key=loc.get)
    print(
        f"The crab submarines should move to (becaus of their crazy fuel costs) with the lowest total fuel cost of {loc[lowest_idx]} is position {lowest_idx}."
    )


solution()