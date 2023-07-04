import re
test_input_text = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

X = 0
Y = 1
LOWER = 0
UPPER = 1


class Sensor:
    def __init__(self, my_position: tuple[int, int], closest_beacon_position: tuple[int, int]):
        self.position = my_position
        self.closest_beacon_position = closest_beacon_position

    def exclusion_radius(self):
        return abs(self.position[X] - self.closest_beacon_position[X]) +\
            abs(self.position[Y] - self.closest_beacon_position[Y])

    def exclusion_range(self, row: int) -> tuple[int, int]:
        er = self.exclusion_radius()
        vert_dist = abs(self.position[Y] - row)
        horz_remaining = er - vert_dist
        if horz_remaining < 0:
            return None
        return (self.position[X] - horz_remaining, self.position[X] + horz_remaining)

    def __repr__(self):
        return "Sensor(pos %d, %d, cb %d, %d, er %d)" % (self.position[X],
                                                        self.position[Y],
                                                        self.closest_beacon_position[X],
                                                        self.closest_beacon_position[Y],
                                                        self.exclusion_radius()
                                                        )


assert Sensor((8, 7), (2, 10)).exclusion_radius() == 9
assert not Sensor((8, 7), (2, 10)).exclusion_range(-3)
assert Sensor((8, 7), (2, 10)).exclusion_range(-2) == (8, 8)
assert Sensor((8, 7), (2, 10)).exclusion_range(-1) == (7, 9)
assert Sensor((8, 7), (2, 10)).exclusion_range(7) == (-1, 17)
assert Sensor((8, 7), (2, 10)).exclusion_range(8) == (0, 16)
assert Sensor((8, 7), (2, 10)).exclusion_range(16) == (8, 8)
assert not Sensor((8, 7), (2, 10)).exclusion_range(17)


def parse_line(text: str) -> Sensor:
    parse_pattern = "^Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)$"
    matches = re.findall(parse_pattern, text)
    assert len(matches) == 1
    assert len(matches[0]) == 4
    coordinates = [int(x) for x in matches[0]]
    return Sensor((coordinates[0], coordinates[1]), (coordinates[2], coordinates[3]))


def parse_text(text: str) -> list[Sensor]:
    return [parse_line(line) for line in text.split("\n") if line.strip() != ""]


def condense_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    working_set = [ _ for _ in ranges if _ ]
    eliminate_range = None
    eliminated_something = True
    while eliminated_something:
        eliminated_something = False
        for index1, range1 in enumerate(working_set):
            for index2, range2 in enumerate(working_set):
                if index1 != index2:

                    if range1[LOWER] <= range2[LOWER] <= range2[UPPER] <= range1[UPPER]:
                        #range1 encapsulates range2 -> delete range2
                        eliminate_range = index2
                        eliminated_something = True
                        break
                    if range2[LOWER] <= range1[LOWER] <= range1[UPPER] <= range2[UPPER]:
                        # range2 encapsulates range1 -> delete range1
                        eliminate_range = index1
                        eliminated_something = True
                        break
                    if range1[LOWER] <= range2[LOWER] <= range1[UPPER] <= range2[UPPER]:
                        # ranges overlap, extent is 1 lower to 2 upper -> fix range1 and delete range2
                        working_set[index1] = (range1[LOWER], range2[UPPER])
                        eliminate_range = index2
                        eliminated_something = True
                        break
                    if range2[LOWER] <= range1[LOWER] <= range2[UPPER] <= range1[UPPER]:
                        # ranges overlap, extent is 2 lower to 1 upper -> fix range1 and delete range2
                        working_set[index1] = (range2[LOWER], range1[UPPER])
                        eliminate_range = index2
                        eliminated_something = True
                        break
                    if range1[UPPER] + 1 == range2[LOWER]:
                        # ranges exactly touch, extent is 1 lower to 2 upper -> fix range1 and delete range2
                        working_set[index1] = (range1[LOWER], range2[UPPER])
                        eliminate_range = index2
                        eliminated_something = True
                        break
                    if range2[UPPER] + 1 == range1[LOWER]:
                        # ranges exactly touch, extent is 2 lower to 1 upper -> fix range1 and delete range2
                        working_set[index1] = (range2[LOWER], range1[UPPER])
                        eliminate_range = index2
                        eliminated_something = True
                        break
            if eliminated_something:
                break
        if eliminated_something:
            del working_set[eliminate_range]
            eliminate_range = None
    return sorted(working_set, key=lambda x: x[0])


def count_excluded_positions(non_overlapping_exclusion_ranges: list[tuple[int, int]]) -> int:
    output = 0
    for index, excluded_range in enumerate(non_overlapping_exclusion_ranges):
        if index < len(non_overlapping_exclusion_ranges) -1:
            assert excluded_range[1] < non_overlapping_exclusion_ranges[index + 1][0]
        output += excluded_range[1] - excluded_range[0] + 1
    return output


def subtract_from_ranges(ranges: list[tuple[int, int]], to_subtract: list[int]) -> list[tuple[int, int]]:
    output = ranges.copy()
    for beacon_X in to_subtract:
        delete_range = False
        delete_index = None
        add_range = False
        new_range = None
        for index, range in enumerate(output):
            if beacon_X == range[LOWER] == range[UPPER]:
                delete_range = True
                delete_index = index
                break
            if beacon_X == range[LOWER]:
                output[index] = (range[LOWER] + 1, range[UPPER])
                break
            if beacon_X == range[UPPER]:
                output[index] = (range[LOWER], range[UPPER] - 1)
                break
            if range[LOWER] < beacon_X < range[UPPER]:
                output[index] = (range[LOWER], beacon_X - 1)
                add_range = True
                new_range = (beacon_X + 1, range[UPPER])
                break
        if delete_range:
            del output[delete_index]
            delete_index = None
            delete_range = False
        if add_range:
            output.append(new_range)
            new_range = None
            add_range = False
    return output

def count_excluded_positions_in_row(sensors: list[Sensor], row: int) -> int:
    exclusion_ranges = condense_ranges([sensor.exclusion_range(row) for sensor in sensors])
    beacons_in_row = [sensor.closest_beacon_position[X] for sensor in sensors if
                           sensor.closest_beacon_position[Y] == row]
    return count_excluded_positions(subtract_from_ranges(exclusion_ranges, beacons_in_row))


test_sensors = parse_text(test_input_text)
assert count_excluded_positions_in_row(test_sensors, 10) == 26

puzzle_input_text = """Sensor at x=3859432, y=2304903: closest beacon is at x=3677247, y=3140958
Sensor at x=2488890, y=2695345: closest beacon is at x=1934788, y=2667279
Sensor at x=3901948, y=701878: closest beacon is at x=4095477, y=368031
Sensor at x=2422190, y=1775708: closest beacon is at x=1765036, y=2000000
Sensor at x=2703846, y=3282799: closest beacon is at x=2121069, y=3230302
Sensor at x=172003, y=2579074: closest beacon is at x=-77667, y=3197309
Sensor at x=1813149, y=1311283: closest beacon is at x=1765036, y=2000000
Sensor at x=1704453, y=2468117: closest beacon is at x=1934788, y=2667279
Sensor at x=1927725, y=2976002: closest beacon is at x=1934788, y=2667279
Sensor at x=3176646, y=1254463: closest beacon is at x=2946873, y=2167634
Sensor at x=2149510, y=3722117: closest beacon is at x=2121069, y=3230302
Sensor at x=3804434, y=251015: closest beacon is at x=4095477, y=368031
Sensor at x=2613561, y=3932220: closest beacon is at x=2121069, y=3230302
Sensor at x=3997794, y=3291220: closest beacon is at x=3677247, y=3140958
Sensor at x=98328, y=3675176: closest beacon is at x=-77667, y=3197309
Sensor at x=2006541, y=2259601: closest beacon is at x=1934788, y=2667279
Sensor at x=663904, y=122919: closest beacon is at x=1618552, y=-433244
Sensor at x=1116472, y=3349728: closest beacon is at x=2121069, y=3230302
Sensor at x=2810797, y=2300748: closest beacon is at x=2946873, y=2167634
Sensor at x=1760767, y=2024355: closest beacon is at x=1765036, y=2000000
Sensor at x=3098487, y=2529092: closest beacon is at x=2946873, y=2167634
Sensor at x=1716839, y=634872: closest beacon is at x=1618552, y=-433244
Sensor at x=9323, y=979154: closest beacon is at x=-245599, y=778791
Sensor at x=1737623, y=2032367: closest beacon is at x=1765036, y=2000000
Sensor at x=26695, y=3049071: closest beacon is at x=-77667, y=3197309
Sensor at x=3691492, y=3766350: closest beacon is at x=3677247, y=3140958
Sensor at x=730556, y=1657010: closest beacon is at x=1765036, y=2000000
Sensor at x=506169, y=3958647: closest beacon is at x=-77667, y=3197309
Sensor at x=2728744, y=23398: closest beacon is at x=1618552, y=-433244
Sensor at x=3215227, y=3077078: closest beacon is at x=3677247, y=3140958
Sensor at x=2209379, y=3030851: closest beacon is at x=2121069, y=3230302"""

puzzle_sensors = parse_text(puzzle_input_text)
print("Part 1: excluded positions = %d" % count_excluded_positions_in_row(puzzle_sensors, 2000000))

def find_possible_ranges(sensors: list[Sensor], top: int, bottom: int, left: int, right:int) -> list[tuple[int, int]]:
    output = []
    for row in range(top, bottom+1):
        excluded_ranges = condense_ranges([x.exclusion_range(row) for x in sensors])
        if len(excluded_ranges) > 1:
            for index, excluded_range in enumerate(sorted(excluded_ranges[:-1])):
                for position in range(excluded_range[UPPER] + 1, excluded_ranges[index+1][LOWER]):
                    if left <= position <= right:
                        output.append((position, row))
        elif len(excluded_ranges) == 1:
            if excluded_ranges[0][LOWER] > left:
                for position in range(left, excluded_ranges[0][LOWER]):
                    if left <= position <= right:
                        output.append((position, row))
            if excluded_ranges[0][UPPER] < right:
                for position in range(excluded_ranges[0][LOWER] + 1, right + 1):
                    if left <= position <= right:
                        output.append((position, row))
    return output


def tuning_frequency(position: tuple[int, int], radix: int) -> int:
    return position[0] * radix + position[1]


test_possible_ranges = find_possible_ranges(test_sensors, 0, 20, 0, 20)
assert len(test_possible_ranges) == 1
assert test_possible_ranges[0] == (14, 11)
assert tuning_frequency(test_possible_ranges[0], 4000000) == 56000011

possible_ranges = find_possible_ranges(puzzle_sensors, 0, 4000000, 0, 4000000)
print()
assert len(possible_ranges) == 1
print("Part 2: tuning frequency = %d" % tuning_frequency(possible_ranges[0], 4000000))