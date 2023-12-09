from helper import file_handler as fh

lines = fh.readLinesFromFile("Inputs/2022Day3.txt")
duplicates = []

def partOne(lines):
    for line in lines:
        firsthalf = line[:len(line)//2]
        secondhalf = line[len(line)//2:]

        for char in firsthalf:
            if char in secondhalf:
                duplicates.append(char)
                break;

def partTwo(lines):
    for x in range(int(len(lines)/3)):
        for char in lines[(x*3)]:
            if char in lines[(x*3)+1] and char in lines[(x*3)+2]:
                duplicates.append(char)
                break;

partTwo(lines)
priorities = 0

for duplicate in duplicates:
    priorities += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(duplicate) + 1

print(priorities)