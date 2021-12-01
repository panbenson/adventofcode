mod = 20201227


def find_loop_size(subject_number: int, key: int):
    # find the card's loop size
    count = 0
    loop = 1
    while loop != key:
        count += 1
        loop *= subject_number
        loop %= mod

    return count


def find_encryption_key(subject_number: int, loop: int):
    res = 1
    for i in range(loop):
        res *= subject_number
        res %= mod
    return res


def day_twenty_five_part_one():
    card_example = 5764801
    card_pub = 3469259
    door_example = 17807724
    door_pub = 13170438

    # from question
    subject_number = 7
    card_loop = find_loop_size(subject_number, card_pub)
    door_loop = find_loop_size(subject_number, door_pub)

    # # encryption key
    subject_number = card_pub
    encryption_key = find_encryption_key(subject_number, door_loop)
    print(encryption_key)


day_twenty_five_part_one()
