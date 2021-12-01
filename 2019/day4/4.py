from collections import defaultdict

def main():
  counter = 0

  for i in range(231832, 767346 + 1):
    prev = -1
    num = i * 10
    digit = 6
    repeated = defaultdict(int)
    # adj_eq = False

    while digit > 0 and prev <= num // (10 ** digit) % 10:
      if prev == num // (10 ** digit) % 10:
        repeated[prev] += 1
        # adj_eq = True
      prev = num // (10 ** digit) % 10
      digit -= 1

    if digit == 0 and 1 in repeated.values(): # adj_eq:
      print(i)
      counter += 1

  print(counter)


main()
