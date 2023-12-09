from helper import file_handler as fh

cards = fh.readLinesFromFile("Inputs/Day4.txt")
winningNrPerLine = []
yourNrPerLine = []

for card in cards:
    splitCard = card.split('|')
    parsedNumbers = splitCard[0][10:].split(' ')
    winningNumbers = []
    for number in parsedNumbers:
        if number != '':
            winningNumbers.append(number)

    parsedNumbers2 = splitCard[1].split(' ')
    yourNumbers = []
    for number in parsedNumbers2:
        if number != '':
            yourNumbers.append(number)

    yourNrPerLine.append(yourNumbers)
    winningNrPerLine.append(winningNumbers)

matches = []


for x in range(len(yourNrPerLine)):
    matchNumbers = []

    for nr in yourNrPerLine[x]:
        if nr in winningNrPerLine[x]:
            matchNumbers.append(nr)

    matches.append(matchNumbers)

def part1():
    totalpoints = 0
    for match in matches:
        if len(match) == 0:
            continue;

        cardPoints = 1
        for i in range(len(match) - 1):
            cardPoints += cardPoints
        totalpoints += cardPoints

    print(totalpoints)

def getCopies(i:int):
    totalForCard = 1
    for x in range(len(matches[i])):
        totalForCard += getCopies(i + x + 1)

    return totalForCard

def part2():
    totalCopies = 0

    for i in range(len(matches)):
        totalCopies += getCopies(i)

    print(totalCopies)

part2()

