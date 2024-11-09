import re
from common import read_raw_input


input = read_raw_input("04.txt")

EXPECTED = ["cid", "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
MANDATORY = set(EXPECTED[1:])


def parse_line(line):
    return [x.split(":") for x in line.split(" ")]


def parse(data):
    lines = input.split("\n")
    elements = [parse_line(line) for line in lines]
    passports = []
    curr = {}
    for line in elements:
        for el in line:
            if el == [""]:
                passports.append(curr)
                curr = {}
            else:
                [k, v] = el
                curr[k] = v
    return passports


def is_valid(passport):
    ks = set(passport.keys())
    return 0 == len(MANDATORY.difference(ks))


def part1():
    return len([x for x in parse(input) if is_valid(x)])


def to_year(s):
    digits = re.search("\d{4}", s)
    return int(digits.group())


def valid_element(element):
    [k, v] = element
    if k == "byr":
        y = to_year(v)
        return len(v) == 4 and 1920 <= y <= 2002
    if k == "iyr":
        y = to_year(v)
        return len(v) == 4 and 2010 <= y <= 2020
    if k == "eyr":
        y = to_year(v)
        return len(v) == 4 and 2020 <= y <= 2030
    if k == "hgt":
        digits = re.search("\d*", v)
        n = int(digits.group())
        if "cm" in v:
            return 150 <= n <= 193 and v == f"{n}cm"
        if "in" in v:
            return 59 <= n <= 76 and v == f"{n}in"
    if k == "hcl":
        return len(v) == 7 and bool(re.match("^#[0-9a-f]{6}$", v))
    if k == "ecl":
        return v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if k == "pid":
        return bool(re.match("\d{9}$", v))
    if k == "cid":
        return None
    return False


def is_valid2(passport):
    validities = [valid_element([k, passport[k]]) for k in passport]
    return is_valid(passport) and False not in validities


def part2():
    return len([x for x in parse(input) if is_valid2(x)])


print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")
