from common import read_input


def parse_instr(instr):
    [values, char] = instr.split(" ")
    [min, max] = values.split("-")
    return (int(min), int(max), char)


def parse(input):
    [instr, password] = input.strip().split(":")
    return [parse_instr(instr), password.strip()]


input = [parse(x) for x in read_input("02.txt")]


def is_valid_1(instr, password):
    [min, max, char] = instr
    return min <= password.count(char) <= max


def is_valid_2(instr, password):
    [min, max, char] = instr
    c1 = password[min - 1]
    c2 = password[max - 1]
    return (c1 == char and c2 != char) or (c2 == char and c1 != char)


def solve(part):
    fn = is_valid_1 if part == 1 else is_valid_2
    return sum([1 for instr, password in input if fn(instr, password)])

print("PART 1: {0}".format(solve(1)))
print("PART 2: {0}".format(solve(2)))
