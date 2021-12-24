# https://adventofcode.com/2021/day/18
import read_input
import heapq
import math
from collections import defaultdict
from collections import deque
from itertools import permutations
import json


def split(snailfish_num):
    i = 0
    while i < len(snailfish_num):
        while i < len(snailfish_num) and snailfish_num[i] in '[],':
            i += 1

        number_stream = ''
        start_num = i
        while i < len(snailfish_num) and snailfish_num[i] not in '[],':
            number_stream += snailfish_num[i]
            i += 1

        if i < len(snailfish_num) and int(number_stream) >= 10:
            left = math.floor(int(number_stream) / 2)
            right = math.ceil(int(number_stream) / 2)
            return f"{snailfish_num[:start_num]}[{left},{right}]{snailfish_num[i:]}"

    return snailfish_num


def explode(snailfish_num):
    # we can split a shellfish number to 7 parts
    # [[6,[5,[4,[3,2]]]],1]
    # beginning, first num to left, misc to left, exploding pair, misc to the right, first num to right, end
    brackets = -1

    for i in range(len(snailfish_num)):
        if snailfish_num[i] == '[':
            brackets += 1
        elif snailfish_num[i] == ']':
            brackets -= 1

        # i is at the first bracket of the exploding pair
        if brackets == 4:
            # first find the entire exploding pair
            exploding_pair_end = i
            while snailfish_num[exploding_pair_end] != ']':
                exploding_pair_end += 1

            add_left, add_right = json.loads(
                snailfish_num[i:exploding_pair_end + 1])

            # find the first num to the left
            left_num = ''
            left_misc = ''
            left_idx = i - 1

            while snailfish_num[left_idx] in '[],' and left_idx > 0:
                left_misc = snailfish_num[left_idx] + left_misc
                left_idx -= 1
            while snailfish_num[left_idx] not in '[],' and left_idx > 0:
                left_num = snailfish_num[left_idx] + left_num
                left_idx -= 1

            # similarly, find the first num to the right
            right_num = ''
            right_misc = ''
            right_idx = exploding_pair_end + 1

            while right_idx < len(snailfish_num) and snailfish_num[right_idx] in '[],':
                right_misc += snailfish_num[right_idx]
                right_idx += 1
            while right_idx < len(snailfish_num) and snailfish_num[right_idx] not in '[],':
                right_num += snailfish_num[right_idx]
                right_idx += 1

            beginning = snailfish_num[:left_idx + 1]
            left_num = str(int(left_num) + add_left) if left_num != '' else ''
            right_num = str(int(right_num) +
                            add_right) if right_num != '' else ''
            end = snailfish_num[right_idx:]

            return f"{beginning}{left_num}{left_misc}0{right_misc}{right_num}{end}"
    return snailfish_num


def magnitude(root):
    left, right = root

    if type(left) == list:
        left = magnitude(left)
    if type(right) == list:
        right = magnitude(right)

    return 3*left + 2*right


def day_eighteen(input_file):
    lines = read_input.parse_lines(input_file)

    operating_line = lines[0]
    for line in lines[1:]:
        operating_line = f"[{operating_line},{line}]"
        while True:
            exploded = explode(operating_line)
            if operating_line == exploded:
                split_already = split(operating_line)

                if operating_line == split_already:
                    break
                else:
                    operating_line = split_already
            else:
                operating_line = exploded

    print(magnitude(json.loads(operating_line)))


def day_eighteen_p2(input_file):
    lines = read_input.parse_lines(input_file)
    max_magnitude = 0

    for combo in permutations(lines, 2):
        operating_line = f"[{combo[0]},{combo[1]}]"
        while True:
            exploded = explode(operating_line)
            if operating_line == exploded:
                split_already = split(operating_line)

                if operating_line == split_already:
                    break
                else:
                    operating_line = split_already
            else:
                operating_line = exploded

        max_magnitude = max(max_magnitude, magnitude(
            json.loads(operating_line)))

    print(max_magnitude)


def main():
    input_file = '18-example.in'
    input_file = '18.in'
    # day_eighteen(input_file)
    day_eighteen_p2(input_file)


main()
