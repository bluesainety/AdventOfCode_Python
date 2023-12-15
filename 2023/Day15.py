from helper import file_handler as fh


def hash_step(current, val):
    current = current + ord(val) % 256
    current = current * 17 % 256
    return current


def hash(step):
    current = 0
    for val in step:
        current = hash_step(current, val)
    return current


def part1(instruction):
    total = 0

    for step in instruction:
        total += hash(step)

    print(f"The answer to part 1 is: {total}")


def to_hashmap(instructions, hashmap: dict):
    for step in instructions:
        delimiter = step.index('=') if '=' in step else step.index('-')
        label = step[:delimiter]
        box = hash(label)

        if step[delimiter] == "=":
            lens = step[-1]

            if box not in hashmap:
                hashmap[box] = []

            if label not in [lab for lab, _ in hashmap[box]]:
                hashmap[box].append((label, lens))
            else:
                to_update = next((lab, y) for lab, y in hashmap[box] if lab == label)
                index = hashmap[box].index(to_update)
                hashmap[box][index] = (label, lens)

        elif step[delimiter] == '-':
            if box not in hashmap:
                continue

            if label in [lab for lab, _ in hashmap[box]]:
                to_delete = next((lab, y) for lab, y in hashmap[box] if lab == label)
                hashmap[box].remove(to_delete)
    return hashmap


def focusing_power(hashmap: dict):
    total_power = 0

    for box, content in hashmap.items():
        box_power = 0
        for i, item in enumerate(content):
            box_power += ((box + 1) * (i + 1) * int(item[1]))
        total_power += box_power

    return total_power


def part2(instructions):
    hashmap = {}
    hashmap = to_hashmap(instructions, hashmap)
    print(f"The result of part 2 is: {focusing_power(hashmap)}")


def main():
    instructions = fh.readLinesFromFile("Inputs/Day15.txt", split_at=",")[0]
    part1(instructions)
    part2(instructions)


if __name__ == "__main__":
    main()