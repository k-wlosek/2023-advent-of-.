

def parse(lines: list[str]):
    ret = {}
    for line in lines:
        line_split = line.strip().split(": ")
        card_no = int(line_split[0].split(" ")[-1])
        line_split = [x.strip() for x in line_split[1].split("|")]
        winning_numbers = [int(x) for x in line_split[0].split(" ") if x != ""]
        scratched_numbers = [int(x) for x in line_split[1].split(" ") if x != ""]
        ret[card_no] = (winning_numbers, scratched_numbers)
    return ret


def solve_part1(parsed: dict[int, tuple[list[int], list[int]]]):
    sum = 0
    for _, (winning_numbers, scratched_numbers) in parsed.items():
        correct_guesses_count = len([x for x in winning_numbers if x in scratched_numbers])
        sum += 2**(correct_guesses_count-1) if correct_guesses_count > 0 else 0
    return sum


if __name__ == "__main__":
    with open("testing_part1", "r") as f:
        parsed = parse(f.readlines())
        print(solve_part1(parsed))
