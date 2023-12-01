#/usr/bin/env python3


def solve_part1(lines: list[str]) -> int:
    result: int = 0
    for line in lines:
        numbers: list[int] = []
        for character in line:
            try:
                temp = int(character)
                numbers.append(temp)
            except ValueError:
                pass
        result += 10*numbers[0] + numbers[-1]
    return result


if __name__ == '__main__':
    with open('testing') as f:
        lines: list[str] = f.readlines()
    print(solve_part1(lines))