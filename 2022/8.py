from parser import parse_newline_delimited_array


def is_visible(arr, x, y):
    curr = arr[y][x]

    # check left
    idx = x - 1
    visible = True
    while idx >= 0:
        if arr[y][idx] >= curr:
            visible = False
            break
        idx -= 1

    if visible:
        return True

    # check up
    idx = y - 1
    visible = True
    while idx >= 0:
        if arr[idx][x] >= curr:
            visible = False
            break
        idx -= 1

    if visible:
        return True

    # check right
    idx = x + 1
    visible = True
    while idx < len(arr[0]):
        if arr[y][idx] >= curr:
            visible = False
            break
        idx += 1

    if visible:
        return True

    # check down
    idx = y + 1
    visible = True
    while idx < len(arr):
        if arr[idx][x] >= curr:
            visible = False
            break
        idx += 1

    if visible:
        return True

    return False


def scenic_score(arr, x, y):
    curr = arr[y][x]

    if x == 0 or y == 0 or x == len(arr[0]) or y == len(arr):
        return 0

    # check left
    idx = x - 1
    score = 1
    trees = 0
    while idx >= 0:
        trees += 1
        if arr[y][idx] >= curr:
            break
        idx -= 1
    score *= trees

    # check up
    idx = y - 1
    trees = 0
    while idx >= 0:
        trees += 1
        if arr[idx][x] >= curr:
            break
        idx -= 1
    score *= trees

    # check right
    idx = x + 1
    trees = 0
    while idx < len(arr[0]):
        trees += 1
        if arr[y][idx] >= curr:
            break
        idx += 1
    score *= trees

    # check down
    idx = y + 1
    trees = 0
    while idx < len(arr):
        trees += 1
        if arr[idx][x] >= curr:
            break
        idx += 1
    score *= trees

    return score


def part_one():
    arr = parse_newline_delimited_array(
        '2022/8-example.in', lambda e: list(map(int, e)))
    arr = parse_newline_delimited_array(
        '2022/8.in', lambda e: list(map(int, e)))

    visible = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if is_visible(arr, col, row):
                visible += 1
    print(visible)


def part_two():
    arr = parse_newline_delimited_array(
        '2022/8-example.in', lambda e: list(map(int, e)))
    arr = parse_newline_delimited_array(
        '2022/8.in', lambda e: list(map(int, e)))

    max_score = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            max_score = max(max_score, scenic_score(arr, col, row))
    print(max_score)


# part_one()
part_two()
