from helper import *

def part1(filename: str) -> int:
    workflows, parts = readInput(filename)
    input = parseInput(workflows, parts)
    running_total = 0
    for part in input.parts:
        running_total += calculatePartValue(input.workflows, part)
    return running_total

if __name__ == "__main__":
    print(part1("testing"))