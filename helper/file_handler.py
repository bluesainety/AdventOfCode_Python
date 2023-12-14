# file_handler.py>

import numpy as np

def readLinesFromFile(file_path, split_at = None, remove_empty = False, convert_to_int = False):
    parsedLines = []

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if remove_empty and line == "":
                continue;
            if split_at is not None:
                line = line.split(split_at)
            if convert_to_int:
                line = [int(item) for item in line]

            parsedLines.append(line)

    return parsedLines


def readFileAsMatrix(file_path, numpy = False):
    parsedLines = []

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            parsedLines.append(line.strip())

    matrix = []

    for line in parsedLines:
        matrix.append(np.array([char for char in line]) if numpy else [char for char in line])

    return np.array(matrix) if numpy else matrix
