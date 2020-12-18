from functools import reduce

def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents


def parse_input(txt):
    lines = txt.split('\n')
    return [int(l.strip()) for l in lines]


def ten_point_one(nums):
    nums.append(0)
    nums.sort()
    nums.append(nums[-1]+3)
    higher, lower = nums[1:], nums[0:-1]    
    diffs = [ higher[i]-lower[i] for i in range(0, len(higher))]
    ones = len([n for n in diffs if n == 1])
    threes = len([n for n in diffs if n == 3])
    return diffs, ones * threes
    

def ten_point_two(diffs):
    ones = ''.join([str(n) for n in diffs]).split('3')
    run_lengths = [len(m) for m in ones if len(m) >= 2]
    multiplier = { 2:2, 3:4, 4:7 }
    multipliers = [multiplier[n] for n in run_lengths]
    return reduce(lambda x, y: x*y, multipliers, 1)


contents = file_contents('./10.input.txt')
nums = parse_input(contents)
diffs, product = ten_point_one(nums)
print(product)
print(ten_point_two(diffs))
