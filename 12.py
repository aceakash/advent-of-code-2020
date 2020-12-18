def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def parse_input(contents):
    lines = contents.split('\n')
    instructions = []
    for i in lines:
        instructions.append((i[0], int(i[1:])))
    return instructions


def move(x, y, dir, by):
    if dir == 'N':
        return x, y+by
    if dir == 'S':
        return x, y-by
    if dir == 'E':
        return x+by, y
    if dir == 'W':
        return x-by, y


def turn(curr_dir, move_dir, angle):
    angle = angle % 360
    l = {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E'
    }
    r = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    if move_dir == 'L':
        while angle > 0:
            curr_dir = l[curr_dir]
            angle -= 90
        return curr_dir

    if move_dir == 'R':
        while angle > 0:
            curr_dir = r[curr_dir]
            angle -= 90
        return curr_dir


def carry_out_instr(curr_dir, x, y, instr):
    move_dir, by = instr
    if move_dir == 'F':
        x, y = move(x, y, curr_dir, by)
        return curr_dir, x, y

    if move_dir in ['E', 'W', 'N', 'S']:
        x, y = move(x, y, move_dir, by)
        return curr_dir, x, y

    curr_dir = turn(curr_dir, move_dir, by)
    return (curr_dir, x, y)


def calc_manhattan_distance(x, y):
    return abs(x) + abs(y)


def parse_wp(wp_str):
    # E10:S4  /  N4:W54
    parts = wp_str.split(':')
    wpx, wpy = 0, 0
    for p in parts:
        dir = p[0]
        dist = int(p[1:])
        if dir == 'W':
            wpx = -dist
        elif dir == 'E':
            wpx = dist
        elif dir == 'N':
            wpy = dist
        elif dir == 'S':
            wpy = -dist
    return wpx, wpy


def carry_out_instr2(wpx, wpy, sx, sy, instr):
    move_dir, by = instr
    if move_dir == 'F':
        for _ in range(by):
            sx, sy = sx+wpx, sy+wpy
        return wpx, wpy, sx, sy
    if move_dir == 'N':
        return wpx, wpy+by, sx, sy
    if move_dir == 'S':
        return wpx, wpy-by, sx, sy
    if move_dir == 'E':
        return wpx+by, wpy, sx, sy
    if move_dir == 'W':
        return wpx-by, wpy, sx, sy

    curr_x_dir = 'E' if wpx >= 0 else 'W'
    turned_x_dir = turn(curr_x_dir, move_dir, by)
    curr_y_dir = 'N' if wpy >= 0 else 'S'
    turned_y_dir = turn(curr_y_dir, move_dir, by)
    new = turned_x_dir + str(abs(wpx)) + ":" + turned_y_dir + str(abs(wpy))
    wpx, wpy = parse_wp(new)
    return wpx, wpy, sx, sy


def twelve_point_one(instructions):
    # x,y origin at bottom left
    dir = 'E'
    x, y = 0, 0

    for i in instructions:
        dir, x, y = carry_out_instr(dir, x, y, i)
        # print(f'At {x} {y} facing {dir}')

    mdist = calc_manhattan_distance(x, y)
    return mdist


def twelve_point_two(instructions):
    # x,y origin at bottom left
    wpx, wpy = 10, 1
    sx, sy = 0, 0

    for i in instructions:
        wpx, wpy, sx, sy = carry_out_instr2(wpx, wpy, sx, sy, i)
        # print(f'After {i}, WP at {wpx} {wpy}, ship at {sx} {sy}')

    mdist = calc_manhattan_distance(sx, sy)
    return mdist


contents = file_contents('./12.input.txt')
instructions = parse_input(contents)

ans = twelve_point_one(instructions)
print(ans)

ans2 = twelve_point_two(instructions)
print(ans2)
