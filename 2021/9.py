# https://adventofcode.com/2021/day/9
import read_input


def day_nine(input_file):
    lines = read_input.parse_lines(input_file, True)
    grid = [[int(i) for i in line] for line in lines]
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if check_adjacent(x, y, grid):
                total += grid[y][x] + 1

    print(total)


def check_adjacent(x, y, grid):
    if x + 1 < len(grid[0]):
        if grid[y][x + 1] <= grid[y][x]:
            return False
    if x - 1 >= 0:
        if grid[y][x - 1] <= grid[y][x]:
            return False
    if y + 1 < len(grid):
        if grid[y + 1][x] <= grid[y][x]:
            return False
    if y - 1 >= 0:
        if grid[y - 1][x] <= grid[y][x]:
            return False

    return True


def day_nine_p2(input_file):
    lines = read_input.parse_lines(input_file, True)
    grid = [[int(i) for i in line]for line in lines]
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if check_adjacent(x, y, grid):
                low_points.append([x, y])

    basin_sizes = []
    for low_point in low_points:
        x, y = low_point
        grid_copy = [[x for x in row] for row in grid]
        basin_sizes.append(traverse_basin(x, y, grid_copy))

    basin_sizes = sorted(basin_sizes)
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


def traverse_basin(x, y, grid):
    size = 1

    # mark current node as traversed
    grid[y][x] = 9

    if x + 1 < len(grid[0]):
        if grid[y][x + 1] != 9:
            size += traverse_basin(x + 1, y, grid)
    if x - 1 >= 0:
        if grid[y][x - 1] != 9:
            size += traverse_basin(x - 1, y, grid)
    if y + 1 < len(grid):
        if grid[y + 1][x] != 9:
            size += traverse_basin(x, y + 1, grid)
    if y - 1 >= 0:
        if grid[y - 1][x] != 9:
            size += traverse_basin(x, y - 1, grid)

    return size


def main():
    # input_file = '9-example.in'
    input_file = '9.in'
    day_nine(input_file)
    day_nine_p2(input_file)


main()
