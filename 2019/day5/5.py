def int_code_computer(prog):
  ins = 0

  while ins < len(prog):
    # print(prog[ins], prog[ins + 1], prog[ins + 2], prog[ins + 3])
    # day 5 changes
    opcode = prog[ins] % 100
    # find the modes of 3 parameters
    mode3 = (prog[ins] // 10000 % 10) != 0
    mode2 = (prog[ins] // 1000 % 10) != 0
    mode1 = (prog[ins] // 100 % 10) != 0

    # find the 3 parameters
    val3 = ins + 3 if mode3 else prog[ins + 3]
    val2 = ins + 2 if mode2 else prog[ins + 2]
    val1 = ins + 1 if mode1 else prog[ins + 1]

    if opcode == 1:
      # addition
      prog[val3] = prog[val2] + prog[val1]
      ins += 4
    elif opcode == 2:
      # multiplication
      prog[val3] = prog[val2] * prog[val1]
      ins += 4
    # changes for day 5
    elif opcode == 3:
      # save to position
      prog[val1] = int(input("waiting input: "))
      ins += 2
    elif opcode == 4:
      # output at position
      print(prog[val1])
      ins += 2
    elif opcode == 5:
      if prog[val1] != 0:
        ins = prog[val2]
      else:
        ins += 3
    elif opcode == 6:
      if prog[val1] == 0:
        ins = prog[val2]
      else:
        ins += 3
    elif opcode == 7:
      if prog[val1] < prog[val2]:
        prog[val3] = 1
      else:
        prog[val3] = 0
      ins += 4
    elif opcode == 8:
      if prog[val1] == prog[val2]:
        prog[val3] = 1
      else:
        prog[val3] = 0
      ins += 4
    # 5: jump if true (check first, jump second)
    # 6: jump if false(check first, jump second)
    # 7: first less than 2 ? 1 in 3rd : 0
    # 8: first equals 2 ? 1 in 3rd : 0
    elif opcode == 99:
      break
    else:
      print("error in program!")

def load_program():
  code = open("2.in", "r")
  copy = []
  for line in code:
    copy += map(int, line.strip().split(","))

  return copy

def main():
  code = open("5.in", "r")
  for line in code:
    program = list(map(int,line.strip().split(",")))

  int_code_computer(program)
  # part 2
  # brute force the answer 0 - 99
  # for n in range(100):
  #   for v in range(100):
  #     program = load_program()
  #     program[1] = n
  #     program[2] = v
  #     int_code_computer(program)

  #     if program[0] == 19690720:
  #       print(n, v)
  #       break

main()
