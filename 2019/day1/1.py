import math

def load_input():
  code = open("1.in", "r")
  copy = []
  for line in code:
    copy += map(int, line.strip().split(","))

  return copy

def recurse(amount):
  if amount < 0:
    return 0

  return amount + recurse(math.floor(amount/3) - 2)

def main():
  modules = load_input()
  # part 1
  print(sum([ math.floor(mod/3) - 2 for mod in modules ]))

  # part 2 
  print(sum([ recurse(math.floor(mod/3) - 2) for mod in modules ]))


main()
