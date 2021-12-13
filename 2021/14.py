# https://adventofcode.com/2021/day/14
import read_input
from collections import defaultdict
from collections import deque


def day_fourteen(input_file):
    lines = read_input.parse_lines(input_file)

    total = 0
    for line in lines:
        print(line)


def day_fourteen_p2(input_file):
    pass


def main():
    input_file = '14-example.in'
    # input_file = '14.in'
    day_fourteen(input_file)
    day_fourteen_p2(input_file)


main()
