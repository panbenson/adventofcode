# https://adventofcode.com/2021/day/8
import read_input


def day_eight(input_file):
    with open(input_file, 'r') as reader:
        lines = [line.strip('\n').split('|') if line !=
                 '\n' else [] for line in reader]
    count = 0

    for line in lines:
        code = line[1].strip().split(' ')

        for num in code:
            if len(num) == 2 or len(num) == 3 or len(num) == 7 or len(num) == 4:
                count += 1

    print(count)


def day_eight_p2(input_file):
    with open(input_file, 'r') as reader:
        lines = [line.strip('\n').split('|') if line !=
                 '\n' else [] for line in reader]

    sum = 0

    for line in lines:
        digits = line[0].strip().split(' ')
        code = line[1].strip().split(' ')

        decoded = {}

        # seven has 3 segments
        seven = [i for i in digits if len(i) == 3][0]
        decoded[''.join(sorted(seven))] = 7

        # four has 4 segments
        four = [i for i in digits if len(i) == 4][0]
        decoded[''.join(sorted(four))] = 4

        # one has 2 segments
        one = [i for i in digits if len(i) == 2][0]
        decoded[''.join(sorted(one))] = 1

        # eight has all segments
        eight = [i for i in digits if len(i) == 7][0]
        decoded[''.join(sorted(eight))] = 8

        # nine has 6 segments including four
        nine = [i for i in digits if len(
            i) == 6 and len(set(i) & set(four)) == 4][0]
        decoded[''.join(sorted(nine))] = 9

        # zero has 6 segment including 1 not 4
        zero = [i for i in digits if len(i) == 6 and len(
            set(i) & set(four)) == 3 and len(set(i) & set(one)) == 2][0]
        decoded[''.join(sorted(zero))] = 0

        # six is the other one
        six = [i for i in digits if len(i) == 6 and i != zero and i != nine][0]
        decoded[''.join(sorted(six))] = 6

        # five is 6 intersect 9 nice
        five = [i for i in digits if len(i) == 5 and set(
            i) == (set(six) & set(nine))][0]
        decoded[''.join(sorted(five))] = 5

        # three has 5 segments including 1
        three = [i for i in digits if len(i) == 5 and len(
            set(i) & set(one)) == 2 and len(set(i) & set(four)) == 3][0]
        decoded[''.join(sorted(three))] = 3

        seven_seg = {}
        seven_seg['d'] = list(set(eight) - set(zero))[0]
        seven_seg['c'] = list(set(eight) - set(six))[0]
        seven_seg['e'] = list(set(eight) - set(nine))[0]

        seven_seg['b'] = list(set(four) - set(one) - set([seven_seg['d']]))[0]
        seven_seg['f'] = list(set(one) - set([seven_seg['c']]))[0]
        seven_seg['a'] = list(set(seven) - set(one))[0]
        seven_seg['g'] = list(set(eight) - set(seven_seg.values()))[0]

        # two is the last one
        two = [i for i in digits if i not in decoded][0]
        decoded[''.join(
            sorted(list(set(eight) - set([seven_seg['b']]) - set([seven_seg['f']]))))] = 2

        sum += int(''.join([str(decoded[''.join(sorted(num))])
                            for num in code]))

    print(sum)


def main():
    # input_file = '8-example.in'
    input_file = '8.in'
    day_eight(input_file)
    day_eight_p2(input_file)


main()
