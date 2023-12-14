from enum import Enum
import numpy as np

def read_sets_from_file(file_path, split_at = None, convert_to_int = False):
    parsedLines = []

    set = []

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                parsedLines.append(set)
                set = []
                continue
            if split_at is not None:
                line = line.split(split_at)
            if convert_to_int:
                line = [int(item) for item in line]

            set.append(line)
        parsedLines.append(set)

    return parsedLines

class Axis(Enum):
    Horizontal = 0
    Vertical = 1


def locate_reflection_line(np_set, ignore):
    for line in range(1, len(np_set)):
        if ignore is not None and ignore == line:
            continue

        first_half = np_set[:line]
        first_half = first_half[::-1]
        second_half = np_set[line:]

        if len(first_half) >= len(second_half):
            if all(all(x == y for x, y in zip(pattern, first_half[i])) for i, pattern in enumerate(second_half)):
                return line
        else:
            if all(all(x == y for x, y in zip(pattern, second_half[i])) for i, pattern in enumerate(first_half)):
                return line

    return None


def find_mirror(np_set, ignore = None) -> (Axis, int):
    result = locate_reflection_line(np_set, ignore[1] if ignore is not None and ignore[0] == Axis.Horizontal else None)
    if result is not None and result != ignore:
        return Axis.Horizontal, result

    np_transposed = np.transpose(np_set)

    result = locate_reflection_line(np_transposed, ignore[1] if ignore is not None and ignore[0] == Axis.Vertical else None)
    if result is not None and result != ignore:
        return Axis.Vertical, result

    return None

def flip(char):
    return '#' if char == '.' else '.'


def iter_set(np_set, default_result):
    for i, row in enumerate(np_set):
        for j, char in enumerate(row):
            np_set[i][j] = flip(np_set[i][j])
            new_result = find_mirror(np_set, default_result)
            if new_result is not None and new_result != default_result:
                return new_result[1] if new_result[0] == Axis.Vertical else 100 * new_result[1]
            np_set[i][j] = flip(np_set[i][j])


def main():
    patterns = read_sets_from_file("Day13.txt")
    total = 0
    total2 = 0

    for pattern in patterns:
        np_set = np.array([[char for char in item] for item in pattern])
        default_pattern = find_mirror(np_set)
        total += default_pattern[1] if default_pattern[0] == Axis.Vertical else 100 * default_pattern[1]
        total2 += iter_set(np_set, default_pattern)

    print(f"The answer to part 1 is: {total}")
    print(f"The answer to part 2 is: {total2}")


if __name__ == "__main__":
    main()