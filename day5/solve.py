import logging


def fill_in_blanks(dictionary):
    biggest = max(dictionary.keys())
    ret = dictionary.copy()
    for i in range(0, biggest+1):
        try:
            _ = ret[i]
        except KeyError:
            ret[i] = i
    return ret


def parse_ranges(starting, lines):
    map_draft = {x: x for x in starting}
    count = 0
    for line in lines:
        # We finished parsing the seed-soil map
        if line == "":
            break
        logging.debug(f"line: {line}")
        destination, source, length = tuple(line.split(" "))
        destination = int(destination)
        source = int(source)
        length = int(length)
        count += 1
        for i, j in zip(range(source, source + length), range(destination, destination + length)):
            # print(i, j)
            map_draft[i] = j
    lines = lines[count + 2:]
    return fill_in_blanks(map_draft), lines


def backtrack(first_dict, second_dict):
    # {a: b}, {b: c} -> {a: c}
    ret = {}
    for key, value in first_dict.items():
        ret[key] = second_dict[value]
    return ret


def parse(lines: list[str]):
    seeds = [int(x.strip()) for x in lines.pop(0).split(": ")[1].split(" ")]
    # Remove extra whitespace
    lines.pop(0)
    # Remove the "seed-to-soil map" line
    lines.pop(0)

    seed_soil_map, lines = parse_ranges(seeds, lines)

    soil_fertilizer_map, lines = parse_ranges([x for x in seed_soil_map.values()], lines)
    seed_fertilizer_map = backtrack(seed_soil_map, soil_fertilizer_map)
    logging.debug(f"seed_fertilizer_map: {seed_fertilizer_map}")

    fertilizer_water_map, lines = parse_ranges([x for x in soil_fertilizer_map.values()], lines)
    seed_water_map = backtrack(seed_fertilizer_map, fertilizer_water_map)
    logging.debug(f"seed_water_map: {seed_water_map}")

    water_light_map, lines = parse_ranges([x for x in fertilizer_water_map.values()], lines)
    seed_light_map = backtrack(seed_water_map, water_light_map)
    logging.debug(f"seed_light_map: {seed_light_map}")

    light_temperature_map, lines = parse_ranges([x for x in water_light_map.values()], lines)
    seed_temperature_map = backtrack(seed_light_map, light_temperature_map)
    logging.debug(f"seed_temperature_map: {seed_temperature_map}")

    temperature_humidity_map, lines = parse_ranges([x for x in light_temperature_map.values()], lines)
    seed_humidity_map = backtrack(seed_temperature_map, temperature_humidity_map)
    logging.debug(f"seed_humidity_map: {seed_humidity_map}")

    humidity_location_map, lines = parse_ranges([x for x in temperature_humidity_map.values()], lines)
    seed_location_map = backtrack(seed_humidity_map, humidity_location_map)
    logging.debug(f"seed_location_map: {seed_location_map}")

    return (seeds, seed_soil_map, seed_fertilizer_map, seed_water_map, seed_light_map,
            seed_temperature_map, seed_humidity_map, seed_location_map)


def solve_part1(parsed):
    seeds, _, _, _, _, _, _, seed_location_map = parsed
    original_seeds_location_map = {seed: location for seed, location in seed_location_map.items() if seed in seeds}
    return min(original_seeds_location_map.values())


def parse_part2(lines: list[str]):
    seeds = [int(x.strip()) for x in lines.pop(0).split(": ")[1].split(" ")]
    # modification for PART 2
    seed_ranges = []
    for i in range(0, len(seeds)-1, 2):
        seed_ranges.append((seeds[i], seeds[i+1]))
    seeds = []
    for start, length in seed_ranges:
        for i in range(start, start+length):
            seeds.append(i)

    # As normal

    # Remove extra whitespace
    lines.pop(0)
    # Remove the "seed-to-soil map" line
    lines.pop(0)

    seed_soil_map, lines = parse_ranges(seeds, lines)

    soil_fertilizer_map, lines = parse_ranges([x for x in seed_soil_map.values()], lines)
    seed_fertilizer_map = backtrack(seed_soil_map, soil_fertilizer_map)
    logging.debug(f"seed_fertilizer_map: {seed_fertilizer_map}")

    fertilizer_water_map, lines = parse_ranges([x for x in soil_fertilizer_map.values()], lines)
    seed_water_map = backtrack(seed_fertilizer_map, fertilizer_water_map)
    logging.debug(f"seed_water_map: {seed_water_map}")

    water_light_map, lines = parse_ranges([x for x in fertilizer_water_map.values()], lines)
    seed_light_map = backtrack(seed_water_map, water_light_map)
    logging.debug(f"seed_light_map: {seed_light_map}")

    light_temperature_map, lines = parse_ranges([x for x in water_light_map.values()], lines)
    seed_temperature_map = backtrack(seed_light_map, light_temperature_map)
    logging.debug(f"seed_temperature_map: {seed_temperature_map}")

    temperature_humidity_map, lines = parse_ranges([x for x in light_temperature_map.values()], lines)
    seed_humidity_map = backtrack(seed_temperature_map, temperature_humidity_map)
    logging.debug(f"seed_humidity_map: {seed_humidity_map}")

    humidity_location_map, lines = parse_ranges([x for x in temperature_humidity_map.values()], lines)
    seed_location_map = backtrack(seed_humidity_map, humidity_location_map)
    logging.debug(f"seed_location_map: {seed_location_map}")

    return (seeds, seed_soil_map, seed_fertilizer_map, seed_water_map, seed_light_map,
            seed_temperature_map, seed_humidity_map, seed_location_map)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    with open("testing") as f:
        parsed = parse([line.strip() for line in f.readlines()])
        print(solve_part1(parsed))
    with open("testing") as f:
        parsed_2 = parse_part2([line.strip() for line in f.readlines()])
        print(solve_part1(parsed_2))
