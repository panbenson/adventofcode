from collections import defaultdict
import copy
import sys
import re
import math

def day_8_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        lines = file.readlines()
        instructions = list(map(lambda x: 0 if x == 'L' else 1, lines[0].strip()))
        network = {}
        for line in lines[2:]:
            parts = line.strip().split(' = ')
            left = parts[1].split(', ')[0][1:]
            right = parts[1].split(', ')[1][:-1]
            network[parts[0]] = [left, right]

        # print(instructions, network)

    curr = 'AAA'
    steps = 0
    while curr != 'ZZZ':
        for move in instructions:
            curr = network[curr][move]
            steps += 1

    print(f"took {steps} steps to reach ZZZ")



def day_8_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        lines = file.readlines()
        instructions = list(map(lambda x: 0 if x == 'L' else 1, lines[0].strip()))
        network = {}
        for line in lines[2:]:
            parts = line.strip().split(' = ')
            left = parts[1].split(', ')[0][1:]
            right = parts[1].split(', ')[1][:-1]
            network[parts[0]] = [left, right]

    curr = list(filter(lambda x: x[-1] == 'A', network.keys()))
    print("checking nodes all at once", curr)
    steps = 0
    instruction = 0
    # it's evident we can't iterate to the solution
    # the approach we can take is to see how many steps it takes
    # to reach each Z end?
    while not all(map(lambda x: x[-1] == 'Z', curr)):
        steps += 1

        for i in range(len(curr)):
            curr[i] = network[curr[i]][instructions[instruction]]

        instruction = (instruction + 1) % len(instructions)

    print(f"took {steps} steps to reach ZZZ")


# day_8_1()
day_8_2()
