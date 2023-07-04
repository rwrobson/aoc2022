rock_paths_input_text = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

HORZ = 0
VERT = 1


class Coord:
    def __init__(self, coord):
        if type(coord) == str:
            coord_array = coord.split(",")
            assert len(coord_array) == 2
            coord_tuple = (int(coord_array[0]), int(coord_array[1]))
        elif type(coord) == list:
            assert len(coord) == 2
            coord_tuple = (coord[0], coord[1])
        elif type(coord) == tuple:
            coord_tuple = coord
            assert len(coord_tuple) == 2
        else:
            assert len(coord) == 2
            coord_tuple = tuple(coord)
        self.coord = coord_tuple

    def __add__(self, other):
        return Coord([self.coord[0] + other.coord[0], self.coord[1] + other.coord[1]])

    def __sub__(self, other):
        return Coord([self.coord[0] - other.coord[0], self.coord[1] - other.coord[1]])

    def length(self):
        return abs(self.coord[HORZ]) + abs(self.coord[VERT])

    def unit_step(self, index:int):
        def sign(i: int) -> int:
            if i > 0:
                return 1
            elif i < 0:
                return -1
            return 0

        return Coord([sign(self.coord[HORZ]) * index, sign(self.coord[VERT]) * index])

    def __str__(self):
        return "%d,%d" % (self.coord[HORZ], self.coord[VERT])

    def __lt__(self, other):
        if self.coord[0] == other.coord[0]:
            return self.coord[1] < other.coord[1]
        return self.coord[0] < other.coord[0]


def paths_to_coords(rock_paths_text: str) -> dict[str, Coord]:
    coord_paths = [[Coord(coord_string) for coord_string in line.strip().split(" -> ")] for line in rock_paths_text.split("\n") if line.strip() != ""]
    output = {}
    for coord_path in coord_paths:
        for vertex_index in range(len(coord_path)-1):
            edge = coord_path[vertex_index + 1] - coord_path[vertex_index]
            for step_num in range(edge.length()):
                step = coord_path[vertex_index] + edge.unit_step(step_num)
                output[str(step)] = step
        step = coord_path[-1]
        output[str(step)] = step
    return output


def extent(coord_dict: dict[str, Coord]) -> dict[str, int]:
    uninitialized = True
    top = bottom = left = right = None
    for coord_key in coord_dict:
        coord = coord_dict[coord_key].coord
        if uninitialized or coord[HORZ] < left:
            left = coord[HORZ]
        if uninitialized or coord[HORZ] > right:
            right = coord[HORZ]
        if uninitialized or coord[VERT] < top:
            top = coord[VERT]
        if uninitialized or coord[VERT] > bottom:
            bottom = coord[VERT]
        uninitialized = False
    return {"top": top, "bottom": bottom, "left": left, "right": right}


def render(content: dict[str, dict[str, Coord]]) -> list[str]:
    top = bottom = 0
    left = right = 500
    for pixel_char in content.keys():
        content_extent = extent(content[pixel_char])
        if content_extent["left"] < left:
            left = content_extent["left"]
        if content_extent["right"] > right:
            right = content_extent["right"]
        if content_extent["top"] < top:
            top = content_extent["top"]
        if content_extent["bottom"] > bottom:
            bottom = content_extent["bottom"]
    output = []
    for exponent in range(2, -1, -1):
        output_row = "    "
        for col in range(left, right + 1):
            output_char = " "
            power = 10 ** exponent
            if col == left or col == right or col == 500:
                output_char = str(col // power % 10)
            output_row += output_char
        output.append(output_row)
    for row in range(top, bottom + 1):
        output_row = "%03d " % row
        for col in range(left, right + 1):
            coord_key = "%d,%d" % (col, row)
            output_char = "."
            for pixel_char in content.keys():
                if coord_key in content[pixel_char]:
                    output_char = pixel_char
            if row == 0 and col == 500:
                output_char = "+"
            output_row += output_char
        output.append(output_row)
    return output


def collides(test_coord: Coord, content: dict[str, Coord]) -> bool:
    return str(test_coord) in content.keys()


rocks = paths_to_coords(rock_paths_input_text)


def capacity(obstacles: dict[str, Coord]) -> int:
    down = Coord((0, 1))
    down_right = Coord((1, 1))
    down_left = Coord((-1, 1))

    sand = {}

    units_sand_added = 0
    overflowing = False
    blocked = False
    while not overflowing and not blocked:
        falling_sand = Coord((500,0))
        falling = True
        while falling:
            if not collides(falling_sand + down, obstacles) and not collides(falling_sand + down, sand):
                falling_sand += down
            elif not collides(falling_sand + down_left, obstacles) and not collides(falling_sand + down_left, sand):
                falling_sand += down_left
            elif not collides(falling_sand + down_right, obstacles) and not collides(falling_sand + down_right, sand):
                falling_sand += down_right
            else:
                falling = False
            if falling_sand.coord[VERT] > 200:
                falling = False
                overflowing = True
        if falling_sand.coord[VERT] == 0:
            blocked = True
        if not overflowing:
            units_sand_added += 1
            sand[str(falling_sand)] = falling_sand
    print("\n".join(render({"#": obstacles, "o": sand})))
    return units_sand_added


part1_capacity = capacity(rocks)

print("Part 1:  %d units of sand were added before it started flowing into the abyss" % part1_capacity)

rock_extent = extent(rocks)

floor_path_string = "%d,%d -> %d, %d" % (rock_extent["left"] - rock_extent["bottom"], rock_extent["bottom"] + 2, rock_extent["right"] +  rock_extent["bottom"], rock_extent["bottom"] + 2)

floor = paths_to_coords(floor_path_string)

for coord_key in floor:
    rocks[coord_key] = floor[coord_key]

print("\n".join(render({"#": rocks})))

part2_capacity = capacity(rocks)

print("Part 2:  %d units of sand were added before the source became blocked" % part2_capacity)
