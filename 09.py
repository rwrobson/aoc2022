motionsString = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

step_translation = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}

VERTICAL_INDEX = 0
HORIZONTAL_INDEX = 1

motions = [y.split(" ") for y in [ x.strip() for x in motionsString.split("\n") if x.strip() != ""]]

steps = []

for motion in motions:
    for step_count in range(int(motion[1])):
        steps.append(step_translation[motion[0]])


def solve_part09(rope_length):
    rope = [[0, 0] for i in range(rope_length)]

    def direction(some_int):
        if some_int > 0:
            return 1
        if some_int < 0:
            return -1
        return 0

    def pull_towards(lead_position, follow_position):
        vert_diff = lead_position[VERTICAL_INDEX] - follow_position[VERTICAL_INDEX]
        horz_diff = lead_position[HORIZONTAL_INDEX] - follow_position[HORIZONTAL_INDEX]
        vert_magn = int(abs(vert_diff))
        horz_magn = int(abs(horz_diff))
        vert_dir = direction(vert_diff)
        horz_dir = direction(horz_diff)
        if vert_magn > 1 or horz_magn > 1:
            return [follow_position[VERTICAL_INDEX] + vert_dir,
                               follow_position[HORIZONTAL_INDEX] + horz_dir]
        else:
            return follow_position

    unique_tail_positions = {}

    for step in steps:
        rope[0][VERTICAL_INDEX] += step[VERTICAL_INDEX]
        rope[0][HORIZONTAL_INDEX] += step[HORIZONTAL_INDEX]
        for rope_count in range(1, len(rope)):
            rope[rope_count] = pull_towards(rope[rope_count-1], rope[rope_count])
        if str(rope[-1]) in unique_tail_positions.keys():
            unique_tail_positions[str(rope[-1])] += 1
        else:
            unique_tail_positions[str(rope[-1])] = 1

    return len(unique_tail_positions)


print("Part 1:  A rope of length 2 passes through %d unique locations" % solve_part09(2))
print("Part 2:  A rope of length 10 passes through %d unique locations" % solve_part09(10))