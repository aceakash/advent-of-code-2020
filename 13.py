
def main1(input):
    busses = [b for b in input.split(',')]
    inp = []
    for i in range(len(busses)):
        idx, val = i, busses[i]
        if val != 'x':
            inp.append((int(val), idx))

    print(inp)
    j = 1
    lcm = 1

    for (num, offset) in inp:
        while True:
            if (j+offset) % num == 0:
                break
            j += lcm
        print(f'For {num}, found {j}')
        # the same offsets will keep appearing at the LCM of numbers processed so far, so increment by that LCM
        # and keep looking for the next one.
        # Simple multiplication works here because all numbers are prime.
        lcm = lcm * num

    print(j)


input = "13,x,x,41,x,x,x,37,x,x,x,x,x,419,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,421,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"
ans = main1(input, 1, 1)
# ans = main1("7,13,x,x,59,x,31,19", 55, 59)
print('The answer is ', ans)
