from collections import defaultdict
import copy
import sys
import re
import math

def day_3_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        total = 0
        for line in file.readlines():
            memory = line.strip()
            matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
            for match in matches:
                nums = list(map(int, match[4:-1].split(',')))
                total += nums[0] * nums[1]

        print(total)


def day_3_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        total = 0
        enabled = True
        for line in file.readlines():
            print(line)
            memory = line.strip()
            matches = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', memory)
            print(matches)
            for match in matches:
                if match == "do()":
                    enabled = True
                elif match == "don't()":
                    enabled = False
                else:
                    if enabled:
                        nums = list(map(int, match[4:-1].split(',')))
                        total += nums[0] * nums[1]

        print(total)


# day_3_1()
day_3_2()
