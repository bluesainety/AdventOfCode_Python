import sys
from enum import Enum


class Direction(Enum):
    Start = 0
    Left = 1
    Down = 2
    Right = 3
    Up = 4


def opposite(direction: Direction) -> Direction:
    if direction == Direction.Up:
        return Direction.Down
    if direction == Direction.Down:
        return direction.Up
    if direction == Direction.Left:
        return direction.Right
    if direction == Direction.Right:
        return direction.Left


def f_j_corner(direction: Direction):
    if direction == Direction.Left:
        return Direction.Up
    if direction == Direction.Right:
        return Direction.Down
    if direction == Direction.Up:
        return Direction.Left
    if direction == Direction.Down:
        return Direction.Right
    return None


def l_7_corner(direction: Direction):
    if direction == Direction.Left:
        return Direction.Down
    if direction == Direction.Right:
        return Direction.Up
    if direction == Direction.Up:
        return Direction.Right
    if direction == Direction.Down:
        return Direction.Left
    return None


class Pipe:
    start = False
    index_x = 0
    index_y = 0
    inner_direction = None
    outer_direction = None

    def set_inner_outer_prev(self, prev_inner, prev_outer):
        if prev_inner is None:
            self.inner_direction = Direction.Up
            self.outer_direction = Direction.Down
            return

        self.inner_direction = prev_inner
        self.outer_direction = prev_outer

    def get_inner(self):
        return self.inner_direction

    def get_outer(self):
        return self.outer_direction

    def get_x(self):
        return self.index_x

    def get_y(self):
        return self.index_y

    def has_direction(self, direction: Direction) -> bool:
        return direction in self.directions

    def is_start(self):
        return self.start

    def attaches(self, other, direction: Direction) -> bool:
        if direction in self.directions and other.has_direction(opposite(direction)):
            return True
        return False

    def __init__(self, id, x, y):
        self.id = id
        self.index_x = x
        self.index_y = y
        if id == 'S':
            self.start = True

        self.directions = []

        if id == 'S' or id == '┌' or id == '│' or id == '┐':
            self.directions.append(Direction.Down)
        if id == 'S' or id == '└' or id == '┘' or id == '│':
            self.directions.append(Direction.Up)
        if id == 'S' or id == '─' or id == '┘' or id == '┐':
            self.directions.append(Direction.Left)
        if id == 'S' or id == '─' or id == '┌' or id == '└':
            self.directions.append(Direction.Right)

    def __str__(self):
        return f"[{self.id}, {self.directions}]"

    def __repr__(self):
        return f"[{self.id}, {self.directions}]"


def parse_input(file_path) -> list[list[Pipe]]:
    parsedLines = []

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            parsedLines.append(line.strip())

    matrix = []

    for y, line in enumerate(parsedLines):
        output = []

        for x, char in enumerate(line):
            if char == 'J':
                char =  "┘"
            if char == '7':
                char = '┐'
            if char == 'L':
                char = '└'
            if char == 'F':
                char = '┌'
            if char == '-':
                char = '─'
            if char == '|':
                char = '│'
            output.append(Pipe(char, x, y))

        matrix.append(output)

    return matrix


def find_start(pipes: list[list[Pipe]]) -> (int, int, Pipe):
    start, row, column = None, None, None
    for i, line in enumerate(pipes):
        if start is not None:
            break
        for j, x in enumerate(line):
            if x.is_start():
                start, row, column = x, i, j
                break

    return row, column, start


def find_next_paths(i: int, j: int, pipes: list[list[Pipe]], skip: Direction) -> list[Direction]:
    directions = []

    if skip != Direction.Right and j < (len(pipes[i]) - 1) \
            and pipes[i][j].attaches(pipes[i][j + 1], Direction.Right):
        directions.append(Direction.Right)

    if skip != Direction.Left and j > 0 \
            and pipes[i][j].attaches(pipes[i][j - 1], Direction.Left):
        directions.append(Direction.Left)

    if skip != Direction.Down and i < (len(pipes) - 1) \
            and pipes[i][j].attaches(pipes[i + 1][j], Direction.Down):
        directions.append(Direction.Down)

    if skip != Direction.Up and i > 0 \
            and pipes[i][j].attaches(pipes[i - 1][j], Direction.Up):
        directions.append(Direction.Up)

    return directions


def follow_path(i: int, j: int, pipes: list[list[Pipe]], path: list[Pipe], coming_from: Direction) -> list[Pipe]:
    path.append(pipes[i][j])

    if coming_from != Direction.Start and path[-1].id == "S":
        return path

    next_paths = find_next_paths(i, j, pipes, coming_from)

    for direction in next_paths:
        _i, _j = i, j
        if direction == Direction.Left:
            _j -= 1
        elif direction == Direction.Right:
            _j += 1
        elif direction == Direction.Up:
            _i -= 1
        elif direction == Direction.Down:
            _i += 1

        result = follow_path(_i, _j, pipes, path, opposite(direction))

        if result:
            return result

    return []


def in_direction(direction: Direction, x, y) -> (int, int):
    if direction == Direction.Left:
        return x - 1, y
    elif direction == Direction.Right:
        return x + 1, y
    elif direction == Direction.Up:
        return x, y - 1
    elif direction == Direction.Down:
        return x, y + 1


def draw(loop: list[Pipe]):
    has_loop_matrix = [[" " for i in range(0, 141)] for j in range(0, 141)]

    for counter, node in enumerate(loop):
        if node.is_start():
            has_loop_matrix[node.get_y()][node.get_x()] = "S"

        else:
            has_loop_matrix[node.get_y()][node.get_x()] = node.id
            x, y = in_direction(node.get_inner(), node.get_x(), node.get_y())
            if has_loop_matrix[y][x] == " ":
                has_loop_matrix[y][x] = "."

    inner_count = 0

    for j, line in enumerate(has_loop_matrix):
        line_copy = []
        for i, char in enumerate(line):
            if char != " ":
                line_copy.append(char)
            elif char == ".":
                line_copy.append(char)
            elif 0 < i < (len(line) - 1) and (line_copy[-1] == "." or line[i + 1] == "." or line[i - 1] == "."):
                line_copy.append(".")
            elif i == 0 and line[i + 1] == ".":
                line_copy.append(".")
            elif i == (len(line) - 1) and (line_copy[-1] == "." or line[i - 1] == "."):
                line_copy.append(".")
            elif 0 < j < (len(line) - 1) and (has_loop_matrix[j + 1][i] == "." or has_loop_matrix[j - 1][i] == "."):
                line_copy.append(".")
            else:
                line_copy.append(char)

        inner_count += line_copy.count(".")
        print(f"{''.join(line_copy)}")

    print(inner_count)


def add_directions(loop: list[Pipe]):
    cntr = 0

    while cntr < len(loop) - 1:
        current_node = loop[cntr]

        if current_node.id == 'S':
            current_node.set_inner_outer_prev(None, None)
            cntr += 1
            continue

        prev_inner = loop[cntr-1].get_inner()
        prev_outer = loop[cntr-1].get_outer()

        if current_node.id == '─' or current_node.id == '│':
            loop[cntr].set_inner_outer_prev(prev_inner, prev_outer)

        elif current_node.id == '┌' or current_node.id == '┘':
            current_node.set_inner_outer_prev(f_j_corner(prev_inner), f_j_corner(prev_outer))
        elif current_node.id == '└' or current_node.id == '┐':
            current_node.set_inner_outer_prev(l_7_corner(prev_inner), l_7_corner(prev_outer))

        cntr += 1


# Implementation has a mistake; certain inner squares are ignored if they are surrounded by corners & the loop
# is going in the 'wrong' direction, as corners should technically have two inner / outer directions instead of one.
# However, I don't feel like changing the entire implementation of this at the moment, so be warned that the result
# may be inaccurate.
def main():
    sys.setrecursionlimit(20000)
    pipes = parse_input("Inputs/Day10.txt")

    row, column, start = find_start(pipes)
    loop = follow_path(row, column, pipes, [], Direction.Start)

    print(f"{int(len(loop) / 2)}")
    add_directions(loop)
    draw(loop)


if __name__ == "__main__":
    main()