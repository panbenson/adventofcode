# https://adventofcode.com/2021/day/16
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


def day_sixteen(input_file):
    lines = read_input.parse_lines(input_file)

    for line in lines:
        print(line)


def day_sixteen_p2(input_file):
    pass


def main():
    input_file = '16-example.in'
    # input_file = '16.in'
    day_sixteen(input_file)
    day_sixteen_p2(input_file)


main()
