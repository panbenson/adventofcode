class Cup:
    def __init__(self, num, next):
        self.num = num
        self.next = next


def day_twenty_three_part_one():
    # example
    # cups = [int(n) for n in list("389125467")]
    # real
    cups = [int(n) for n in list("315679824")]
    cups_map = {}

    for cup in cups:
        cups_map[cup] = Cup(cup, None)

    for i in range(len(cups)):
        cups_map[cups[i]].next = cups_map[cups[(i + 1) % (len(cups))]]

    curr = cups_map[3]

    for i in range(100):
        slice_head = curr.next
        slice_end = curr.next.next.next
        picked_up = set([slice_head.num, slice_head.next.num, slice_end.num])

        destination = curr.num - 1 if curr.num - 1 > 0 else 9
        while destination in picked_up:
            destination = destination - 1 if destination - 1 > 0 else 9

        print('current cup:', curr.num, '\npickedup:',
              picked_up, '\ndestination:', destination)
        curr.next = slice_end.next
        destination_next = cups_map[destination].next
        cups_map[destination].next = slice_head
        slice_end.next = destination_next

        curr = curr.next

    # order after cup 1
    curr = cups_map[1].next
    order = []
    while curr.num != 1:
        order.append(str(curr.num))
        curr = curr.next
    print(''.join(order))


day_twenty_three_part_one()
