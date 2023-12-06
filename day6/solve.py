
def part_1(lines):
    times = [x.strip() for x in lines[0].split(" ") if x]
    # Pop header
    times.pop(0)
    times = [int(x) for x in times]
    distances = [x.strip() for x in lines[1].split(" ") if x]
    # Pop header
    distances.pop(0)
    distances = [int(x) for x in distances]
    product_of_sums = 1
    for time, distance in zip(times, distances):
        # Initial speed is 0 mm/ms, we can charge for 1 ms to get 1 mm/ms
        times_we_beat_the_highscore = 0
        for time_charging in range(1, time):
            # Go through all the times we can charge and see if we beat the highscore
            distance_covered = time_charging * (time-time_charging)
            if distance_covered > distance:
                times_we_beat_the_highscore += 1
        product_of_sums *= times_we_beat_the_highscore
    return product_of_sums


def part_2(lines):
    time = int(lines[0].replace(" ", "")[5:])
    distance = int(lines[1].replace(" ", "")[9:])
    times_we_beat_the_highscore = 0
    for time_charging in range(1, time):
        # Go through all the times we can charge and see if we beat the highscore
        distance_covered = time_charging * (time-time_charging)
        if distance_covered > distance:
            times_we_beat_the_highscore += 1
    return times_we_beat_the_highscore


if __name__ == "__main__":
    with open("testing") as f:
        lines = [x.strip() for x in f.readlines()]
    print(part_1(lines))
    print(part_2(lines))
