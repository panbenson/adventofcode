from collections import defaultdict
import sys
import re

def is_number(char):
    return char >= '0' and char <= '9'

def day_3_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        sum = 0
        grid = [[char for char in line.strip()] for line in file]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if not is_number(grid[y][x]) or (x > 0 and is_number(grid[y][x - 1])):
                    continue

                # found a number, continue until no longer a number
                i = x
                while i + 1 < len(grid[0]) and is_number(grid[y][i + 1]):
                    i += 1

                # print(f"found {int(''.join(grid[y][x:i + 1]))}")
                is_part = False

                # check up, if possible
                for k in range(max(0, y - 1), y):
                    for l in range(max(0, x - 1), min(i + 2, len(grid[0]))):
                        if not is_number(grid[k][l]) and grid[k][l] != '.':
                            is_part = True

                # check below, if possible
                for k in range(y + 1, min(len(grid) - 1, y + 2)):
                    for l in range(max(0, x - 1), min(i + 2, len(grid[0]))):
                        if not is_number(grid[k][l]) and grid[k][l] != '.':
                            is_part = True

                # left
                if x - 1 >= 0 and not is_number(grid[y][x - 1]) and grid[y][x - 1] != '.':
                    is_part = True

                # right
                if i + 1 < len(grid[0]) and not is_number(grid[y][i + 1]) and grid[y][i + 1] != '.':
                    is_part = True

                if is_part:
                    sum += int(''.join(grid[y][x:i + 1]))

    print(f"sum: {sum}")



def day_3_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        sum = 0
        grid = [[char for char in line.strip()] for line in file]
        parts = {}

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if not is_number(grid[y][x]) or (x > 0 and is_number(grid[y][x - 1])):
                    continue

                # found a number, continue until no longer a number
                i = x
                while i + 1 < len(grid[0]) and is_number(grid[y][i + 1]):
                    i += 1

                # print(f"found {int(''.join(grid[y][x:i + 1]))}")
                is_part = False
                part_x_y = None

                # check up, if possible
                for k in range(max(0, y - 1), y):
                    for l in range(max(0, x - 1), min(i + 2, len(grid[0]))):
                        if not is_number(grid[k][l]) and grid[k][l] != '.':
                            part_x_y = (l, k)

                # check below, if possible
                for k in range(y + 1, min(len(grid) - 1, y + 2)):
                    for l in range(max(0, x - 1), min(i + 2, len(grid[0]))):
                        if not is_number(grid[k][l]) and grid[k][l] != '.':
                            part_x_y = (l, k)

                # left
                if x - 1 >= 0 and not is_number(grid[y][x - 1]) and grid[y][x - 1] != '.':
                    part_x_y = (x -1, y)

                # right
                if i + 1 < len(grid[0]) and not is_number(grid[y][i + 1]) and grid[y][i + 1] != '.':
                    part_x_y = (i + 1, y)

                if part_x_y:
                    if part_x_y not in parts:
                        parts[part_x_y] = int(''.join(grid[y][x:i + 1]))
                    else:
                        sum += parts[part_x_y] * int(''.join(grid[y][x:i + 1]))

    print(f"sum: {sum}")

day_3_2()
