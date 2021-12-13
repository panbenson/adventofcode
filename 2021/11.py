# https://adventofcode.com/2021/day/11
import read_input
from functools import reduce


def finished_flashing(flashed, grid):
    finished = True
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] > 9 and not flashed[y][x]:
                finished = False

    return finished


def day_eleven(input_file):
    lines = read_input.parse_lines(input_file, True)
    grid = [[int(i) for i in line] for line in lines]

    total = 0

    for i in range(100):
        flashed = [[False for i in range(len(grid[0]))]
                   for n in range(len(grid))]
        # increase energy level by 1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] += 1

        # increase energy level by 1 for > 9
        finished = False
        while not finished:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] > 9 and not flashed[y][x]:
                        check_adjacent(x, y, grid)
                        flashed[y][x] = True
            finished = finished_flashing(flashed, grid)

        # reset > 9
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    total += 1
                    grid[y][x] = 0

    print(total)


def check_adjacent(x, y, grid):
    if x + 1 < len(grid[0]):
        grid[y][x + 1] += 1
        if y + 1 < len(grid):
            grid[y + 1][x + 1] += 1
        if y - 1 >= 0:
            grid[y - 1][x + 1] += 1
    if x - 1 >= 0:
        grid[y][x - 1] += 1
        if y + 1 < len(grid):
            grid[y + 1][x - 1] += 1
        if y - 1 >= 0:
            grid[y - 1][x - 1] += 1
    if y + 1 < len(grid):
        grid[y + 1][x] += 1
    if y - 1 >= 0:
        grid[y - 1][x] += 1


def day_eleven_p2(input_file):
    lines = read_input.parse_lines(input_file, True)
    grid = [[int(i) for i in line] for line in lines]

    step = 0
    all_flashed = False

    while not all_flashed:
        step += 1

        flashed = [[False for i in range(len(grid[0]))]
                   for n in range(len(grid))]
        # increase energy level by 1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] += 1

        # increase energy level by 1 for > 9
        finished = False
        while not finished:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] > 9 and not flashed[y][x]:
                        check_adjacent(x, y, grid)
                        flashed[y][x] = True
            finished = finished_flashing(flashed, grid)

        # reset > 9
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = 0

        # same as
        # stop = reduce(lambda a, b: a and b, [reduce(
        #     lambda a, b: a and b, row, True) for row in flashed], True)
        stop = True
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                stop = stop and flashed[y][x]

        all_flashed = stop

    print(step)


def main():
    # input_file = '11-example.in'
    input_file = '11.in'
    day_eleven(input_file)
    day_eleven_p2(input_file)


main()
