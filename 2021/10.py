# https://adventofcode.com/2021/day/10
import read_input


def get_score(bracket):
    if bracket == ')':
        return 3
    elif bracket == ']':
        return 57
    elif bracket == '}':
        return 1197
    else:
        return 25137


def day_ten(input_file):
    lines = read_input.parse_lines(input_file)

    total = 0
    for line in lines:
        queue = []
        for bracket in line:
            if bracket in ['[', '(', '{', '<']:
                queue.append(bracket)
            else:
                if queue[-1] == '(' and bracket == ')' or queue[-1] == '[' and bracket == ']' or queue[-1] == '{' and bracket == '}' or queue[-1] == '<' and bracket == '>':
                    queue = queue[:-1]
                else:
                    total += get_score(bracket)
                    break

    print(total)


def day_ten_p2(input_file):
    lines = read_input.parse_lines(input_file)

    total = 0
    incomplete = []
    for line in lines:
        queue = []
        stopped = False
        for bracket in line:
            if bracket in ['[', '(', '{', '<']:
                queue.append(bracket)
            else:
                if queue[-1] == '(' and bracket == ')' or queue[-1] == '[' and bracket == ']' or queue[-1] == '{' and bracket == '}' or queue[-1] == '<' and bracket == '>':
                    queue = queue[:-1]
                else:
                    total += get_score(bracket)
                    stopped = True
                    break
        if len(queue) and not stopped:
            incomplete.append(queue)

    scores = []
    for remaining in incomplete:
        score = 0
        for bracket in reversed(remaining):
            if bracket == '(':
                score = score * 5 + 1
            elif bracket == '[':
                score = score * 5 + 2
            elif bracket == '{':
                score = score * 5 + 3
            else:
                score = score * 5 + 4

        scores.append(score)
    scores.sort()
    print(scores[len(scores)/2])


def main():
    input_file = '10-example.in'
    input_file = '10.in'
    day_ten(input_file)
    day_ten_p2(input_file)


main()
