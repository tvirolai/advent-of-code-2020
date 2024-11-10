from common import read_input

input = read_input("05.txt")


def take_upper(rang):
    [lower, upper] = rang
    diff = upper - lower
    if diff == 1:
        return upper
    new_min = ((diff + 1) / 2) + lower
    return [new_min, upper]


def take_lower(rang):
    [lower, upper] = rang
    diff = upper - lower
    if diff == 1:
        return lower
    return [lower, (upper - (diff + 1) / 2)]


assert take_upper([0, 7]) == [4, 7]
assert take_lower([4, 7]) == [4, 5]
assert take_lower([4, 7]) == [4, 5]
assert take_upper([4, 5]) == 5


def search(instr, min, max, lowmarker, highmarker):
    rang = [min, max]
    for char in instr:
        if char == lowmarker:
            rang = take_lower(rang)
        if char == highmarker:
            rang = take_upper(rang)
    return int(rang)


def get_seat(instr):
    row_instr = list(instr[:7])
    col_instr = list(instr[7:])
    return [search(row_instr, 0, 127, "F", "B"), search(col_instr, 0, 7, "L", "R")]


assert get_seat("FBFBBFFRLR") == [44, 5]
assert get_seat("BFFFBBFRRR") == [70, 7]
assert get_seat("FFFBBBFRRR") == [14, 7]
assert get_seat("BBFFBBFRLL") == [102, 4]


def get_id(seat):
    [row, col] = seat
    return row * 8 + col


def get_all_ids(input):
    return sorted([get_id(get_seat(x)) for x in input])


def part1():
    return max(get_all_ids(input))


def part2():
    ids = get_all_ids(input)
    for i, x in enumerate(ids):
        if i == 0:
            continue
        if x - ids[i - 1] == 2:
            return x - 1


print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")
