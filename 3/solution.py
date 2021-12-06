import copy


def get_bit_counts(numbers, idx=-1):
    bit_counts = [
        [0, 0] for _ in numbers[0]
    ]  # a list of lists that keep track of the counts of 0 and 1 bits

    start = 0 if idx == -1 else idx
    end = len(bit_counts) if idx == -1 else idx + 1
    for n in numbers:
        for j in range(start, end):
            if n[j] == "0":
                bit_counts[j][0] += 1
            else:
                bit_counts[j][1] += 1

    return bit_counts


def solution():
    input = []

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    with open("input.txt") as file:
        for line in file:
            x = line.rstrip()
            input.append(x)

    bit_counts = get_bit_counts(input)
    gamma = [""] * len(bit_counts)
    epsilon = [""] * len(bit_counts)

    for i in range(len(bit_counts)):
        if bit_counts[i][0] > bit_counts[i][1]:
            gamma[i] = "0"
            epsilon[i] = "1"
        else:
            gamma[i] = "1"
            epsilon[i] = "0"

    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)

    print(
        f"Multiplying the gamma rate ({gamma}) by the epsilon rate ({epsilon}) produces the power consumption, {gamma*epsilon}."
    )

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    oxygen, co2 = 0, 0

    for bits in [["0", "1"], ["1", "0"]]:
        nums = copy.deepcopy(input)
        idx = 0

        while len(nums) > 1:
            keeps = bits[0]
            if bit_counts[idx][1] >= bit_counts[idx][0]:
                keeps = bits[1]

            nums = [x for x in nums if x[idx] == keeps]
            idx += 1
            bit_counts = get_bit_counts(nums, idx)

        if bits[0] == "0":
            oxygen = int("".join(nums[0]), 2)
        else:
            co2 = int("".join(nums[0]), 2)

    print(
        f"Multiplying the oxygen generator rating ({oxygen}) by the CO2 scrubber rating ({co2}) produces the life support rating, {oxygen*co2}."
    )


solution()