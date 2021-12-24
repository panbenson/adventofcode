# https://adventofcode.com/2021/day/20
import read_input
import heapq
from collections import defaultdict
from collections import deque


def next_pixel(x, y, grid, image_enhancement_algorithm, infinity_space):
    bin_str = ''
    default_val = '0' if infinity_space == '.' else '1'

    # top row
    if y - 1 >= 0:
        if x - 1 >= 0:
            bin_str += '0' if grid[y - 1][x - 1] == '.' else '1'
        else:
            bin_str += default_val
        bin_str += '0' if grid[y - 1][x] == '.' else '1'
        if x + 1 < len(grid[0]):
            bin_str += '0' if grid[y - 1][x + 1] == '.' else '1'
        else:
            bin_str += default_val
    else:
        bin_str += default_val*3

    # middle row
    if x - 1 >= 0:
        bin_str += '0' if grid[y][x - 1] == '.' else '1'
    else:
        bin_str += default_val
    bin_str += '0' if grid[y][x] == '.' else '1'
    if x + 1 < len(grid[0]):
        bin_str += '0' if grid[y][x + 1] == '.' else '1'
    else:
        bin_str += default_val

    # bottom row
    if y + 1 < len(grid):
        if x - 1 >= 0:
            bin_str += '0' if grid[y + 1][x - 1] == '.' else '1'
        else:
            bin_str += default_val
        bin_str += '0' if grid[y + 1][x] == '.' else '1'
        if x + 1 < len(grid[0]):
            bin_str += '0' if grid[y + 1][x + 1] == '.' else '1'
        else:
            bin_str += default_val
    else:
        bin_str += default_val * 3

    return image_enhancement_algorithm[int(bin_str, 2)]


def day_twenty(input_file):
    lines = read_input.parse_lines(input_file)
    # grid = [[int(i) for i in row] for row in lines]
    image_enhancement_algorithm = list(lines[0])

    grid = [list(line) for line in lines[2:]]
    infinity_space = '.'

    for i in range(50):
        print()
        grid_copy = [[grid[y - 5][x - 5] if y - 5 >= 0 and y - 5 < len(grid) and x - 5 >= 0 and x - 5 < len(grid[0]) else infinity_space for x in range(len(grid[0]) + 10)]
                     for y in range(len(grid) + 10)]

        next_grid = [[infinity_space for x in range(len(grid[0]) + 10)]
                     for y in range(len(grid) + 10)]

        print('\n'.join([''.join(row) for row in grid_copy]))

        for y in range(len(next_grid)):
            for x in range(len(next_grid[0])):
                next_grid[y][x] = next_pixel(
                    x, y, grid_copy, image_enhancement_algorithm, infinity_space)

        print('\n'.join([''.join(row) for row in next_grid]))
        print(len(next_grid))
        value_grid = [[0 if next_grid[y][x] == '.' else 1 for x in range(
            len(next_grid[0]))] for y in range(len(next_grid))]

        count = 0
        for row in next_grid:
            for item in row:
                if item == '#':
                    count += 1
        print(count)
        print(sum([sum(row) for row in value_grid]))

        grid = next_grid
        infinity_space = image_enhancement_algorithm[int(
            (infinity_space * 9).replace('.', '0').replace('#', '1'), 2)]

    # for line in lines:
    #     print(line)


def day_twenty_p2(input_file):
    pass


def main():
    input_file = '20-example.in'
    input_file = '20.in'
    day_twenty(input_file)
    day_twenty_p2(input_file)


main()
