def check_adjacent(x, y, grid):
    if x + 1 < len(grid[0]):
        print(grid[y][x + 1])
        if y + 1 < len(grid):
            print(grid[y + 1][x + 1])
        if y - 1 >= 0:
            print(grid[y - 1][x + 1])
    if x - 1 >= 0:
        print(grid[y][x - 1])
        if y + 1 < len(grid):
            print(grid[y + 1][x - 1])
        if y - 1 >= 0:
            print(grid[y - 1][x - 1])
    if y + 1 < len(grid):
        print(grid[y + 1][x])
    if y - 1 >= 0:
        print(grid[y - 1][x])
