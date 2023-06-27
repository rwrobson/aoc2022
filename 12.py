

input_elevation_map_alpha_string = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

ROW = 0
COL = 1

given_elevation_map_alpha = [x.strip() for x in input_elevation_map_alpha_string.split("\n") if not x.strip() == ""]

size = (len(given_elevation_map_alpha), len(given_elevation_map_alpha[0]))

given_start: (int, int) = (None, None)
given_end: (int, int) = (None, None)


def replace_char_in_string(string: str, pos: int, char: str) -> str:
    return string[:pos] + char + string[pos + 1:]


assert replace_char_in_string("flip", 2, "o") == "flop"

for row in range(size[ROW]):
    for col in range(size[COL]):
        if given_elevation_map_alpha[row][col] == "S":
            given_start = (row, col)
            given_elevation_map_alpha[row] = replace_char_in_string(given_elevation_map_alpha[row], col, "a")
        if given_elevation_map_alpha[row][col] == "E":
            given_end = (row, col)
            given_elevation_map_alpha[row] = replace_char_in_string(given_elevation_map_alpha[row], col, "z")

given_elevation_map = [[ord(y) - ord("a") for y in x.strip()] for x in given_elevation_map_alpha]


def find_shortest_path(elevation_map, start: (int, int), end: (int, int), climbing: bool) -> int:
    steps_to_reach: list[list[int | None]] = [[None for _ in range(size[COL])] for _ in range(size[ROW])]
    steps_to_reach[start[ROW]][start[COL]] = 0

    reached = [[False for _ in range(size[COL])] for _ in range(size[ROW])]
    reached[start[ROW]][start[COL]] = True

    def debug_print():
        for row in range(size[ROW]):
            output = ""
            for col in range(size[COL]):
                if row == start[ROW] and col == start[COL]:
                    output += "S"
                else:
                    if end and row == end[ROW] and col == end[COL]:
                        output += "E"
                    else:
                        if steps_to_reach[row][col]:
                            output += chr(ord("a") + steps_to_reach[row][col] - 1)
                        else:
                            output += "."
            print(output)

    stalled = False
    current_distance = 1
    if climbing:
        step_condition = lambda unreached_elevation, reached_elevation: unreached_elevation <= reached_elevation + 1
    else:
        step_condition = lambda unreached_elevation, reached_elevation: reached_elevation <= unreached_elevation + 1

    while not (end and reached[end[ROW]][end[COL]]) and not stalled:
        stalled = True
        for col in range(size[COL]):
            in_first_col = (col == 0)
            in_last_col = (col == size[COL] -1)
            for row in range(size[ROW]):
                in_first_row = (row == 0)
                in_last_row = (row == size[ROW] - 1)
                if row == 2 and col == 4:
                    pass
                if not reached[row][col]:
                    this_cell_elevation = elevation_map[row][col]
                    this_cell_now_reachable = False
                    if not in_first_col and steps_to_reach[row][col - 1] == current_distance - 1:
                        if step_condition(this_cell_elevation, elevation_map[row][col - 1]):
                            this_cell_now_reachable = True
                    if not in_last_col and steps_to_reach[row][col + 1] == current_distance - 1:
                        if step_condition(this_cell_elevation, elevation_map[row][col + 1]):
                            this_cell_now_reachable = True
                    if not in_first_row and steps_to_reach[row - 1][col] == current_distance - 1:
                        if step_condition(this_cell_elevation, elevation_map[row - 1][col]):
                            this_cell_now_reachable = True
                    if not in_last_row and steps_to_reach[row + 1][col] == current_distance - 1:
                        if step_condition(this_cell_elevation, elevation_map[row + 1][col]):
                            this_cell_now_reachable = True
                    if this_cell_now_reachable:
                        steps_to_reach[row][col] = current_distance
                        reached[row][col] = True
                        stalled = False
                        if not climbing and elevation_map[row][col] == 0:
                            end = (row, col)
        current_distance += 1
    if end:
       return steps_to_reach[end[ROW]][end[COL]]

print("Part 1: Fewest steps to reach = %d" % find_shortest_path(given_elevation_map, given_start, given_end, True))
print("Part 2: Fewest steps to reach = %d" % find_shortest_path(given_elevation_map, given_end, None, False))


