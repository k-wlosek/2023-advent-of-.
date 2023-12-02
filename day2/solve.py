"""
Day 2
"""


def parse(input_list: list):
    """
    Transform input list into a dictionary, where the key is the game id and the value is a list of the game results.
    :param input_list: lines read from a file
    :return: game results
    """
    lines = {}
    for line in input_list:
        line = line.strip()
        game_id = int(line.split(":")[0].split(" ")[1])
        game = []
        for i, result in enumerate(line.split(";")):
            if i == 0:
                result = result.split(":")[1].strip()
            else:
                result = result.strip()
            subset = [0, 0, 0]
            colors = [x.strip() for x in result.split(",")]
            for color in colors:
                color_str_split = color.split(" ")
                if color_str_split[1] == "red":
                    subset[0] = int(color_str_split[0])
                elif color_str_split[1] == "green":
                    subset[1] = int(color_str_split[0])
                elif color_str_split[1] == "blue":
                    subset[2] = int(color_str_split[0])
            game.append(subset)
        lines[game_id] = game
    return lines


def solve_part1(game_results: dict):
    sum = 0
    for key, value in game_results.items():
        invalid = False
        for result in value:
            red = result[0]
            green = result[1]
            blue = result[2]
            if red > 12 or green > 13 or blue > 14:
                invalid = True
                break
        if not invalid:
            sum += key
    return sum


def solve_part2(game_results: dict):
    set_sum = []
    for key, value in game_results.items():
        reds = [x[0] for x in value]
        greens = [x[1] for x in value]
        blues = [x[2] for x in value]
        set_sum.append(max(reds) * max(greens) * max(blues))
    return sum(set_sum)


if __name__ == '__main__':
    with open('input') as f:
        parsed = parse(f.readlines())
        print(solve_part1(parsed))
        print(solve_part2(parsed))
