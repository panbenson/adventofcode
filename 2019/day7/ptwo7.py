import itertools

def int_code_computer_two_input(prog, start_ins, signal):
  ins = start_ins
  input_prompt = 0

  while ins < len(prog):
    opcode = prog[ins] % 100

    if opcode == 99:
      return -1, -1

    # find the modes of 3 parameters
    mode3 = (prog[ins] // 10000 % 10) != 0
    mode2 = (prog[ins] // 1000 % 10) != 0
    mode1 = (prog[ins] // 100 % 10) != 0

    # find the 3 parameters
    if opcode in [1, 2, 7, 8]:
      val3 = ins + 3 if mode3 else prog[ins + 3]
    if opcode in [1, 2, 5, 6, 7, 8]:
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
      prog[val1] = signal[input_prompt]
      input_prompt += 1
      ins += 2
    elif opcode == 4:
      # output at position
      return ins + 2, prog[val1]
    # jumps
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
    # end jumps
    else:
      print("error in program!")

def amplifier_controller_software():
  p = [list(p) for p in itertools.permutations([5, 6, 7, 8, 9], 5)]
  max_signal = 0

  for seq in p:
    # for each sequence, calculate the final_output
    signal = 0
    program = []
    input_phase = 1

    # laod program
    code = open("7.in", "r")
    for line in code:
      program = list(map(int,line.strip().split(",")))

    saved_programs = [list(program) for i in range(5)]
    ins_ptr = [0 for i in range(5)]
    halted = False

    while not halted:
      # actually do the feedback
      for idx, phase in enumerate(seq):
        ins, signal = int_code_computer_two_input(saved_programs[idx], ins_ptr[idx], [phase, signal] if input_phase else [signal])

        if signal == -1:
          halted = True
          break

        ins_ptr[idx] = ins

      if max_signal < signal:
        max_signal = signal
      input_phase = 0

  print(max_signal)

amplifier_controller_software()
