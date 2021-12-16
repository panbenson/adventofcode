def parse_lines(input_file, split_by_char=False):
    with open(input_file, 'r') as reader:
        lines = [list(line.strip('\n')) if split_by_char else line.strip('\n') if line !=
                 '\n' else '' for line in reader]

    return lines


def parse_ints(input_file, delimiter=','):
    with open(input_file, 'r') as reader:
        lines = [[int(i) for i in line.strip('\n').split(delimiter) if i != '']
                 for line in reader]
    return lines


def parse_strings(input_file, delimiter=','):
    with open(input_file, 'r') as reader:
        lines = [line.strip('\n').split(delimiter) if line !=
                 '\n' else [] for line in reader]
    return lines


def group_grid(arr):
    grids = []
    grid = []
    for line in arr:
        if len(line) == 0:
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    grids.append(grid)

    return grids
