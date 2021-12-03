# https://adventofcode.com/2021/day/4
def day_four(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.strip('\n') for line in reader]

    print(nums)


def day_four_p2(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.strip('\n') for line in reader]


def main():
    input_file = '4-example.in'
    # input_file = '4.in'
    day_four(input_file)
    # day_four_p2(input_file)


main()
