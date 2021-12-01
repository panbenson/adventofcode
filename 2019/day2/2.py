def int_code_computer(prog):
  ins = 0
  line_width = 4

  while ins * line_width < len(prog):
    if prog[ins * line_width] == 1:
      # addition
      prog[prog[ins * line_width + 3]] = prog[prog[ins * line_width + 2]] + prog[prog[ins * line_width + 1]]
    elif prog[ins * line_width] == 2:
      # multiplication
      prog[prog[ins * line_width + 3]] = prog[prog[ins * line_width + 2]] * prog[prog[ins * line_width + 1]]
    elif prog[ins * line_width] == 99:
      break
    else:
      print("error in program!")
    
    ins += 1

def compile_int_code_program(prog):
  ins = 0
  line_width = 4

  while ins * line_width < len(prog):
    if prog[ins * line_width] == 1:
      # addition
      prog[prog[ins * line_width + 3]] = f'({prog[prog[ins * line_width + 2]]} + {prog[prog[ins * line_width + 1]]})'
    elif prog[ins * line_width] == 2:
      # multiplication
      prog[prog[ins * line_width + 3]] = f'({prog[prog[ins * line_width + 2]]} * {prog[prog[ins * line_width + 1]]})'
    elif prog[ins * line_width] == 99:
      break
    else:
      print("error in program!")
    
    ins += 1

def load_program():
  code = open("2.in", "r")
  copy = []
  for line in code:
    copy += map(int, line.strip().split(","))

  return copy

def main():
  # part 1
  program = load_program()
  program[1] = 12
  program[2] = 2
  int_code_computer(program)

  print(program[0])

  # part 2
  # brute force the answer 0 - 99
  for n in range(100):
    for v in range(100):
      program = load_program()
      program[1] = n
      program[2] = v
      int_code_computer(program)

      if program[0] == 19690720:
        print(n, v)
        break

main()
