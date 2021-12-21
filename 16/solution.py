from input import INS, CONV

packets = []

'''
I wanted to make this even though I know there are libraries out there
'''


def hex_to_bin(hex):
    binary = ""

    for i in list(hex):
        binary += CONV[i]

    return binary


def get_packets(b, ltid_0=0, ltid_1=0):
    # print(b)



    if len(b) < 11:
        return None

    pkt = {"version": int("".join(b[:3]), 2), "type_id": int("".join(b[3:6]), 2)}
    if pkt["type_id"] == 4:
        # get literal value
        groups = []
        for i in range(6, len(b), 5):
            groups.append(b[i : i + 5])
            if groups[-1][0] == "0":
                pkt["binary"] = b[: i + 5]
                pkt["end"] = i + 5
                break
        pkt["literal_value"] = int("".join(["".join(x[1:]) for x in groups]), 2)

        packets.append(pkt)
        print(pkt)

        if ltid_0:
            get_packets(b[pkt["end"] :], ltid_0=ltid_0 - pkt["end"])
        elif ltid_1:
            get_packets(b[pkt["end"] :], ltid_1=ltid_1 - 1)
    else:
        packets.append(pkt)
        if b[6] == "0":
            # next 15 bits represents the number of bits in the sub-packets (total sum)
            num = int("".join(b[7:22]), 2)
            subs = b[22 : 22 + num]
            print(f"operator 0: total sum of subpackets {num} and it looks like {subs}")
            print(pkt)
            get_packets(b[22:], ltid_0=num)
        else:
            # next 11 bits represents the number of sub-packets
            num = int("".join(b[7:18]), 2)
            print(f"operator 1: total subpackets {num}")
            print(pkt)
            get_packets(b[18:], ltid_1=num)


def solution():
    b = hex_to_bin(INS["input"]["input"])

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    get_packets(b)

    version_sum = 0
    for p in packets:
        # print(p)
        version_sum += p["version"]

    print(f"The total sum of all versions number is {version_sum} .")

    # # ------------------------------------------------
    # # Part 2
    # # ------------------------------------------------
    # for f in folds[1:]:
    #     paper, count = fold(paper, f)

    # print_matrix(paper)
    # print(f"The code is output above...")


solution()
