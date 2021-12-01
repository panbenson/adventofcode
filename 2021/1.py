# https://adventofcode.com/2021/day/1
def day_one():
    with open('1.in', 'r') as reader:
        prev = 99999
        increasing = 0
        for line in reader:
            num = int(line)
            if prev < num:
                increasing += 1
            prev = num
        print(increasing)


def day_one_part_two():
    with open('1.in', 'r') as reader:
        prev = 99999
        increasing = 0
        nums = [int(line) for line in reader]

        # exclude the last 2 because they don't form a window of 3
        for i in range(len(nums) - 2):
            num = sum(nums[i:i+3])
            # print(num)
            # only consider increase NOT no change :(
            if prev < num:
                increasing += 1
            prev = num
        print(increasing)


day_one()
day_one_part_two()
