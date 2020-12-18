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

def sum_of_values2(mem):
    sum = 0
    for k, v in mem.items():
        if v == '0':
            continue
        sum += int(v, 10)
    return sum

def process_floating_bits(num):
    outputs = []
    # print('num', num)
    x_count = num.count('X')
    for i in range(x_count):
        # print('x_idx', x_idx)
        # print('outputs', outputs)
        if len(outputs) == 0:
            outputs.append(num.replace('X', '0', 1))
            outputs.append(num.replace('X', '1', 1))
        else:
            for o in outputs:
                if o.find('X') == -1:
                    continue
                # print('o', o)
                new_outputs = []
                new_outputs.append(o.replace('X', '0', 1))
                new_outputs.append(o.replace('X', '1', 1))
                outputs.extend(new_outputs)
                # print('outputs new', outputs)


    return [o for o in outputs if o.find('X') == -1]

def apply_mask2(bin_str, mask):
    output = [c for c in bin_str]
    x_indexes = []
    for i in range(len(mask)):
        m = mask[i]
        b = bin_str[i]
        if m == '1':
            output[i] = '1'
        elif m == '0':
            output[i] = b
        elif m == 'X':
            output[i] = 'X'
            # x_indexes.append(i)

    # print('x indexes', x_indexes)
    # print()
    output_str = ''.join(output)
    outputs = process_floating_bits(output_str)
    # print(f'outputs for {output_str}')
    # print(outputs)
    return outputs


def process2(cmd, mem, mask):
    if cmd.startswith('mask'):
        return cmd.split(" = ")[1]
    elif cmd.startswith('mem'):
        [part1, val_str] = cmd.split(' = ')
        addr = part1[4:-1]
        bin_str = to_binary(addr)
        new_addrs = apply_mask2(bin_str, mask)
        for new_addr in new_addrs:
            mem[new_addr] = val_str
        return mask


def fourteen_point_one(cmds):
    mem = dict()
    mask = ""
    for c in cmds:
        mask = process(c, mem, mask)

    sum = sum_of_values(mem)
    return sum

def fourteen_point_two(cmds):
    mem = dict()
    mask = ''
    for i in range(len(cmds)):
        c = cmds[i]
        print(f'Processing cmd {i} of {len(cmds)}')
        mask = process2(c, mem, mask)

    sum = sum_of_values2(mem)
    return sum


input = file_contents('./14.input.txt')
cmds = parse_input(input)

ans = fourteen_point_one(cmds)
print(ans)

ans2 = fourteen_point_two(cmds)
print(ans2)

