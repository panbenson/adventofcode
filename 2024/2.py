from collections import defaultdict
import copy
import sys
import re
import math

def day_2_1():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        reports = []
        for line in file:
            row = line.strip().split(' ')
            reports.append(list(map(int, row)))

        count = 0
        for report in reports:
            increasing = False
            decreasing = False
            prev = report[0]
            safe = True


            for level in report[1:]:
                if not increasing and not decreasing:
                    if level > prev:
                        increasing = True
                    else:
                        decreasing = True

                difference = level - prev
                prev = level
                if increasing and difference >= 1 and difference <= 3:
                    continue
                elif decreasing and difference >= -3 and difference <= -1:
                    continue
                else:
                    safe = False
                    break
            print("Safe" if safe else "Unsafe")
            if safe:
                count += 1

        print("Safe reports:", count)


def check_safety(report):
    increasing = False
    decreasing = False
    prev = report[0]
    safe = True


    for level in report[1:]:
        if not increasing and not decreasing:
            if level > prev:
                increasing = True
            else:
                decreasing = True

        difference = level - prev
        prev = level
        if increasing and difference >= 1 and difference <= 3:
            continue
        elif decreasing and difference >= -3 and difference <= -1:
            continue
        else:
            safe = False
            break

    return safe


def day_2_2():
    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        reports = []
        for line in file:
            row = line.strip().split(' ')
            reports.append(list(map(int, row)))

        count = 0
        for report in reports:
            if check_safety(report):
                count += 1
            else:
                # just try every possible option
                for i in range(len(report)):
                    if check_safety(report[:i] + report[i+1:]):
                        count += 1
                        break

        print("Safe reports:", count)



# day_2_1()
day_2_2()
