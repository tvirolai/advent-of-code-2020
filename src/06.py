from common import read_input

input = read_input("06.txt")


def part1():
    counts = []
    curr = set()
    for i, x in enumerate(input):
        for c in list(x):
            curr.add(c)
        if x == "" or i == len(input) - 1:
            counts.append(len(curr))
            curr = set()
    return sum(counts)


def part2():
    counts = []
    curr = set()
    first = True
    for i, x in enumerate(input):
        if x == "":
            counts.append(len(curr))
            curr = set()
            first = True
            continue
        if first:
            for c in list(x):
                curr.add(c)
            first = False
        curr = curr.intersection(set(x))
        if i == len(input) - 1:
            counts.append(len(curr))
    return sum(counts)


print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")
