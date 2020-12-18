NOT_EXECUTED = ''
EXECUTED = 'executed'

def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents

def parse_line(line):
    instr, num_str = line[:3], line[4:]
    sign = 1 if num_str[0] == '+' else -1
    num = sign * int(num_str[1:])
    return (instr, num, NOT_EXECUTED)

def parse_input(txt):
    lines = txt.split('\n')
    return [parse_line(l) for l in lines]

def run_code(code):
    acc = 0
    ptr = 0
    is_last_instruction = False
    inf_loop_detected = False
    while True:   
        if is_last_instruction:
            break

        if ptr >= len(code):
            ptr = len(code) - 2
            is_last_instruction = True    
            continue
        
        instr, num, execute_flag = code[ptr]    
        if execute_flag == EXECUTED:
            inf_loop_detected = True
            break

        code[ptr] = (instr, num, EXECUTED)
        if instr == 'nop':
            ptr += 1
        elif instr == 'acc':
            acc = acc + num
            ptr += 1
        elif instr == 'jmp':
            ptr += num

    return (acc, inf_loop_detected)

def eight_point_one(txt):
    parsed = parse_input(txt)
    acc, inf_loop_detected = run_code(parsed)
    return acc

def change_next(fromInstr, toInstr, code, from_index):
    mod_code = code[:]
    for j in range(from_index+1, len(mod_code)):
        (instr, num, exec_flag) = mod_code[j]
        if instr == fromInstr:
            mod_code[j] = (toInstr, num, exec_flag)
            from_index = j
            return mod_code, from_index
    
    return mod_code, None

def change_and_run_code(fromInstr, toInstr, code):
    last = -1
    while last != None:
        mod_code, last = change_next(fromInstr, toInstr, code, last)
        acc, inf_loop = run_code(mod_code)
        if not inf_loop:
            return acc

def eight_point_two(txt):
    code = parse_input(txt)
    
    acc = change_and_run_code('jmp', 'nop', code)
    if acc != None:
        return acc

    acc = change_and_run_code('nop', 'jmp', code)
    if acc != None:
        return acc
        
 
contents = file_contents('./8.input.txt')
print(eight_point_one(contents))
print(eight_point_two(contents))