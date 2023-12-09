from helper.file_handler import *

digitsToFind = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9]]
inputLines = readLinesFromFile("Inputs/Day1.txt")

def sumOfLines(linesToSum):
    sum = 0
    for line in linesToSum:
        digits = []

        for char in line:
            if char in "1234567890":
                digits.append(char)

        if len(digits) > 1:
            toAdd = digits[0] + digits[-1]
        elif len(digits) == 1:
            toAdd = digits[0] + digits[0]
        else:
            toAdd = '0'

        sum += int(toAdd)

    print(sum)

def numbersPerLine(linesToProcess):
    updatedInputLines = []

    for line in linesToProcess:
        counter = 0
        digitsInLine = []
        testingLine = line
        while counter <= len(testingLine):
            counter += 1
            for subLine in range(0, len(testingLine)):
                found = False
                for tests in digitsToFind:
                    if tests[0] in testingLine[:subLine] or str(tests[1]) in testingLine[:subLine]:
                        testingLine = testingLine[subLine:]
                        digitsInLine.append(tests[1])
                        found = True
                        break
                if found:
                    break

        updatedInputLines.append(str(digitsInLine))

    return updatedInputLines

sumOfLines(inputLines)
sumOfLines(numbersPerLine(inputLines))