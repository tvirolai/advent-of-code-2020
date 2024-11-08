from common import read_input

input = read_input("03.txt")


def is_tree(line, idx):
    return line[idx] == "#"


def count_path(input, right, down):
    count = 0
    data = input if down == 1 else [row for i, row in enumerate(input) if i % 2 == 0]
    for i, row in enumerate(data):
        index = i * right % len(row)
        if is_tree(row, index):
            count += 1
    return count


def part1(data):
    return count_path(data, 3, 1)


def part2(data):
    return (
        count_path(input, 1, 1)
        * count_path(input, 3, 1)
        * count_path(input, 5, 1)
        * count_path(input, 7, 1)
        * count_path(input, 1, 2)
    )


print(f"PART 1: {part1(input)}")
print(f"PART 2: {part2(input)}")
