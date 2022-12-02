# this is probably over engineered..
def parse_newline_delimited_arrays(file, formatter):
    with open(file) as file:
        content = file.read()

        # newline separated arrays
        groups = content.split('\n\n')
        arrays = list(
            map(lambda x: list(map(lambda e: formatter(e), x.strip().split())), groups))

        return arrays
