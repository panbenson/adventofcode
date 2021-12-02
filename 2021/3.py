# https://adventofcode.com/2021/day/3
def day_three(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.split(' ') for line in reader]
    instructions = [[instruction[0], int(instruction[1])]
                    for instruction in nums]

    # depth = 0
    # hor = 0

    # for (instruction, X) in instructions:
    #     if instruction == "forward":
    #         hor += X
    #     if instruction == "down":
    #         depth += X
    #     if instruction == "up":
    #         depth -= X

    # print(f'depth: {depth}, hor: {hor}')
    # print('part 1', depth * hor)


def day_three_p2(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.split(' ') for line in reader]
    instructions = [[instruction[0], int(instruction[1])]
                    for instruction in nums]

    # depth = 0
    # hor = 0
    # aim = 0

    # for (instruction, X) in instructions:
    #     if instruction == "forward":
    #         hor += X
    #         depth += X * aim
    #     if instruction == "down":
    #         aim += X
    #     if instruction == "up":
    #         aim -= X

    # print(f'depth: {depth}, hor: {hor}')
    # print('part 2:', depth * hor)


def main():
    # input_file = '3-example.in'
    input_file = '3.in'
    day_three(input_file)
    day_three_p2(input_file)


main()
