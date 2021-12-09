def set_up():
    segs = []

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip().split(" | ")
            seg = {"patterns": x[0].split(), "output": x[1].split(), "lengths": {}}

            for p in seg["patterns"]:
                if len(p) not in seg["lengths"]:
                    seg["lengths"][len(p)] = [p]
                else:
                    seg["lengths"][len(p)].append(p)

            segs.append(seg)

    return segs


def get_numbers(s):
    # find B
    one = set(s["lengths"][2][0])
    seven = set(s["lengths"][3][0])
    B = list(one.symmetric_difference(seven))[0]

    # find 6
    SIX = ""
    z_n = []
    for n in s["lengths"][6]:
        t_a = set(n)
        t_b = t_a.symmetric_difference(one)
        if len(t_b) == 6:
            SIX = n
        else:
            z_n.append(n)

    # find C
    eight = set(s["lengths"][7][0])
    C = list(set(SIX).symmetric_difference(eight))[0]

    # find G
    G = list(one.symmetric_difference(C))[0]

    # find D & E & F & 0 & 9
    four_seven = set(s["lengths"][4][0] + s["lengths"][3][0])
    ZERO = ""
    NINE = ""

    for n in z_n:
        t_a = set(n)
        t_b = t_a.symmetric_difference(four_seven)
        if len(t_b) == 3:
            ZERO = n
        else:
            NINE = n

    D = list(eight.symmetric_difference(ZERO))[0]
    E = list(eight.symmetric_difference(set(NINE)))[0]
    F = list(set(NINE).symmetric_difference(four_seven))[0]

    # Get A
    A = list(set(B + C + D + E + F + G).symmetric_difference(set("abcdefg")))[0]

    return [
        "".join(sorted((A + B + C + E + F + G))),  # 0
        "".join(sorted((C + G))),  # 1
        "".join(sorted((B + C + D + E + F))),  # 2
        "".join(sorted((B + C + D + F + G))),  # 3
        "".join(sorted((A + C + D + G))),  # 4
        "".join(sorted((A + B + D + F + G))),  # 5
        "".join(sorted((A + B + D + E + F + G))),  # 6
        "".join(sorted((B + C + G))),  # 7
        "".join(sorted((A + B + C + D + E + F + G))),  # 8
        "".join(sorted((A + B + C + D + F + G))),  # 9
    ]


# len  |  nums
# ------------
#  2   |   1
#  3   |   7
#  4   |   4
#  5   | 2,3,5
#  6   | 0,6,9
#  7   |   8

# ----------------

#    BBBB
#   A    C
#   A    C
#    DDDD
#   E    G
#   E    G
#    FFFF

'''
1           = C & G
1 vs 7      = B
1 vs 6,9,0  = 6
-> 6 vs 8   = C --> G
-> 9 vs 0   = 0 & 9
-> 0 vs 8   = D
-> 1 vs 4   = A

4+7 vs 8    = E & F

'''


def solution():
    segs = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    count = 0

    for s in segs:
        for o in s["output"]:
            if len(o) in [2, 3, 4, 7]:
                count += 1

    print(f"There are {count} 1's/4's/7's/8's that appear in the output values.")

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    sum = 0
    for s in segs:
        nums = get_numbers(s)
        out = []

        for i in s["output"]:
            out.append(str(nums.index("".join(sorted(i)))))
        sum += int("".join(out))

    print(f"The sum of all the output values is {sum}.")


solution()