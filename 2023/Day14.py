from itertools import dropwhile

from helper.Direction import Direction
import numpy as np

from helper import file_handler as fh


def slide(line: []):
    sections = "".join(line).split("#")
    slide_result = ""

    for section in sections:
        mirror_count = section.count('O')
        slide_result += "".join(["O" * mirror_count])
        slide_result += "".join(["." * (len(section) - mirror_count)])
        slide_result += "#"

    return slide_result[:-1]


def weight(line: str):
    weight = [len(line) - i for i, char in enumerate(line) if char == "O"]
    return sum(*[weight])


def slide_in_direction(platform: np.ndarray, dir: Direction) -> np.ndarray:
    result = []

    if dir == Direction.North or dir == Direction.South:
        platform = platform.T

    shape = platform.shape

    for line in platform:
        if dir == Direction.West or dir == Direction.North:
            result += [char for char in slide(line.tolist())]
        else:
            rev = line.tolist()
            rev.reverse()
            result += [char for char in slide(rev)][::-1]

    platform = np.reshape(np.array(result), shape)

    if dir == Direction.North or dir == Direction.South:
        platform = platform.T

    return platform

def cycle(platform):
    platform = slide_in_direction(platform, Direction.North)
    platform = slide_in_direction(platform, Direction.West)
    platform = slide_in_direction(platform, Direction.South)
    platform = slide_in_direction(platform, Direction.East)

    return platform


def total_weight(platform):
    total2 = 0

    for line in platform:
        total2 += weight(line)

    return total2


def main():
    platform = fh.readFileAsMatrix("Inputs/Day14.txt", True)
    rotate = platform.T

    total = 0

    for line in rotate:
        slide_result = slide(line.tolist())
        total += weight(slide_result)

    counter = 1
    platforms_as_bytes = []
    weights = []

    while True:
        platform = cycle(platform)
        comparer = platform.tobytes()

        if comparer in platforms_as_bytes:
            cycle_length: int = counter - platforms_as_bytes.index(comparer) - 1
            weights.append(total_weight(platform.T))
            for i in range(0, cycle_length):
                platform = cycle(platform)
                weights.append(total_weight(platform.T))
            break

        print(f"{counter} - weight: {total_weight(platform.T)}")
        weights.append(total_weight(platform.T))
        platforms_as_bytes.append(comparer)

        counter += 1

    counter = counter - 1

    # the ugliest shit:
    store = (1_000_000_000 - counter)
    print(f"{store} - {cycle_length} - {999999839 % 42} - {store % cycle_length}")
    print(counter + ((1_000_000_000 - counter) % cycle_length) - 1)
    print(f"The answer to part 1 is: {total}")
    print(f"The answer to part 2 is: {weights[counter + ((1_000_000_000 - counter) % cycle_length) - 1]}")


if __name__ == "__main__":
    main()