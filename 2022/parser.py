# this is probably over engineered..
def parse_newline_delimited_arrays(file, formatter):
    with open(file) as file:
        content = file.read()

        # newline separated arrays
        groups = content.split('\n\n')
        arrays = list(
            map(lambda x: list(map(lambda e: formatter(e), x.strip().split())), groups))

        return arrays


def parse_space_delimited_arrays(file, formatter):
    with open(file) as file:
        content = file.read()

        # newline separated arrays
        groups = content.split('\n')[:-1]
        arrays = list(
            map(lambda x: list(map(lambda e: formatter(e), x.strip().split())), groups))

        return arrays


def parse_newline_delimited_array(file, formatter):
    with open(file) as file:
        content = file.read()

        # newline separated arrays
        groups = content.split('\n')[:-1]

        arrays = list(
            map(lambda x: formatter(x.strip()), groups))

        return arrays


def parse_newline_delimited_array_in_groups_of(file, formatter, group_size):
    with open(file) as file:
        content = file.read()

        # newline separated arrays
        groups = content.split('\n')[:-1]

        arrays = list(
            map(lambda x: formatter(x.strip()), groups))

        array_groups = []
        for i in range(0, len(arrays), group_size):
            array_groups.append(arrays[i: i+group_size])

        return array_groups
