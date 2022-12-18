from parser import parse_newline_delimited_array
from collections import defaultdict
import re
import heapq
from itertools import permutations
from itertools import combinations


class Valve():
    def __init__(self, name="", flow=0, tunnels=[]) -> None:
        self.name = name
        self.flow = flow
        self.tunnels = tunnels


def parse_valve(e):
    match = re.search(r'Valve (\w+).* rate=(\d+).* valves? (.*)', e)
    return Valve(match.group(1), int(match.group(2)), match.group(3).split(', '))


def pressure(graph, flow):
    sum = 0
    for key, val in flow.items():
        sum += graph[key].flow * val

    return sum


def djikstras(graph, start, dest):
    h = []
    heapq.heappush(h, (0, start))
    visited = set()

    while len(h):
        (cost, curr) = heapq.heappop(h)

        if curr == dest:
            return cost

        for valve in graph[curr].tunnels:
            if valve not in visited:
                heapq.heappush(h, (cost + 1, valve))

        visited.add(curr)


def visit(graph, time_between, curr, remaining, time, total):
    new_remaining = remaining.copy()
    if curr in new_remaining:
        new_remaining.remove(curr)
    # new_remaining.remove(curr)
    max_pressure = total

    if len(new_remaining) == 0 or time < 0:
        return total

    for valve in new_remaining:
        time_remaining = time - time_between[(curr, valve)] - 1
        if time_remaining >= 0:
            max_pressure = max(max_pressure, visit(graph, time_between, valve, new_remaining,
                                                   time_remaining, total + (time - time_between[(curr, valve)] - 1) * graph[valve].flow))

    return max_pressure


def part_one():
    arr = parse_newline_delimited_array('2022/16-example.in', parse_valve)
    arr = parse_newline_delimited_array('2022/16.in', parse_valve)
    graph = {valve.name: valve for valve in arr}

    # we only really care about the valves that we can get pressure
    non_zero_valves = [valve.name for valve in graph.values()
                       if valve.flow > 0]
    non_zero_valves.append('AA')
    time_between = {}

    # find distance between such valves
    for start in non_zero_valves:
        for dest in non_zero_valves:
            if start == dest:
                time_between[(start, dest)] = 0
                continue
            # djikstra's
            time_between[(start, dest)] = djikstras(graph, start, dest)

    # try all combinations
    print(visit(graph, time_between, 'AA', non_zero_valves, 30, 0))


# theres probably some way to optimise this but future me problem
# it just took forever to run but it works??
def part_two_combinations():
    arr = parse_newline_delimited_array('2022/16-example.in', parse_valve)
    arr = parse_newline_delimited_array('2022/16.in', parse_valve)
    graph = {valve.name: valve for valve in arr}

    # we only really care about the valves that we can get pressure
    non_zero_valves = [valve.name for valve in graph.values()
                       if valve.flow > 0]
    non_zero_valves.append('AA')
    time_between = {}

    # find distance between such valves
    for start in non_zero_valves:
        for dest in non_zero_valves:
            if start == dest:
                time_between[(start, dest)] = 0
                continue
            # djikstra's
            time_between[(start, dest)] = djikstras(graph, start, dest)

    highest_pressure = 0
    for i in range(1, len(non_zero_valves) // 2 + 1):
        for combo in combinations(non_zero_valves, i):
            other_combo = [a for a in non_zero_valves if a not in combo]
            print(list(combo), other_combo)
            me = visit(graph, time_between, 'AA', list(combo), 26, 0)
            elephant = visit(graph, time_between, 'AA', other_combo, 26, 0)
            highest_pressure = max(highest_pressure, me + elephant)

    # try all combinations
    print(highest_pressure)


# part_one()
part_two_combinations()
