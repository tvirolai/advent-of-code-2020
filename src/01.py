from common import read_input_as_nums

input = read_input_as_nums("01.txt")

def part1(input, TARGET):
    for x in input:
        if (TARGET - x) in input:
            return x * (TARGET - x)


print("PART 1: {0}".format(part1(input, 2020)))


def part2(input):
    for i, x in enumerate(input):
        rest = input[:i] + input[i+1:]
        target = 2020 - x
        res = part1(rest, target)
        if res:
            return res * x

print("PART 2: {0}".format(part2(input)))
