def set_up():
    fish, babies = [0 for _ in range(7)], [0, 0]

    with open("input.txt") as file:
        for line in file:
            x = line.rstrip().split(",")
            for i in x:
                fish[int(i)] += 1

    return fish, babies


def rotateArray(arr):
    return arr[1:] + arr[:1]


def solution():
    # ------------------------------------------------
    # Part 1
    # ------------------------------------------------
    fish, babes = set_up()
    for _ in range(80):
        new_babes = fish[0]
        fish = rotateArray(fish)

        fish[6] += babes[0]
        babes[0] = babes[1]
        babes[1] = new_babes

    print(f"After 80 days, there are {sum(fish+babes)} lanternfish.")

    # ------------------------------------------------
    # Part 2
    # ------------------------------------------------
    fish, babes = set_up()
    for _ in range(256):
        new_babes = fish[0]
        fish = rotateArray(fish)

        fish[6] += babes[0]
        babes[0] = babes[1]
        babes[1] = new_babes

    print(f"After 256 days, there are {sum(fish+babes)} lanternfish.")


solution()