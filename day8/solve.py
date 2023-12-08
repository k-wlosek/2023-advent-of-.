import re
import math


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


def solve_part2(destinations, instructions):
    starting_positions = [x for x in destinations.keys() if x.endswith("A")]
    ending_positions = [x for x in destinations.keys() if x.endswith("Z")]

    # 1. Go through each starting position (until we hit an ending position) and find the cycle length
    cycle_lengths = []
    for start_pos in starting_positions:
        current_pos = start_pos
        cycle_length = 0
        while current_pos not in ending_positions:
            current_pos = destinations[current_pos][instructions[cycle_length % len(instructions)]]
            cycle_length += 1
        cycle_lengths.append(cycle_length)

    # 2. Take the LCM of the cycle lengths
    # This is the number of steps it would have taken, had we gone through all the cycles at the same time
    return math.lcm(*cycle_lengths)


if __name__ == "__main__":
    with open("testing") as f:
        lines = [line.strip() for line in f.readlines() if line.strip() != ""]
        instructions = list(lines.pop(0))
        destinations = parse_destinations(lines)
        print(solve_part1(destinations, instructions))
        print(solve_part2(destinations, instructions))
