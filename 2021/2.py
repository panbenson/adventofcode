# https://adventofcode.com/2021/day/2
def day_two(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.split(' ') for line in reader]
    instructions = [[instruction[0], int(instruction[1])]
                    for instruction in nums]

    depth = 0
    hor = 0

    for (instruction, X) in instructions:
        if instruction == "forward":
            hor += X
        if instruction == "down":
            depth += X
        if instruction == "up":
            depth -= X

    print(f'depth: {depth}, hor: {hor}')
    print('part 1', depth * hor)


def day_two_p2(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.split(' ') for line in reader]
    instructions = [[instruction[0], int(instruction[1])]
                    for instruction in nums]

    depth = 0
    hor = 0
    aim = 0

    for (instruction, X) in instructions:
        if instruction == "forward":
            hor += X
            depth += X * aim
        if instruction == "down":
            aim += X
        if instruction == "up":
            aim -= X

    print(f'depth: {depth}, hor: {hor}')
    print('part 2:', depth * hor)


def main():
    # input_file = '2-example.in'
    input_file = '2.in'
    day_two(input_file)
    day_two_p2(input_file)


main()
