from parser import parse_raw_newline_delimited_groups


def parse_monkey(arr):
    monkey = int(arr[0].split()[1][:-1])
    operation_parts = arr[2].split(' = old ')[1].split()

    def operation_operand(x): return x if operation_parts[1] == 'old' else int(
        operation_parts[1])

    def test(x): return int(arr[4].split(' monkey ')[1]) if x % (
        int(arr[3].split(' by ')[1])) == 0 else int(arr[5].split(' monkey ')[1])

    return {
        "monkey": monkey,
        "items": list(map(int, arr[1].split(': ')[1].split(', '))),
        "operation": lambda x: (x + operation_operand(x)) if operation_parts[0] == '+' else (x * operation_operand(x)),
        "test": test
    }


def part_one():
    raw_monkeys = parse_raw_newline_delimited_groups(
        '2022/11-example.in', lambda e: e)
    raw_monkeys = parse_raw_newline_delimited_groups(
        '2022/11.in', lambda e: e)
    monkeys = list(map(parse_monkey, raw_monkeys))
    monkey_dict = {monkey["monkey"]: monkey for monkey in monkeys}
    monkey_inspects = {monkey["monkey"]: 0 for monkey in monkeys}

    for rounds in range(20):
        for monkey in monkey_dict.keys():
            for item in monkey_dict[monkey]["items"]:
                print(f"current worry: {item}")
                new = monkey_dict[monkey]["operation"](item)
                print(f"new worry: {new}")
                bored = new // 3
                print(f"after bored worry: {bored}")
                throw_to = monkey_dict[monkey]["test"](bored)
                print(f">>>> throw item {bored} to {throw_to}")
                monkey_dict[throw_to]["items"].append(bored)
                monkey_inspects[monkey] += 1
            monkey_dict[monkey]["items"] = []
            print()

    inspects = sorted(monkey_inspects.values())

    print(monkeys, monkey_inspects,
          inspects[-1] * inspects[-2])


def get_mod(raw_monkeys):
    modulo = 1
    for arr in raw_monkeys:
        modulo *= int(arr[3].split(' by ')[1])

    return modulo


def part_two():
    raw_monkeys = parse_raw_newline_delimited_groups(
        '2022/11-example.in', lambda e: e)
    raw_monkeys = parse_raw_newline_delimited_groups(
        '2022/11.in', lambda e: e)
    monkeys = list(map(parse_monkey, raw_monkeys))
    monkey_dict = {monkey["monkey"]: monkey for monkey in monkeys}
    monkey_inspects = {monkey["monkey"]: 0 for monkey in monkeys}

    # a bit brute-forcey, but we could prob just modulo the product
    # of the divisible, theres prob some better math tricks tho...
    modulo = get_mod(raw_monkeys)

    for rounds in range(10000):
        for monkey in monkey_dict.keys():
            for item in monkey_dict[monkey]["items"]:
                new = monkey_dict[monkey]["operation"](item)
                bored = new % modulo
                throw_to = monkey_dict[monkey]["test"](bored)
                monkey_dict[throw_to]["items"].append(bored)
                monkey_inspects[monkey] += 1
            monkey_dict[monkey]["items"] = []
        print(f'after round {rounds + 1}: {monkey_inspects}')

    inspects = sorted(monkey_inspects.values())

    print(monkeys, monkey_inspects,
          inspects[-1] * inspects[-2])


# part_one()
part_two()
