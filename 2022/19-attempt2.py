from parser import parse_newline_delimited_array
import re
import copy

def get_robot_parts(e):
    match = re.search(r'Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', e)
    return (int(match.group(1)), int(match.group(2)), (int(match.group(3)), int(match.group(4))), (int(match.group(5)), int(match.group(6))))

def tick(robots, resources):
    new_resources = copy.deepcopy(resources)
    for key in new_resources:
        new_resources[key] += robots[key]
    return new_resources

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

    for blueprint in arr:
        visited = set()
        horizon = [(0, copy.deepcopy(robots), copy.deepcopy(resources))]

        while horizon:
            time, robo, res = horizon.pop()
            if time == 24:
                continue
            visited.add((time, robo.values(), res.values()))

            # print(blueprint)
            possible_robots = []
            # buy robots if possible
            if res['ore'] >= blueprint[0]:
                print('clay bot')
                new_robots = copy.deepcopy(robo)
                new_robots['clay'] += 1
                possible_robots.append(new_robots)
                new_resources = copy.deepcopy(res)
                new_resources['ore'] -= blueprint[0]
                new_resources = tick(robo, new_resources)
                if (time+1,new_robots.values(),new_resources.values()) not in visited:
                    horizon.append((time + 1, new_robots, new_resources))
                print(time + 1, new_robots, new_resources)

            # also do nothing
            new_resources = tick(robo, res)
            if (time+1,robo.values(),new_resources.values()) not in visited:
                horizon.append((time + 1, copy.deepcopy(robo),new_resources))
            print(time + 1, copy.deepcopy(robo), tick(robo, res))

part_one()

    # for blueprint in arr[:1]:
    #     print(recursive_soln(blueprint, robots, resources, 0))
