const treeCount = countTreesEncountered(getInput(), 3, 1)
console.log(treeCount)
const counts = [
    countTreesEncountered((getInput()), 1, 1),
    countTreesEncountered((getInput()), 3, 1),
    countTreesEncountered((getInput()), 5, 1),
    countTreesEncountered((getInput()), 7, 1),
    countTreesEncountered((getInput()), 1, 2)
]
console.log(counts.reduce((prev, curr) => prev*curr, 1))

type Position = {x: number, y: number}

function parseInput(input: string) {
    return input
        .trim()
        .split('\n')
        .map(line => line.trim().split('')
                        .map(c => c !== ".")
        )
}

function reachedTheBottom(theSlopes: boolean[][], pos: Position): boolean {
    return pos.y >= theSlopes.length
}

function moveBy(right: number, down: number, theSlopes: boolean[][], pos: Position) {
    return {...pos, x: pos.x + right, y: pos.y + down};
}

function isTree(theSlopes: boolean[][], pos: Position) {
    const sampleWidth = theSlopes[0].length
    return theSlopes[pos.y][pos.x % sampleWidth]
}

export function countTreesEncountered(input: string, slopeRight: number, slopeDown: number): number {
    const theSlopes = parseInput(input)

    let pos: Position = {x: 0, y: 0}
    let treeCount = 0
    while (!reachedTheBottom(theSlopes, pos)) {
        if (isTree(theSlopes, pos)) {
            treeCount++
        }
        pos = moveBy(slopeRight, slopeDown, theSlopes, pos)
    }

    return treeCount
}

function getInput() {
    return `...............#...#..#...#....
    ...#....##.....##...######..#..
    ....#.....#.##..#...#..#.......
    ...#..........#.#....#......#..
    ....#.#...#.#.......#......##.#
    ....#.#..........#.....#.##....
    ##...#.#.##......#......#.#.#..
    #.#.#........#....#..#.#.......
    ..#...##..#..#.......#....###..
    .#.#..........#...#........#..#
    .#..#......#....#.#...#...#.#.#
    ..#.........#..##.....#.#.##.#.
    .#......#...#....#.....#......#
    ........#..##..##.........#..#.
    .....#....###..#....##........#
    .###...#..##..#.##......##...##
    .#...#...#..#.#..#...##.....#..
    .......#....#....#.#...#.......
    .##.......#.##...#.#...#..#....
    #.#...#......#....#.......#....
    ..###...............####...#.#.
    .##.#....#......#..#...#.#..#.#
    .............#.#.#......##.....
    #....#.#.#........#....##...#..
    ...##....##...##..#...#........
    ..##......#...#......#...###...
    ...#...##......##.#.#..#.......
    #......#..#...#.#..#......#..##
    .#..#..#........##....##.......
    .#...........###.###.##...#....
    ............#.#...........#.#..
    #...#........#...#...#..#.#.#.#
    ...#.......#.#.#..#.#..........
    ......#..#..#....##..##..##....
    ........##...#......#..#.#.....
    ..#.#.......#......#...........
    #.#.....#......##..........#.#.
    #.....###.#...#...#..#....#...#
    .##.#...#............##.....#..
    ###....#.#.....#.......##......
    ##.......##.....#..#...#..##.##
    ....#.##............###...#..##
    .###..#...##.#..#..##..#.......
    .##.##..####.....#.........#...
    ....####..#...#....#.#...#.....
    ..##....#..#......#...........#
    ..........#......#..##.......#.
    .................#.#.#........#
    #.......##.#...##.......##.##..
    .#................#.#.....##..#
    ......#..#............##.#.....
    ...##............#.....#.....#.
    ##.###.#.......#....#.........#
    ......#.....#.#.#.#......#.....
    ......#.##......#......##......
    ..#....#...#..#.....#..#....#.#
    .#.##.##.....#.......#.......#.
    ...#..#.#......##....##..#.....
    .#.....#......##...#..#.#....#.
    ..#......#....#..#..###.#.#....
    .....#........#.#...#..#.#.....
    ....#.#.......#...##.....####..
    #..#..##...#...........#...#..#
    .#..#...#.....#.....#.#.....#.#
    ..##..###.....#...#.#.#.......#
    #..##.##......###..#......###..
    #..#...#.......#....#.#...#.#.#
    ...........###..#...#..##....#.
    .....#...........###.......#...
    ##......#.......#......##.#..#.
    #.................#........#...
    #.#.............#......#...#..#
    ......#.#....#....#....#....#.#
    ..#...#....#..#....#....#..#...
    #....#......#..#...#..#....#.#.
    ..#.....#..#...#...#.......#...
    .#........###..##.#..#.........
    .....##.#.....#..###..#........
    ...#...#.###....######......#..
    .###.#..#.....#.....#..#...#...
    ##..#.#......#.........#...#..#
    ###...##..###.......#..##.#.#.#
    .#...................#..#...##.
    .#...#...###...#.......#......#
    ....#.....##....#...##.#...#.##
    ..#....#......#...#..###.......
    .........#..........##........#
    ...#.........##..#....#..###...
    ......#.##....#.#........#.#.##
    ....#..#...#.............#....#
    #..#.....#.#.....#....#........
    ....#..#...####.#.###..#.......
    .....#....#....#..#..#.#.....#.
    #..##....#.....#.#.............
    .##...#..#.......#...##.###....
    ##......#...##....#......##....
    #......#.#......#.#..#......#..
    .#...#......#............###..#
    .#..#.#.....#.#.....#..#....#..
    .#............#...#..#..#...##.
    ...#...#....#.#.#....#....#....
    ........#......###.#....##.##.#
    ......#.#..................##..
    ..#..#........#..##..........##
    .#...#.#....#####.#.#..#.......
    .....#..#.#..#.....#.#........#
    #.#..#..#.#..........#..#..#...
    .##........#.#.......#........#
    .....#....#..##...#......##....
    ....#.##.##...##.#.........#.#.
    ...#...#..#.#.......#.......#..
    .................##..#.........
    ..##.##....#...#.##.......#..#.
    ....#...........#.....###....##
    .#..................#..........
    ....#.##....#......##.#..#.##.#
    #......#..#.#....##...####...#.
    #.....#.#.##...........#.##...#
    .......#...##..#.........##....
    .#...#..........##......#..#.#.
    #...#.#......#.....#........#..
    ........#.....#.......##......#
    .#..#...........#...#..#..#....
    ......#.##......##.#......#..##
    ......#....#..#................
    ##.#.......#......#..#....##.##
    ..#...###..#.......#...#.#....#
    .....#...#.........#.....#..#.#
    ..#.....#.........#..#...#.#...
    .#.........##..#.#...#.....##..
    ..........#.#.#...#....#....#..
    ....#.###.#..#..#..#.#........#
    ..#...##...##.#.#.....#.#..##..
    .#..#......#.####..#.......#..#
    ##.......#.....#.#.#..#...##..#
    .##......##...##.........#..#..
    ..#.##..#......#......#..#..#..
    ..#..#.##..#........#....#.#...
    ##.####...##.#..##.........#..#
    .#.......#.#..#.....#.##.......
    ........#.........#...........#
    ..#...#.####.....##.##.#....#.#
    .....#..##.#..###.##.#.#...#...
    #..##..##....#...#....#...#....
    .###.#....#..#.......#......###
    .#....##.....#.#........#...#.#
    #.#.#..#..#...#....#..#.....#..
    ....##...#.##..#............#..
    ##......###...#...#...#....#...
    #.#...#.#..#..##.##..##..#....#
    .#...#.#....#..##.#..##..#.....
    .............#..#..#.#.....#...
    #........#..........#....###...
    ..#..#......#...#........#.....
    .#..#.............#.........#..
    #.....#....##..#..#.#.#..#.....
    ...#......#.........#.#....##.#
    ..#.......##....###..#.........
    .#.......#......#..............
    .#...##.....##...###.#....#.#..
    ......#....#.........#.......#.
    ##.......#..##....###.#.....##.
    .....#......####.....#......#..
    ....#....#..###....#.....##...#
    ...#...#.#........#.....#..#.##
    #..#....#.#...###...##.....##..
    #.....##...#.#............#....
    ##....#.......#.#.#....#.#.###.
    #........#...#...####.#....#.#.
    .##.#......#........#..#.....#.
    ...##.#.......#...#.#.##..#...#
    ......#.........##..#....#.....
    .#......#...........#......#...
    ......#.#.#.#..#.#....#....#..#
    ##.................##...#.#....
    ........#.........#..#..#...###
    .#........#........#....#..#...
    ....###.##.##......#.#...#....#
    #......#.#..............#......
    .......#..#....#..##.........#.
    #............#....#............
    #...#.#.........##..###...##...
    .#....#.#.#.....#..#..##.......
    .............##.#.#.......#..#.
    #...#..##.#..###.....##..#.....
    ...#.#.....#...#......##.#..#..
    #..........#.##.#...#...#.#...#
    ...#.#...#.........#.#..#.#..#.
    #....#.................#.......
    ..#..#.#.#..#.#..##...#.#......
    ..#....#.#.#...#.....#...#.....
    #...#.###......#.......#..#..#.
    #.#.##.##..............#.#.#..#
    #..........#.#.........#.###...
    ...........#.......#.#..#......
    ....#.#..#....#....#....##.....
    #..#...##########.........#.#..
    ..#.............##........#.#..
    #.#.##......#...#.#....##..##..
    ..##..#.#.#....#......#.#..#.#.
    .#.#...#................#......
    #...#...#.....##.#...#.......#.
    .....##.......#...#......#.##..
    ....#.##..........#.#.##....##.
    ...........##........#.#.#.#...
    ..#...........###.#....#..#....
    ..#.#...#...#.#........#.....#.
    .##......##.....#........#.....
    ....#.......#....#...#.##...#..
    .#.....##.....#...##...........
    #....#.##.##...#...###.#####...
    ..#.#......#.#.......#....#..#.
    ..........#...#...........#....
    .........#..#...#...#......#.##
    .#...#.#...#.###.##..#........#
    #....#.....#.......##....#.....
    #.....#..#.....#...##.......#..
    #.#.#.#.............#.....#...#
    ...#.....#.....#...............
    ..##.###.#.#........#.........#
    ...##..#.##..#....#.#...#.#....
    ...##...#...##.#.........#.#..#
    .###......#....#.........#.#...
    ###.#.#...#.......#...#.....#.#
    ...#.#.......#.....####........
    ......#..#.....###.#....#..#...
    ..####...#...#..#......#...#...
    #..............##....#......##.
    ..##..###...##..#.#.........#..
    #..#.#...#.......#.........##..
    ..##....#......#...#..##.......
    ..#.#..#..###.....#.....#...###
    .#..#.##.....##.#.#.#........#.
    ..#.#.........#................
    ..#...........#.#...##.#...#..#
    .....#........#..#.....#....#..
    #.#....#...........##.....#..##
    ##.......#.....#.....#.#......#
    .##............####.#........##
    ....##.#.....#......#....#...#.
    .#.#...##.#..##..#..........#..
    ..........................#....
    ##..##..#..#.#....#.....#......
    ...#.#........#.#.##.#.....#..#
    #..#....#...#..#...#........#.#
    #.......#####...#..#..#.#......
    #.##....#......#......#..###...
    ..#.......#...........#.....##.
    #...#....#..#......##...#......
    ...##.#..##........#..###......
    ##.#...........#.............##
    #.....#..#.....#.....#.........
    .#..........#..#......###......
    ...#...#..##.......#...#...#.#.
    ..####......#.....#..#.#......#
    ....#..#.....#.#...............
    .#.......#....#.....#..##....#.
    .....#.........#..........##...
    #...........#..#.....#........#
    ............#..##...#...#.#....
    ##.............####...#.....#..
    .....#......#....##.#.....##...
    ...........#.....#.#..#.#......
    .#.#......#....#.............##
    ##...#.#.......##........#.....
    #..#.....#.#.......####...#..#.
    ....#.#...#....#.###..#..#.#...
    .....#.#..#......#.##.#####.#..
    .....#....##..........#......#.
    #.......#........##.......##...
    #...#..#..##.#....#...#...#....
    ...#..##..#...#..........#.....
    #..#....###.....#......##......
    ...###......#.....#....#.......
    #.#...#.#..###.####.......#.#.#
    ...#......#.#..##..#.....#.....
    #.#............#.....##.#......
    #..#......##...##..#...#.#..###
    #.....#...#..#..#....#..###....
    ####..###....#..##....#..#.....
    ..##.#.....#.......##....#.#.#.
    ##..#.#.......#.#...##.#..#.#..
    ..#.#.#.##.#.#.#...........#...
    ...#.##.....#....#..#.#..#.....
    ...#..#.........#..........#..#
    #...#..#.....#.#.#.............
    ##.#....##.##...#...#..#..#..#.
    ....####..##..##.#..#...##.....
    ##.....##.#.#...#.#.......###..
    #..#.#....#......#.......##...#
    #.#...............#..#..#......
    .....##...##..#........#......#
    .#..#............##......#....#
    ......#.#..#..##.#......#.....#
    ..#.#.............#...#......##
    ....#.#..#..#...##...#..##.....
    #.#.............#...#.#..#....#
    #..#..#.##....#....#...#.......
    ....#..#..........#.....##...#.
    ..#####.......#...#..........#.
    ....#......##.......#..##.#.#.#
    #...#.#.....#....#....##.......
    ..##.#.#..#.#...#.....##.....#.
    #.#..#....#............#..#.#..
    ...#.##..##..#.#...###......#.#
    ......##.......#....#......###.
    ....#..##.......#..#.#....#..#.
    #............#..........##..#.#
    ..#.....#..#.#..##..#....##.#..
    .....#.....#....##.#.#......#.#
    ...####.......###..#...#.#....#
    .#.##.....##.....##..#..#......
    ...#..###..##..................
    ##..##.....#.#..#..#.#........#
    .#.#........##.........#....#..
    ........#......###....#...#....
    ......#...........#...........#
    .#...###...#.........#.#...#..#
    .....#..........#......##....#.
    .#.#...#........##.......#.#...
    .....##.....##....#...#...#..#.
    ..#.....................##...##
    #..#.#......##...##..#......#..
    `
}