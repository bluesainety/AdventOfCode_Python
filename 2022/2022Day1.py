from helper import file_handler as fh
import numpy as np

lines = fh.readLinesFromFile("Inputs/2022Day1.txt")
print(lines)

def caloriesPerElf(lines):
    calorieBuffer = []
    calorieSums = []

    for line in lines:
        if line == '':
            calorieSums.append(np.sum(calorieBuffer))
            calorieBuffer = []
        else:
            calorieBuffer.append(int(line))

    return calorieSums

output = caloriesPerElf(lines)
maxCalories = np.max(output)

print(maxCalories)

sortedOutput = np.sort(output)

topThree = sortedOutput[-1] + sortedOutput[-2] + sortedOutput[-3]

print(sortedOutput)
print(topThree)
