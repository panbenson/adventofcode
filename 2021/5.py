# https://adventofcode.com/2021/day/5
def parse_input(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.strip('\n').split(' -> ') for line in reader]
        lines = [[[int(x) for x in i.split(',')] for i in num]for num in nums]
    return lines


# rough work during 12 AM EST
# def day_five(input_file):
#     nums = parse_input(input_file)
#     # say there is a 1000x1000 grid
#     grid = [[0 for i in range(1000)] for n in range(1000)]

#     # print(nums)
#     for pair in nums:
#         fro, to = pair
#         # print(fro, to)
#         horizontal_diff = abs(to[0]- fro[0])
#         vertical_diff = abs(to[1]- fro[1])
#         # print(horizontal_diff, vertical_diff)
#         min_x = min(to[0], fro[0])
#         min_y = min(to[1], fro[1])

#         if horizontal_diff == 0:
#             for i in range(vertical_diff + 1):
#                 grid[min_x][min_y + i] += 1

#         if vertical_diff == 0:
#             for i in range(horizontal_diff + 1):
#                 grid[min_x + i][min_y] += 1

#     # print(grid)
#     count = 0
#     for i in range(len(grid)):
#         for n in range(len(grid[0])):
#             if grid[i][n] >= 2:
#                 count += 1

#     print(count)


#     # for to, fro in nums


# def day_five_p2(input_file):
#     nums = parse_input(input_file)
#     # say there is a 1000x1000 grid
#     grid = [[0 for i in range(1000)] for n in range(1000)]

#     # print(nums)
#     for pair in nums:
#         fro, to = pair
#         # print(fro, to)
#         horizontal_diff = abs(to[0]- fro[0])
#         vertical_diff = abs(to[1]- fro[1])
#         # print(horizontal_diff, vertical_diff)
#         min_x = min(to[0], fro[0])
#         min_y = min(to[1], fro[1])

#         if horizontal_diff == 0:
#             for i in range(vertical_diff + 1):
#                 grid[min_x][min_y + i] += 1
#         elif vertical_diff == 0:
#             for i in range(horizontal_diff + 1):
#                 grid[min_x + i][min_y] += 1
#         else:
#             # i could be + or -
#             dx = 1
#             dy = 1
#             if to[0] < fro[0]:
#                 dx = -1
#             if to[1] < fro[1]:
#                 dy = -1
#             for i in range(horizontal_diff + 1):
#                 grid[fro[0] + i * dx][fro[1] + i * dy] += 1

#     # print(grid)
#     count = 0
#     for i in range(len(grid)):
#         for n in range(len(grid[0])):
#             if grid[i][n] >= 2:
#                 count += 1

#     print(count)


def day_five_optimised(input_file, no_diagonals=False):
    nums = parse_input(input_file)
    # say there is a 1000x1000 grid
    grid = [[0 for i in range(1000)] for n in range(1000)]

    # print(nums)
    for pair in nums:
        fro, to = pair
        horizontal_diff = abs(to[0] - fro[0])
        vertical_diff = abs(to[1] - fro[1])
        max_diff = max(horizontal_diff, vertical_diff)

        if no_diagonals and horizontal_diff != 0 and vertical_diff != 0:
            continue

        # i could be + or -
        dx = 1 if to[0] > fro[0] else -1 if to[0] < fro[0] else 0
        dy = 1 if to[1] > fro[1] else -1 if to[1] < fro[1] else 0

        # we can do this because we have 45 degree angles and horizontal and vertical lines
        for i in range(max_diff + 1):
            grid[fro[0] + i * dx][fro[1] + i * dy] += 1

    count = 0
    for i in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[i][n] >= 2:
                count += 1

    print(count)


def main():
    # input_file = '5-example.in'
    input_file = '5.in'
    # day_five(input_file)
    day_five_optimised(input_file, True)
    # day_five_p2(input_file)
    day_five_optimised(input_file)


main()
