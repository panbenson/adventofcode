def parse_ints(input_file):
    with open(input_file, 'r') as reader:
        lines = [[int(i) for i in line.strip('\n').split(',') if i != '']
                 for line in reader]
    return lines


def parse_strings(input_file):
    with open(input_file, 'r') as reader:
        lines = [line.strip('\n').split(',') if line !=
                 '\n' else [] for line in reader]
    return lines


def group_grid(arr, type="str"):
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
