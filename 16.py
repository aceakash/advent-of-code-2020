def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def parse_input(contents):
    ranges = []
    tickets = []

    lines = contents.split('\n')
    range_lines = [l for l in lines if " or " in l]
    for rl in range_lines:
        parts = rl.split(':')
        range_strings = [p.strip() for p in parts[1].split('or')]
        for rs in range_strings:
            rparts = rs.split('-')
            ranges.append((int(rparts[0]), int(rparts[1])))

    skip = True
    for l in lines:
        if "nearby tickets" in l:
            skip = False
            continue
        if skip:
            continue
        nums = [int(s) for s in l.split(',')]
        tickets.append(nums)

    # print(ranges)
    # print(tickets)
    return ranges, tickets


def sixteen(ranges, tickets):
    map = ['i' for n in range(0, 1000)]
    for (min, max) in ranges:
        for i in range(min, max+1):
            map[i] = 'v'

    scanning_error_rate = 0

    for tline in tickets:
        for t in tline:
            if map[t] == 'i':
                scanning_error_rate += t

    return scanning_error_rate


contents = file_contents('./16.input.txt')
ranges, tickets = parse_input(contents)
ans = sixteen(ranges, tickets)
print(ans)
