def file_contents(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    return contents

def parse_input(txt):
    lines = txt.split('\n')
    return [int(l.strip()) for l in lines]

def is_sum_of_two(sum, num_list):
    curr = 0
    while curr < len(num_list):
        remaining = sum - num_list[curr]
        try:
            match = num_list.index(remaining, curr+1)
            return True
        except ValueError:
            curr = curr + 1
    return False

def nine_point_one(nums):
    window_size = 25
    for i in range(window_size, len(nums)):
        num = nums[i]
        num_list = nums[i-window_size:i]
        if not is_sum_of_two(num, num_list):
            return num
    
def nine_point_two(nums, invalid_num):
    nums = [n for n in nums if n < invalid_num]
    s = 0
    while s < len(nums):
        sum = nums[s]
        i = s + 1
        exceeded = False
        while not exceeded:
            sum += nums[i]
            if sum == invalid_num:
                return min(*nums[s:i+1]) + max(*nums[s:i+1])
            if sum > invalid_num:
                exceeded = True
                break
            i += 1
        s += 1

contents = file_contents('./9.input.txt')
nums = parse_input(contents)

invalid_num = nine_point_one(nums)
print(invalid_num)
print(nine_point_two(nums, invalid_num))

