# https://adventofcode.com/2021/day/12
import read_input
from collections import defaultdict
from collections import deque


def day_twelve(input_file):
    lines = read_input.parse_strings(input_file, '-')

    total = 0
    graph = defaultdict(lambda: [])
    small_caves = set()

    # create the graph and keep track of small caves
    for line in lines:
        a, b = line
        if a.lower() == a:
            small_caves.add(a)

        if b.lower() == b:
            small_caves.add(b)

        graph[a].append(b)
        graph[b].append(a)

    # bfs
    queue = deque([('start', set())])
    while queue:
        node, visited = deque.popleft(queue)
        if node == 'end':
            total += 1
            continue

        for neighbour in graph[node]:
            # we can only visit a small cave once
            if neighbour not in visited or neighbour not in small_caves:
                new_visited = visited.copy()
                new_visited.add(node)
                queue.append((neighbour, new_visited))

    print(total)


def day_twelve_p2(input_file):
    lines = read_input.parse_strings(input_file, '-')

    total = 0
    graph = defaultdict(lambda: [])
    small_caves = set()

    # create the graph and keep track of small caves
    for line in lines:
        a, b = line
        if a.lower() == a:
            small_caves.add(a)

        if b.lower() == b:
            small_caves.add(b)

        graph[a].append(b)
        graph[b].append(a)

    # bfs
    queue = deque([('start', set(), False)])
    while queue:
        node, visited, twiced = deque.popleft(queue)
        if node == 'end':
            total += 1
            continue

        for neighbour in graph[node]:
            # we can't visit start twice, but a single small cave can be visited twice
            if neighbour != 'start' and (neighbour not in visited or neighbour not in small_caves or not twiced):
                a = twiced
                if neighbour in small_caves and neighbour in visited:
                    a = True
                new_visited = visited.copy()
                new_visited.add(node)
                queue.append((neighbour, new_visited, a))

    print(total)


def main():
    # input_file = '12-example.in'
    input_file = '12.in'
    day_twelve(input_file)
    day_twelve_p2(input_file)


main()
