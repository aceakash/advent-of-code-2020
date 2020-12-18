def parseInput(filePath):
    file = open(filePath, 'r')
    lines = file.readlines()
    file.close()
    return [line.strip() for line in lines]


def toBinary(boardingPass, zeroBitChar):
    chars = ['0' if c == zeroBitChar else '1'
             for c in boardingPass]
    return int(''.join(chars), 2)


def getRowAndColumn(boardingPass):
    row = toBinary(boardingPass[:7], 'F')
    col = toBinary(boardingPass[7:], 'L')
    return (row, col)


def getAllSeatNumbers(boardingPasses):
    binaryBoardingPasses = [getRowAndColumn(bp) for bp in boardingPasses]
    return [r*8+c for (r, c) in binaryBoardingPasses]


def fivePointOne():
    boardingPasses = parseInput('./5.input.txt')
    return max(getAllSeatNumbers(boardingPasses))


def fivePointTwo():
    boardingPasses = parseInput('./5.input.txt')
    allotedSeats = getAllSeatNumbers(boardingPasses)
    allPossibleSeats = [*range(min(allotedSeats), max(allotedSeats)+1)]
    return set(allPossibleSeats)-set(allotedSeats)


print(fivePointOne())
print(fivePointTwo())
