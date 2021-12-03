# https://adventofcode.com/2021/day/3
def day_three(input_file):

    with open(input_file, 'r') as reader:
        nums = [line.strip('\n') for line in reader]

    most_common = ""

    # loop thru all the positions
    for i in range(len(nums[0])):
        zeros = 0
        ones = 0
        for line in nums:
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            most_common += '0'
        else:
            most_common += '1'

    # with the python bitwise xor `^` operator, we can invert the string
    mask = 2 ** len(nums[0]) - 1  # this is 111111...
    least_common = '{0:b}'.format(int(most_common, 2) ^ mask)
    print(int(most_common, 2), int(least_common, 2))
    print(int(most_common, 2) * int(least_common, 2))


def day_three_p2(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.strip('\n') for line in reader]

    def find_o2(values, depth):
        if len(values) == 1:
            return(int(values[0], 2))

        zeros = []
        ones = []
        # print(depth)
        for line in values:
            if line[depth] == "0":
                zeros.append(line)
            else:
                ones.append(line)

        if len(zeros) > len(ones):
            # print('zeros more common', values)
            return find_o2(zeros, depth + 1)
        else:
            # print('ones more common', values)
            return find_o2(ones, depth + 1)

    def find_co2(values, depth):
        if len(values) == 1:
            return(int(values[0], 2))

        zeros = []
        ones = []
        # print(depth)
        for line in values:
            if line[depth] == "0":
                zeros.append(line)
            else:
                ones.append(line)

        if len(zeros) <= len(ones):
            # print('zeros less common', values)
            return find_co2(zeros, depth + 1)
        else:
            # print('ones less common', values)
            return find_co2(ones, depth + 1)

    print(find_o2(nums, 0), find_co2(nums, 0))
    print(find_o2(nums, 0) * find_co2(nums, 0))


def main():
    # input_file = '3-example.in'
    input_file = '3.in'
    day_three(input_file)
    day_three_p2(input_file)


main()
