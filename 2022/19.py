from parser import parse_newline_delimited_array
import re


def get_robot_parts(e):
    match = re.search(r'Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', e)
    return (int(match.group(1)), int(match.group(2)), (int(match.group(3)), int(match.group(4))), (int(match.group(5)), int(match.group(6))))


def recursive_soln(blueprint, robots, resources, minute):
    max_geodes = 0
    print(minute, robots, resources)
    if minute >= 5:
        return resources["geode"]

    # build a robot, if possible
    # ore robot
    if resources["ore"] >= blueprint[0] and minute < 24:
        new_resources = resources.copy()
        new_robots = robots.copy()
        new_resources["ore"] -= blueprint[0]
        new_robots["ore"] += 1
        # collect materials
        for key in robots.keys():
            new_resources[key] += robots[key]
        max_geodes = max(max_geodes, recursive_soln(
            blueprint, new_robots, new_resources, minute + 1))
    # clay robot
    if resources["ore"] >= blueprint[1] and minute < 24:
        new_resources = resources.copy()
        new_robots = robots.copy()
        new_resources["ore"] -= blueprint[1]
        new_robots["clay"] += 1
        # collect materials
        for key in robots.keys():
            new_resources[key] += robots[key]
        max_geodes = max(max_geodes, recursive_soln(
            blueprint, new_robots, new_resources, minute + 1))
    # obsidian robot
    if resources["ore"] >= blueprint[2][0] and resources["clay"] >= blueprint[2][1] and minute < 24:
        new_resources = resources.copy()
        new_robots = robots.copy()
        new_resources["ore"] -= blueprint[2][0]
        new_resources["clay"] -= blueprint[2][1]
        new_robots["obsidian"] += 1
        # collect materials
        for key in robots.keys():
            new_resources[key] += robots[key]
        max_geodes = max(max_geodes, recursive_soln(
            blueprint, new_robots, new_resources, minute + 1))
    # geode robot
    if resources["ore"] >= blueprint[3][0] and resources["obsidian"] >= blueprint[3][1] and minute < 24:
        new_resources = resources.copy()
        new_robots = robots.copy()
        new_resources["ore"] -= blueprint[3][0]
        new_resources["obsidian"] -= blueprint[3][1]
        new_robots["geode"] += 1
        # collect materials
        for key in robots.keys():
            new_resources[key] += robots[key]
        max_geodes = max(max_geodes, recursive_soln(
            blueprint, new_robots, new_resources, minute + 1))

    new_resources = resources.copy()
    new_robots = robots.copy()

    # collect materials
    for key in robots.keys():
        new_resources[key] += robots[key]

    # build nothing
    if minute < 24:
        max_geodes = max(max_geodes, recursive_soln(
            blueprint, new_robots, new_resources, minute + 1))

    return max_geodes


def part_one():
    arr = parse_newline_delimited_array('2022/19-example.in', get_robot_parts)
    robots = {
        "ore": 1,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
    }
    resources = {
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
    }

    # maybe there are two sub problems:
    # - at specific times, how many robots of what type can you have?

    for blueprint in arr[:1]:
        print(recursive_soln(blueprint, robots, resources, 0))

    # print(arr)


def part_two():
    arr = parse_newline_delimited_array('2022/19-example.in', lambda e: int(e))
    # arr = parse_newline_delimited_array('2022/19.in', lambda e: int(e))


part_one()
# part_two()
