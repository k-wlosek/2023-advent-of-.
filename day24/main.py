from helper import *


def part1(filename: str, bounds: tuple[int]) -> int:
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
    hailstones = parse_input(lines)
    sum = 0
    for pair in pair_up(hailstones):
        if crossed_in_bounds(pair[0], pair[1], bounds):
            sum += 1
    return sum


if __name__ == "__main__":
    print(part1("testing", (7, 27)))
