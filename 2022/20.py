from parser import parse_newline_delimited_array


class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next
        self.prev = None


def part_one():
    arr = parse_newline_delimited_array('2022/20-example.in', lambda e: int(e))
    mixing = arr.copy()

    i = 0
    while i < 3000:
        if (i + 1) % 1000 == 0:
            print(arr)
        item = arr[i % len(arr)]
        if item == 0:
            i += 1
            continue

        idx = mixing.index(item)
        new_idx = item + idx
        if new_idx < 0:
            new_idx = (new_idx % len(arr) - 1) % len(arr)
        if new_idx >= len(arr):
            new_idx = new_idx % len(arr)
        if new_idx == 0:
            new_idx = len(arr) - 1
        # print(new_idx, idx)
        # print(item, 'moves between',
        #       mixing[new_idx], 'and', mixing[new_idx + 1] if new_idx + 1 < len(arr) else mixing[0])
        if new_idx > idx:
            mixing = mixing[:idx] + mixing[idx +
                                           1:new_idx + 1] + [item] + (mixing[new_idx+1:] if new_idx + 1 < len(arr) else [])
        else:
            mixing = mixing[:new_idx + 1] + mixing[new_idx +
                                                   1:idx] + [item] + mixing[idx+1:]
        # print(mixing)
        i += 1


def part_two():
    arr = parse_newline_delimited_array('2022/20-example.in', lambda e: int(e))
    # arr = parse_newline_delimited_array('2022/20.in', lambda e: int(e))


part_one()
# part_two()
