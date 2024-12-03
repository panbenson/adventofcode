import sys

def day_1_1():
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        sum = 0
        for line in file:
            text = line.strip()
            calibration_value = ''

            # first number
            i = 0
            while not (text[i] >= '0' and text[i] <= '9'):
                i += 1
            calibration_value += text[i]

            # second number
            i = -1
            while not (text[i] >= '0' and text[i] <= '9'):
                i -= 1
            calibration_value += text[i]

            sum += int(calibration_value)

    print(f"sum: {sum}")


def check_spelt_with_letters(text, i):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for num in numbers:
        if text[i:].find(num) == 0:
            return num


spelt_to_str = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def day_1_2():
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        sum = 0
        for line in file:
            text = line.strip()
            calibration_value = ''

            # first number
            i = 0
            while not (text[i] >= '0' and text[i] <= '9') and not check_spelt_with_letters(text, i):
                i += 1
            spelt_num = check_spelt_with_letters(text, i)
            calibration_value += text[i] if not spelt_num else spelt_to_str[spelt_num]

            # second number
            i = len(text) - 1
            while not (text[i] >= '0' and text[i] <= '9') and not check_spelt_with_letters(text, i):
                i -= 1
            spelt_num = check_spelt_with_letters(text, i)
            calibration_value += text[i] if not spelt_num else spelt_to_str[spelt_num]

            print(f"{text} --> {calibration_value}")

            sum += int(calibration_value)

    print(f"sum: {sum}")

day_1_2()
