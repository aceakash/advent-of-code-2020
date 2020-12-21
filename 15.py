class SpokenNumbers:
    def __init__(self, nums):
        self.nums = nums
        self.lookup = {}
        for i in range(len(nums)):
            num = nums[i]
            turn_no = i + 1
            if num in self.lookup:
                self.lookup[num].append(turn_no)
            else:
                self.lookup[num] = [turn_no]

    def turn_count(self):
        return len(self.nums)

    def set_next_num(self, next_num):
        self.nums.append(next_num)
        turn_no = len(self.nums)
        if next_num in self.lookup:
            self.lookup[next_num].append(turn_no)
        else:
            self.lookup[next_num] = [turn_no]

    def next_num(self):
        last_num = self.nums[-1]
        last_num_past = self.lookup[last_num]
        if len(last_num_past) == 1:
            self.set_next_num(0)
        else:
            diff = last_num_past[-1] - last_num_past[-2]
            self.set_next_num(diff)

    def last_num(self):
        return self.nums[-1]


def fifteen_point_one(input):
    initial_spoken = [int(a) for a in input.split(',')]
    spoken = SpokenNumbers(initial_spoken)
    while spoken.turn_count() < 2020:
        spoken.next_num()

    return spoken.last_num()


if __name__ == '__main__':
    input = "1,20,11,6,12,0"
    ans1 = fifteen_point_one(input)
    print(ans1)