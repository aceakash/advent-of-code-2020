def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def parse_input(contents):
    lines = contents.split('\n')
    return lines

def to_binary(val_str):
    bin_str = bin(int(val_str))
    bin_str = bin_str[2:].rjust(36, '0')
    return bin_str

def apply_mask(bin_str, mask):
    output = [c for c in bin_str]
    for i in range(len(mask)):
        m = mask[i]
        b = bin_str[i]
        if m == '1':
            output[i] = '1'
        elif m == '0':
            output[i] = '0'

    return ''.join(output)

def process(cmd, mem, mask):
    if cmd.startswith('mask'):
        return cmd.split(" = ")[1]
    elif cmd.startswith('mem'):
        [part1, val_str] = cmd.split(' = ')
        addr = part1[4:-1]
        bin_str = to_binary(val_str)
        new_val_str = apply_mask(bin_str, mask)
        mem[addr] = new_val_str
        return mask

def sum_of_values(mem):
    sum = 0
    for k, v in mem.items():
        if v == '000000000000000000000000000000000000':
            continue
        sum += int(v, 2)
    return sum

def fourteen_point_one(cmds):
    mem = dict()
    mask = ""
    for c in cmds:
        mask = process(c, mem, mask)

    sum = sum_of_values(mem)
    return sum



input = file_contents('./14.input.txt')
cmds = parse_input(input)
ans = fourteen_point_one(cmds)
print(ans)
