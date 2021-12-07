# https://adventofcode.com/2021/day/4
def parse_input(input_file):
    with open(input_file, 'r') as reader:
        nums = [line.strip('\n') for line in reader]

        bingo = [int(num) for num in nums[0].split(',')]

        boards = []
        board = []
        for row in nums[2:]:
            if row == '':
                boards.append(board)
                board = []
            else:
                board.append([int(i)
                              for i in row.strip().split(' ') if i != ''])
        boards.append(board)

    return bingo, boards


def day_four(input_file):
    bingo, boards = parse_input(input_file)

    for num in bingo:
        # print('checking', num)
        for board in boards:
            mark_number(board, num)

        for board in boards:
            if check_winner(board):
                # print('winner!!!', board)
                print(sum_unmarked(board) * num)
                return


def check_winner(board):
    for row in board:
        if ''.join([str(i) for i in row]) == 'X' * len(board):
            return True

    for col in range(len(board[0])):
        if ''.join([str(row[col]) for row in board]) == 'X' * len(board):
            return True


def mark_number(board, num):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == num:
                board[row][col] = 'X'


def sum_unmarked(board):
    sum = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 'X':
                sum += board[row][col]

    return sum


def day_four_p2(input_file):
    bingo, boards = parse_input(input_file)

    winners = set()
    for num in bingo:
        # print('checking', num)
        for board in boards:
            mark_number(board, num)

        for board in range(len(boards)):
            if check_winner(boards[board]):
                if len(winners) == len(boards) - 1 and board not in winners:
                    print(sum_unmarked(boards[board]) * num)
                    return
                winners.add(board)


def main():
    # input_file = '4-example.in'
    input_file = '4.in'
    day_four(input_file)
    day_four_p2(input_file)


main()
