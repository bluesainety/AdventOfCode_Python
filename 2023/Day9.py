from helper import file_handler as fh


def find_next_in_sequence(sec: [], to_sum: [], reverse=False) -> int:
    if len(sec) == 0 or all([s == 0 for s in sec]):
        return 0 if reverse else sum(to_sum)

    to_sum.append(sec[-1])
    sec_of_differences = []

    for i, s in enumerate(sec):
        if i == len(sec) - 1:
            break
        sec_of_differences.append(sec[i + 1] - s)

    next_in_sequence = find_next_in_sequence(sec_of_differences, to_sum, reverse)
    return (sec[0] - next_in_sequence) if reverse else next_in_sequence


def main():
    sequences = fh.readLinesFromFile("Inputs/Day9.txt", ' ', convert_to_int=True)
    result = 0

    for s in sequences:
        result += find_next_in_sequence(s, [], reverse=True)

    print(result)


if __name__ == "__main__":
    main()
