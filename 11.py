import copy


def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def parse_line(line):
    seats = [s for s in line]
    return seats


def parse_input(txt):
    lines = txt.split('\n')
    return [parse_line(l) for l in lines]


def is_seat_occupied(seats, i, j):
    if i < 0 or i >= len(seats):
        return False

    if j < 0 or j >= len(seats[i]):
        return False

    return seats[i][j] == '#'


def neighbour_count(seats, i, j):
    occupied_count = 0

    if is_seat_occupied(seats, i-1, j-1):
        occupied_count += 1

    if is_seat_occupied(seats, i-1, j):
        occupied_count += 1

    if is_seat_occupied(seats, i-1, j+1):
        occupied_count += 1

    if is_seat_occupied(seats, i, j-1):
        occupied_count += 1
    if is_seat_occupied(seats, i, j+1):
        occupied_count += 1

    if is_seat_occupied(seats, i+1, j-1):
        occupied_count += 1

    if is_seat_occupied(seats, i+1, j):
        occupied_count += 1

    if is_seat_occupied(seats, i+1, j+1):
        occupied_count += 1

    return occupied_count


def run_rules(prev):
    next = copy.deepcopy(prev)

    for i in range(0, len(prev)):
        for j in range(0, len(prev[i])):
            st = prev[i][j]
            if st == 'L' and neighbour_count(prev, i, j) == 0:
                next[i][j] = '#'
            elif st == '#' and neighbour_count(prev, i, j) >= 4:
                next[i][j] = 'L'

    return next


def line_of_sight_count(seats, i, j):
    occupied_count = 0

    # west
    visible = False
    for x in range(j-1, -1, -1):
        if seats[i][x] != '.':
            visible = seats[i][x] == '#'
            break
    if visible:
        occupied_count += 1

    # east
    visible = False
    for x in range(j+1, len(seats[0])):
        if seats[i][x] != '.':
            visible = seats[i][x] == '#'
            break
    if visible:
        occupied_count += 1

    # north
    visible = False
    for y in range(i-1, -1, -1):
        if seats[y][j] != '.':
            visible = seats[y][j] == '#'
            break
    if visible:
        occupied_count += 1

    # south
    visible = False
    for y in range(i+1, len(seats)):
        if seats[y][j] != '.':
            visible = seats[y][j] == '#'
            break
    if visible:
        occupied_count += 1

    # south-east
    visible = False
    y, x = i+1, j+1
    while True:
        if y >= len(seats) or x >= len(seats[0]):
            break

        if seats[y][x] != '.':
            visible = seats[y][x] == '#'
            break
        y += 1
        x += 1
    if visible:
        occupied_count += 1

    # south-west
    visible = False
    y, x = i+1, j-1
    while True:
        if y >= len(seats) or x < 0:
            break

        if seats[y][x] != '.':
            visible = seats[y][x] == '#'
            break
        y += 1
        x -= 1
    if visible:
        occupied_count += 1

    # north-east
    visible = False
    y, x = i-1, j+1
    while True:
        if y < 0 or x >= len(seats[0]):
            break

        if seats[y][x] != '.':
            visible = seats[y][x] == '#'
            break
        y -= 1
        x += 1
    if visible:
        occupied_count += 1

    # north-west
    visible = False
    y, x = i-1, j-1
    while True:
        if y < 0 or x < 0:
            break

        if seats[y][x] != '.':
            visible = seats[y][x] == '#'
            break
        y -= 1
        x -= 1
    if visible:
        occupied_count += 1

    return occupied_count


def run_rules2(prev):
    next = copy.deepcopy(prev)
    for i in range(0, len(prev)):
        for j in range(0, len(prev[i])):
            st = prev[i][j]
            los_count = line_of_sight_count(prev, i, j)
            if st == 'L' and los_count == 0:
                next[i][j] = '#'
            elif st == '#' and los_count >= 5:
                next[i][j] = 'L'

    return next


def count_occupied(seats, st):
    c = 0
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            if seats[i][j] == '#':
                c += 1

    return c


def eleven_point_two(seats):
    prev = None
    curr = copy.deepcopy(seats)
    passCount = 1
    while prev != curr:
        prev = curr
        curr = run_rules2(prev)
        passCount += 1

    return count_occupied(curr, 'u')


def pp(seats):
    print('\n'.join([''.join(s) for s in seats]))


def eleven_point_one(seats):
    prev = None
    curr = copy.deepcopy(seats)
    passCount = 1
    while prev != curr:
        prev = curr
        curr = run_rules(prev)
        passCount += 1

    return count_occupied(curr, 'u')


contents = file_contents('./11.input.txt')
seats = parse_input(contents)
ans = eleven_point_one(parse_input(contents))
print(ans)
ans2 = eleven_point_two(seats)
print(ans2)
