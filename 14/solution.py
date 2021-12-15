import time

def set_up():
    template, inserts, counts = "", {}, {}

    with open("input.txt") as file:
        for line in file:
            l = line.rstrip()
            if "->" in l:
                t = l.split(" -> ")
                inserts[t[0]] = t[1]
            elif l.isalpha():
                template = l
                for i in template:
                    counts[i] = counts.get(i, 0) + 1

    return template, inserts, counts


def one_step(tmp, ins, cnts):
    tmp_out = ""

    tmp_lst = list(tmp)
    pairs = list(map(list, zip(tmp_lst, tmp_lst[1:])))

    for p in pairs:
        i = ins.get("".join(p))
        tmp_out += p[0] + i
        cnts[i] = cnts.get(i, 0) + 1
    tmp_out += tmp[-1]

    return tmp_out, ins, cnts


def solution():
    template, inserts, counts = set_up()

    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------

    for _ in range(10):
        template, inserts, counts = one_step(template, inserts, counts)

    max_cnt = max(counts.keys(), key=(lambda k: counts[k]))
    min_cnt = min(counts.keys(), key=(lambda k: counts[k]))

    print(
        f"After 10 steps of pair insertion to the polymer template, the result is {counts[max_cnt] - counts[min_cnt]} ."
    )

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    for i in range(30):
        start = time.time()
        template, inserts, counts = one_step(template, inserts, counts)
        print(i + 10, (time.time() - start))

    max_cnt = max(counts.keys(), key=(lambda k: counts[k]))
    min_cnt = min(counts.keys(), key=(lambda k: counts[k]))

    print(
        f"After 40 steps of pair insertion to the polymer template, the result is {counts[max_cnt] - counts[min_cnt]} ."
    )


solution()
