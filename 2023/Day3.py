from helper import file_handler as fh
import numpy as np

matrix = fh.readFileAsMatrix("Inputs/Day3.txt")
lineLength = len(matrix[0])
symbolsInMatrix = [[[False, ''] for i in range(len(matrix[0]))] for j in range(len(matrix))]
numbersInMatrix = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

for lineCounter in range(len(matrix)):
    for charCounter in range(lineLength):
        if matrix[lineCounter][charCounter] not in "1234567890.":
            symbolsInMatrix[lineCounter][charCounter] = [True, matrix[lineCounter][charCounter]]
    lineCounter += 1
    charCounter += 1

charCounter = 0

for lineCounter in range(len(matrix)):
    charCounter = 0
    while charCounter < lineLength:
        if matrix[lineCounter][charCounter] in "1234567890":
            digitCounter = 0
            digits = []
            while matrix[lineCounter][charCounter + digitCounter] in "1234567890":
                digit = matrix[lineCounter][charCounter + digitCounter]
                digits.append(digit)
                digitCounter += 1
                if charCounter + digitCounter > lineLength - 1:
                    break;

            for x in range(digitCounter):
                numbersInMatrix[lineCounter][charCounter+x] = [int("".join(digits)), x, digitCounter]

            charCounter += digitCounter
        else:
            charCounter += 1

def checkNeighbours(i, j, checkMatrix):
    if i != 0:
        if (j != 0 and checkMatrix[i-1][j - 1][0]) or checkMatrix[i-1][j][0] or (j != len(checkMatrix[0]) - 1 and checkMatrix[i-1][j + 1][0]):
            return True
    if i != len(checkMatrix) - 1:
        if (j != 0 and checkMatrix[i+1][j - 1][0]) or checkMatrix[i+1][j][0] or (j != len(checkMatrix[0]) - 1 and checkMatrix[i+1][j + 1][0]):
            return True
    if (j != 0 and checkMatrix[i][j - 1][0]) or (j != len(checkMatrix[0]) - 1 and checkMatrix[i][j + 1][0]):
        return True
    else:
        return False

def part1():
    digitsToSum = []
    for i in range(len(numbersInMatrix)):
        j = 0
        while j < lineLength:
            record = numbersInMatrix[i][j]
            if record is not None and checkNeighbours(i, j, symbolsInMatrix):
                digitsToSum.append(record[0])
                j += record[2] - record[1]
            else:
                j += 1

    print(digitsToSum)
    print(np.sum(digitsToSum))

def multNumberNeighbours(i, j, checkMatrix):

    numbersFound = []

    if i != 0 and j != 0 and checkMatrix[i-1][j-1] is not None:
        numbersFound.append(checkMatrix[i-1][j-1][0])
    if i != 0 and checkMatrix[i-1][j] is not None:
        numbersFound.append(checkMatrix[i - 1][j][0])
    if i != 0 and j != len(checkMatrix[0]) - 1 and checkMatrix[i-1][j + 1] is not None:
        numbersFound.append(checkMatrix[i - 1][j + 1][0])
    if i != len(checkMatrix) - 1 and j != 0 and checkMatrix[i+1][j - 1] is not None:
        numbersFound.append(checkMatrix[i + 1][j - 1][0])
    if i != len(checkMatrix) - 1 and checkMatrix[i+1][j] is not None:
        numbersFound.append(checkMatrix[i + 1][j][0])
    if i != len(checkMatrix) - 1 and j != len(checkMatrix[0]) - 1 and checkMatrix[i+1][j + 1] is not None:
        numbersFound.append(checkMatrix[i + 1][j + 1][0])
    if j != 0 and checkMatrix[i][j - 1] is not None:
        numbersFound.append(checkMatrix[i][j - 1][0])
    if j != len(checkMatrix[0]) - 1 and checkMatrix[i][j + 1] is not None:
        numbersFound.append(checkMatrix[i][j + 1][0])

    numbersFound = list(dict.fromkeys(numbersFound))

    if len(numbersFound) != 2:
        return 0

    return numbersFound[0]*numbersFound[1]


def part2():
    digitsToSum = []
    for i in range(len(symbolsInMatrix)):
        for j in range(len(symbolsInMatrix[0])):
            record = symbolsInMatrix[i][j]
            if record[1] is '*':
                digitsToSum.append(multNumberNeighbours(i, j, numbersInMatrix))

    print(digitsToSum)
    print(np.sum(digitsToSum))

part2()