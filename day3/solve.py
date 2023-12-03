import re


def solve_part1(lines: list[str]):
    num_coords = []
    symbol_coords = []

    for x, line in enumerate(lines):
        nums = re.finditer(r'\d+', line)
        for n in nums:
            coords = [(x, n.start() + i) for i in range(len(n.group()))]
            num_coords.append([n.group(), coords])

        symbols = re.finditer(r'[^.\d]', line)
        for s in symbols:
            symbol_coords.append([s.group(), (x, s.start())])

    adj_nums = []
    for n in num_coords:
        for c in n[1]:
            for s in symbol_coords:
                if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
                    adj_nums.append(n) if n not in adj_nums else 0
                    break

    return sum([int(n[0]) for n in adj_nums])


def solve_part2(lines: list[str]):
    num_coords = []
    symbol_coords = []

    for x, line in enumerate(lines):
        nums = re.finditer(r'\d+', line)
        for n in nums:
            coords = [(x, n.start() + i) for i in range(len(n.group()))]
            num_coords.append([int(n.group()), coords])

        symbols = re.finditer(r'[*]', line)
        for s in symbols:
            symbol_coords.append([s.group(), (x, s.start()), []])

    for n in num_coords:
        for c in n[1]:
            for s in symbol_coords:
                if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
                    s[2].append(n) if n not in s[2] else 0
                    break

    return sum([s[2][0][0] * int(s[2][1][0]) for s in symbol_coords if len(s[2]) == 2])


if __name__ == "__main__":
    with open("testing") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(solve_part1(lines))
        print(solve_part2(lines))
