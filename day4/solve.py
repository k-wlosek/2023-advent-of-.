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
        sum += 2 ** (correct_guesses_count - 1) if correct_guesses_count > 0 else 0
    return sum


def solve_part2(parsed: dict[int, tuple[list[int], list[int]]]):
    winning_scratched_pairs = [(winning, scratched) for _, (winning, scratched) in parsed.items()]
    matched_and_scratched = [
        [
            [x for x in winning if x in scratched],
            scratched
        ] for winning, scratched in winning_scratched_pairs
    ]
    card_counts = [
        [
            1, len([x for x in winning if x in scratched])
        ] for winning, scratched in matched_and_scratched
    ]

    total_cards = 0
    for i, n in enumerate(card_counts):
        total_cards += n[0]
        for _ in range(n[0]):
            for j in range(1, n[1] + 1):
                card_counts[i + j][0] += 1

    return total_cards


if __name__ == "__main__":
    with open("testing", "r") as f:
        parsed = parse(f.readlines())
        print(solve_part1(parsed))
        print(solve_part2(parsed))
