from enum import Enum
from helper import file_handler as fh

class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

games = fh.readLinesFromFile("Inputs/2022Day2.txt")
gameResults = []
gameChoices = []
totalScore = 0

for game in games:
    choices = game.split(' ')
    enumChoices = []

    if choices[0] == 'A':
        enumChoices.append(Choice.ROCK)
        if choices[1] == 'Z':
            enumChoices.append(Choice.PAPER)
            gameResults.append(Result.WIN)
        elif choices[1] == 'Y':
            enumChoices.append(Choice.ROCK)
            gameResults.append(Result.DRAW)
        elif choices[1] == 'X':
            enumChoices.append(Choice.SCISSORS)
            gameResults.append(Result.LOSE)
    elif choices[0] == 'B':
        enumChoices.append(Choice.PAPER)
        if choices[1] == 'Y':
            enumChoices.append(Choice.PAPER)
            gameResults.append(Result.DRAW)
        elif choices[1] == 'X':
            enumChoices.append(Choice.ROCK)
            gameResults.append(Result.LOSE)
        elif choices[1] == 'Z':
            enumChoices.append(Choice.SCISSORS)
            gameResults.append(Result.WIN)
    elif choices[0] == 'C':
        enumChoices.append(Choice.SCISSORS)
        if choices[1] == 'X':
            enumChoices.append(Choice.PAPER)
            gameResults.append(Result.LOSE)
        elif choices[1] == 'Z':
            enumChoices.append(Choice.ROCK)
            gameResults.append(Result.WIN)
        elif choices[1] == 'Y':
            enumChoices.append(Choice.SCISSORS)
            gameResults.append(Result.DRAW)

    gameChoices.append(enumChoices)

for result in gameResults:
    totalScore += result.value

for choice in gameChoices:
    totalScore += choice[1].value

print(totalScore)


