import re


def parse_destinations(lines):
    destinations = {}
    for line in lines:
        destination, value = line.split(" = ")
        matches = re.findall(r"(\w+)", value)
        destinations[destination] = {
            "L": matches[0],
            "R": matches[1],
        }
    return destinations


def solve_part1(destinations, instructions):
    current_position = "AAA"
    steps = 0
    while current_position != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        steps += 1
        current_position = destinations[current_position][instruction]
    return steps


if __name__ == "__main__":
    with open("input") as f:
        lines = [line.strip() for line in f.readlines() if line.strip() != ""]
        instructions = list(lines.pop(0))
        destinations = parse_destinations(lines)
        print(solve_part1(destinations, instructions))
