# https://adventofcode.com/2021/day/15
import read_input
import heapq
from collections import defaultdict
from collections import deque


def check_adjacent(x, y, cost, grid, pq, visited):
    if x + 1 < len(grid[0]):
        if not visited[y][x + 1]:
            heapq.heappush(pq, (cost + grid[y][x + 1], (x + 1, y)))
        # if y + 1 < len(grid):
        #     if not visited[y + 1][x + 1]:
        #         heapq.heappush(pq, (cost + grid[y + 1][x + 1], (x + 1, y + 1)))
        # if y - 1 >= 0:
        #     if not visited[y - 1][x + 1]:
        #         heapq.heappush(pq, (cost + grid[y - 1][x + 1], (x + 1, y - 1)))
    if x - 1 >= 0:
        if not visited[y][x - 1]:
            heapq.heappush(pq, (cost + grid[y][x - 1], (x - 1, y)))
        # if y + 1 < len(grid):
        #     if not visited[y + 1][x - 1]:
        #         heapq.heappush(pq, (cost + grid[y + 1][x - 1], (x - 1, y + 1)))
        # if y - 1 >= 0:
        #     if not visited[y - 1][x - 1]:
        #         heapq.heappush(pq, (cost + grid[y - 1][x - 1], (x - 1, y - 1)))
    if y + 1 < len(grid):
        if not visited[y + 1][x]:
            heapq.heappush(pq, (cost + grid[y + 1][x], (x, y + 1)))
    if y - 1 >= 0:
        if not visited[y - 1][x]:
            heapq.heappush(pq, (cost + grid[y - 1][x], (x, y - 1)))


def day_fifteen(input_file):
    lines = read_input.parse_lines(input_file)
    grid = [[int(i) for i in row] for row in lines]

    # use djikstras to find the best route
    pq = [(0, (0, 0))]
    visited = [[False for i in row] for row in lines]

    while len(pq):
        cost, (x, y) = heapq.heappop(pq)
        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            print(cost)
            break
        if not visited[y][x]:
            check_adjacent(x, y, cost, grid, pq, visited)

        visited[y][x] = True


def day_fifteen_p2(input_file):
    lines = read_input.parse_lines(input_file)
    base_grid = [[int(i) for i in row] for row in lines]
    # print(base_grid)

    big_grid = [[0 for i in range(5 * len(base_grid[0]))]
                for n in range(5 * len(base_grid))]

    # grow the grid
    for times_x in range(5):
        for times_y in range(5):
            for y in range(len(base_grid)):
                for x in range(len(base_grid[0])):
                    n = base_grid[y][x]
                    # luckily, we can do this because it doesnt wrap over twice
                    big_grid[len(base_grid) * times_y + y][len(base_grid[0]) * times_x + x] = (
                        times_x + times_y + n) % 10 + (times_x + times_y + n) // 10

    # use djikstras to find the best route
    pq = [(0, (0, 0))]
    visited = [[False for i in row] for row in big_grid]

    while len(pq):
        cost, (x, y) = heapq.heappop(pq)
        if x == len(big_grid[0]) - 1 and y == len(big_grid) - 1:
            print(cost)
            break
        if not visited[y][x]:
            check_adjacent(x, y, cost, big_grid, pq, visited)

        visited[y][x] = True


def main():
    # input_file = '15-example.in'
    input_file = '15.in'
    day_fifteen(input_file)
    day_fifteen_p2(input_file)


main()
