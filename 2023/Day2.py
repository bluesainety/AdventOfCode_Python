from helper import file_handler as fh

def maxCubesPerGame(filePath):
    inputLines = fh.readLinesFromFile(filePath)
    games = []

    for line in inputLines:
        splitLine = line.split(': ')
        splitGames = splitLine[1].split('; ')

        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        for game in splitGames:
            draws = game.split(', ')
            for draw in draws:
                splitDraw = draw.split(' ')

                if splitDraw[1] == "red" and int(splitDraw[0]) > maxRed:
                    maxRed = int(splitDraw[0])
                elif splitDraw[1] == "green" and int(splitDraw[0]) > maxGreen:
                    maxGreen = int(splitDraw[0])
                elif splitDraw[1] == "blue" and int(splitDraw[0]) > maxBlue:
                    maxBlue = int(splitDraw[0])

        games.append([maxRed, maxGreen, maxBlue])

    return games

def challenge1(filepath):
    games = maxCubesPerGame(filepath)
    gameNr = 1
    gameSum = 0

    # 12 red cubes, 13 green cubes, and 14 blue cubes
    for game in games:
        if game[0] <= 12 and game[1] <= 13 and game[2] <= 14:
            gameSum += gameNr
        gameNr += 1

    print(gameSum)

def challenge2(filepath):
    games = maxCubesPerGame(filepath)
    gameSumOfPowers = 0

    for game in games:
        power = game[0]*game[1]*game[2]
        gameSumOfPowers += power

    print(gameSumOfPowers)


challenge1("Inputs/Day2")
challenge2("Inputs/Day2")