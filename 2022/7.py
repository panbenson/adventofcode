from parser import parse_newline_delimited_array


class Dir:
    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        self.contents = []
        self.size = 0


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


def build_filesystem(terminal_output):
    cwd = None
    root = Dir(None, '/')
    line = 0
    while line < len(terminal_output):
        print(terminal_output[line])
        if terminal_output[line][1] == 'cd':
            if terminal_output[line][2] == '..':
                cwd = cwd.parent
            elif terminal_output[line][2] == '/':
                cwd = root
            else:
                cwd = list(filter(lambda x: x.name ==
                                  terminal_output[line][2], cwd.contents))[0]
            line += 1
        elif terminal_output[line][1] == 'ls':
            line += 1
            while line < len(terminal_output) and terminal_output[line][0] != '$':
                print(terminal_output[line])
                if terminal_output[line][0] == 'dir':
                    cwd.contents.append(Dir(cwd, terminal_output[line][1]))
                else:
                    cwd.contents.append(
                        File(terminal_output[line][1], int(terminal_output[line][0])))
                line += 1

    return root


def calculate_size(root):
    less_than_100k = []
    folders = list(filter(lambda x: isinstance(x, Dir), root.contents))

    # # traverse folders first
    for folder in folders:
        less_than_100k += calculate_size(folder)

    # sum size of contents
    root.size = sum(list(map(lambda x: x.size, root.contents)))
    if root.size < 100000:
        return less_than_100k + [root.size]
    else:
        return less_than_100k


def min_size(root, size):
    at_least_size = []
    folders = list(filter(lambda x: isinstance(x, Dir), root.contents))

    # # traverse folders first
    for folder in folders:
        at_least_size += min_size(folder, size)

    # sum size of contents
    root.size = sum(list(map(lambda x: x.size, root.contents)))
    if root.size >= size:
        return at_least_size + [root.size]
    else:
        return at_least_size


def part_one():
    arr = parse_newline_delimited_array(
        '2022/7-example.in', lambda e: e.split())
    arr = parse_newline_delimited_array(
        '2022/7.in', lambda e: e.split())
    fs = build_filesystem(arr)
    print(sum(calculate_size(fs)))


def part_two():
    arr = parse_newline_delimited_array(
        '2022/7-example.in', lambda e: e.split())
    arr = parse_newline_delimited_array(
        '2022/7.in', lambda e: e.split())
    fs = build_filesystem(arr)
    calculate_size(fs)
    print(f'we need to free {30000000 - (70000000 - fs.size)}')
    print(min(min_size(fs, 30000000 - (70000000 - fs.size))))


# part_one()
part_two()
