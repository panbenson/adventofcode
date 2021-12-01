import itertools

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

def int_code_computer_two_input(prog, last_ins, phase, signal):
  ins = last_ins
  input_prompt = 0
  output_val = 0

  while ins < len(prog):
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
      # prog[val1] = int(input("waiting input: "))
      if input_prompt == 0:
        prog[val1] = phase
      else:
        prog[val1] = signal
      input_prompt += 1
      ins += 2
    elif opcode == 4:
      # output at position
      return ins, prog[val1]
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
    elif opcode == 99:
      return ins, output_val
      break
    else:
      print("error in program!")



def amplifier_controller_software():
  p = [list(p) for p in itertools.permutations([0, 1, 2, 3, 4], 5)]
  max_signal = 0

  for seq in p:
    # for each sequence, calculate the final_output
    signal = 0

    for phase in seq:
      # laod program
      code = open("7.in", "r")
      for line in code:
        program = list(map(int,line.strip().split(",")))

      _, signal = int_code_computer_two_input(program, 0, phase, signal)

    if max_signal < signal:
      max_signal = signal

  print(max_signal)


def amplifier_controller_software_feedback():
  p = [list(p) for p in itertools.permutations([5, 6, 7, 8, 9], 5)]
  max_signal = 0

  for seq in p:
    # for each sequence, calculate the final_output
    signal = 0
    ins = 0

    # keep looping the same signal until we get the signal to stop

    # laod program
    code = open("p2example.in", "r")
    for line in code:
      program = list(map(int,line.strip().split(",")))
    while True:
      for phase in seq:
        ins, signal = int_code_computer_two_input(program, ins, phase, signal)
        if max_signal < signal:
          max_signal = signal
        print(max_signal)
      

    if max_signal < signal:
      max_signal = signal

  print(max_signal)

def main():
  amplifier_controller_software()
  amplifier_controller_software_feedback()

main()
