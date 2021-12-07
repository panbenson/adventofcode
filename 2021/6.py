# https://adventofcode.com/2021/day/6
from collections import defaultdict

def day_six(input_file):
    # nums = [3,4,3,1,2]
    nums = [1,3,4,1,1,1,1,1,1,1,1,2,2,1,4,2,4,1,1,1,1,1,5,4,1,1,2,1,1,1,1,4,1,1,1,4,4,1,1,1,1,1,1,1,2,4,1,3,1,1,2,1,2,1,1,4,1,1,1,4,3,1,3,1,5,1,1,3,4,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,5,2,5,5,3,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,1,1,1,1,5,1,1,1,1,1,4,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,1,2,4,1,5,5,1,1,5,3,4,4,4,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,5,3,1,4,1,1,2,2,1,2,2,5,1,1,1,2,1,1,1,1,3,4,5,1,2,1,1,1,1,1,5,2,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,4,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,5,1,1,1,1,1,1,1,5,1,1,3,1,1,1,3,1,4,2,1,5,1,3,5,5,2,1,3,1,1,1,1,1,3,1,3,1,1,2,4,3,1,4,2,2,1,1,1,1,1,1,1,5,2,1,1,1,2]
    counts = {i: 0 for i in range(9)}

    for i in nums:
        counts[i] += 1

    # counts[3] += 1
    print(counts)
    runs = 256
    
    for run in range(runs):
        temp = 0
        for i in range(8, -1, -1):
            if i == 0:
                counts[6] += counts[0]
                counts[8] += counts[0]
                counts[0] = temp
            else:
                next = counts[i]
                counts[i] = temp
                temp = next
            # print(i)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[i] = 6
        #         nums.append(8)
        #     else:
        #         nums[i] -= 1
        # print(nums)
        print(counts)
        print(len(nums))
    print(sum(counts.values()))

def day_six_p2(input_file):
    # nums = parse_input(input_file)
    pass

def main():
    input_file = '6-example.in'
    # input_file = '6.in'
    day_six(input_file)
    # day_six_p2(input_file)


main()
