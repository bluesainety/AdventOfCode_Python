import numpy

from helper import file_handler as fh
import itertools


def fit(coded_groups, remainder):
    maxlen = len(coded_groups)+remainder
    opts = itertools.combinations(range(maxlen), len(coded_groups))

    options = []

    for opt in opts:
        match_string = ['.'] * maxlen
        for i, op in enumerate(opt):
                match_string[op] = coded_groups[i]
        options.append("".join(match_string))

    return options


def solve(puzzle, groups):
    puzzle_len = len(puzzle)
    group_len = sum([int(group) for group in groups]) + len(groups) - 1

    coded_groups = []

    for group in groups:
        coded_groups.append('#' * int(group))
        coded_groups.append('.')

    coded_groups.pop()

    options = fit(coded_groups, puzzle_len - group_len)

    solutions = []

    for option in options:
        if any(char for i, char in enumerate(option) if (char != puzzle[i] and puzzle[i] != '?')):
            continue
        solutions.append(option)

    solutions = numpy.unique(numpy.asarray(solutions))
    print(f"{puzzle} ({puzzle_len}) - {groups} ({group_len}) - {coded_groups} - {len(solutions)} solutions")

    return solutions


def main():
    lines = fh.readLinesFromFile("Inputs/Day12.txt", " ")
    counter = 0

    for line in lines:
        line[0] = line[0] * 5
        line[1] = line[1].split(',') * 5
        sol = solve(line[0], line[1])
        counter += len(sol)

    print(f"The answer to part 1 is: {counter}")


if __name__ == "__main__":
    main()