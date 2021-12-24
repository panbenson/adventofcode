# https://adventofcode.com/2021/day/22
import read_input
import heapq
from collections import defaultdict
from collections import deque


def day_twenty_two(input_file):
    lines = read_input.parse_lines(input_file)
    instructions = []

    for line in lines:
        on, rest = line.split(' ')
        x, y, z = rest.split(',')
        instructions.append((on == 'on', [int(i) for i in x.split('=')[1].split('..')], [int(
            i) for i in y.split('=')[1].split('..')], [int(i) for i in z.split('=')[1].split('..')]))

    print(instructions)
    grid = [[[False for i in range(101)]
             for n in range(101)] for r in range(101)]
    for instruction in instructions:
        val, x_pair, y_pair, z_pair = instruction
        if x_pair[0] + 50 > len(grid[0][0]) or x_pair[0] + 50 < 0 or x_pair[1] + 50 > len(grid[0][0]) or x_pair[1] + 50 < 0:
            continue
        if y_pair[0] + 50 > len(grid[0]) or y_pair[0] + 50 < 0 or y_pair[1] + 50 > len(grid[0]) or y_pair[1] + 50 < 0:
            continue
        if z_pair[0] + 50 > len(grid) or z_pair[0] + 50 < 0 or z_pair[1] + 50 > len(grid) or z_pair[1] + 50 < 0:
            continue
        print(instruction)
        for z in range(z_pair[0] + 50, z_pair[1] + 51):
            for y in range(y_pair[0] + 50, y_pair[1] + 51):
                for x in range(x_pair[0] + 50, x_pair[1] + 51):
                    grid[z][y][x] = val

    count = 0
    for z in range(len(grid)):
        for y in range(len(grid[0])):
            for x in range(len(grid[0][0])):
                if grid[z][y][x]:
                    count += 1

    print(count)


def day_twenty_two_p2(input_file):
    lines = read_input.parse_lines(input_file)
    instructions = []
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0

    for line in lines:
        on, rest = line.split(' ')
        x, y, z = rest.split(',')
        instructions.append((on == 'on', [int(i) for i in x.split('=')[1].split('..')], [int(
            i) for i in y.split('=')[1].split('..')], [int(i) for i in z.split('=')[1].split('..')]))

    for instruction in instructions:
        val, x_pair, y_pair, z_pair = instruction
        min_x = min(min_x, x_pair[0])
        max_x = max(max_x, x_pair[1])
        min_y = min(min_y, y_pair[0])
        max_y = max(max_y, y_pair[1])
        min_z = min(min_z, z_pair[0])
        max_z = max(max_z, z_pair[1])

    grid = [[[False for i in range(max_x - min_x + 1)]
             for n in range(max_y - min_y + 1)] for r in range(max_z - min_z + 1)]
    for instruction in instructions:
        val, x_pair, y_pair, z_pair = instruction
        if x_pair[0] + 50 > len(grid[0][0]) or x_pair[0] + 50 < 0 or x_pair[1] + 50 > len(grid[0][0]) or x_pair[1] + 50 < 0:
            continue
        if y_pair[0] + 50 > len(grid[0]) or y_pair[0] + 50 < 0 or y_pair[1] + 50 > len(grid[0]) or y_pair[1] + 50 < 0:
            continue
        if z_pair[0] + 50 > len(grid) or z_pair[0] + 50 < 0 or z_pair[1] + 50 > len(grid) or z_pair[1] + 50 < 0:
            continue

        for z in range(z_pair[0] + 50, z_pair[1] + 51):
            for y in range(y_pair[0] + 50, y_pair[1] + 51):
                for x in range(x_pair[0] + 50, x_pair[1] + 51):
                    grid[z][y][x] = val

    count = 0
    for z in range(len(grid)):
        for y in range(len(grid[0])):
            for x in range(len(grid[0][0])):
                if grid[z][y][x]:
                    count += 1

    print(count)


def main():
    input_file = '22-example.in'
    # input_file = '22.in'
    # day_twenty_two(input_file)
    day_twenty_two_p2(input_file)


main()
