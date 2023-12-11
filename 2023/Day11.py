import numpy as np
from helper import file_handler as fh

def readFile(filepath):
    lines = fh.readFileAsMatrix(filepath)

    np_lines = np.asarray(lines)
    horizontal = 0
    vertical = 0

    for i, line in enumerate(lines):
        if all(char == '.' for char in line):
            np_lines = np.insert(np_lines, i + horizontal, '.', axis=0)
            horizontal += 1

    for i, column in enumerate(lines[0]):
        if all(line[i] == '.' for line in lines):
            np_lines = np.insert(np_lines, i + vertical, '.', axis=1)
            vertical += 1

    print(np_lines)
    return np_lines

def readFilePart2(filepath):
    lines = fh.readFileAsMatrix(filepath)
    np_lines = np.asarray(lines)

    for i, line in enumerate(lines):
        if all(char == '.' for char in line):
            np_lines[i] = '$'

    for i, column in enumerate(lines[0]):
        if all(line[i] == '.' for line in lines):
            np_lines[:, i] = '$'

    print(np_lines)
    return np_lines

def distance_to(me: (int, int), others: list[(int, int)], universe, extra = 1):
    distances = 0

    for other in others:
        #print(f"\nMatrix for {me} to {other}:")
        matrix_top_left = min(me[0], other[0])
        matrix_top_right = min(me[0], other[0]) + abs(me[0] - other [0]) + 1
        matrix_bottom_left = min(me[1], other[1])
        matrix_bottom_right = min(me[1], other[1]) + abs(me[1] - other [1]) + 1
        sub_matrix = universe[matrix_top_left:matrix_top_right, matrix_bottom_left:matrix_bottom_right]
        #print(sub_matrix)

        amount_of_extras = np.count_nonzero(sub_matrix[0, :] == '$') + np.count_nonzero(sub_matrix[:, 0] == '$')
        dist = np.absolute(np.subtract(me, other))
        dist = np.int64(dist)
        #print(f"Amount of $ found: {amount_of_extras}, starting distance {np.sum(dist)}, distance after adding " +
              #f"{np.sum(dist) - amount_of_extras + (extra*amount_of_extras)}")

        distances += (np.sum(dist) - amount_of_extras + (extra*amount_of_extras))

    return distances


def main():
    universe = readFilePart2("Inputs/Day11.txt")
    galaxies = []

    for i, row in enumerate(universe):
        for j, column in enumerate(row):
            if column == "#":
                galaxies.append((i, j))

    print(galaxies)
    distances = 0

    while len(galaxies) != 1:
        this_galaxy = galaxies[0]
        distances += distance_to(this_galaxy, galaxies[1:], universe, 1000000)
        galaxies.pop(0)

    print(f"The answer to part 2 is: {distances}")




if __name__ == "__main__":
    main()