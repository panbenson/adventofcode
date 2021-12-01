def main():
  code = open("3.in", "r")
  wires = []
  for line in code:
    wires.append(line.strip().split(","))

  center = 10000
  # lets assume 5k by 5k is large enough
  board = [[0 for i in range(center * 2 + 1)] for x in range(center * 2 + 1)] # center point at 2500, 2500
  closest_x = closest_y = 0
  curr_x = curr_y = center

  # modifications for part 2: we track steps, then compare
  steps = 1
  for move in wires[0]:
    dir = move[0]
    dist = int(move[1:])

    if dir == 'R':
      for x in range(curr_x + 1, curr_x + dist + 1):
        board[x][curr_y] = steps
        steps += 1
      curr_x += dist
    elif dir == 'L':
      for x in range(curr_x - 1, curr_x - dist - 1, -1):
        board[x][curr_y] = steps
        steps += 1
      curr_x -= dist
    elif dir == 'U':
      for y in range(curr_y + 1, curr_y + dist + 1):
        board[curr_x][y] = steps
        steps += 1
      curr_y += dist
    else:
      for y in range(curr_y - 1, curr_y - dist - 1, -1):
        board[curr_x][y] = steps
        steps += 1
      curr_y -= dist

  board[center][center] = 0
  curr_x = curr_y = center
  steps = 1
  fewest = -1

  for move in wires[1]:
    dir = move[0]
    dist = int(move[1:])

    if dir == 'R':
      for x in range(curr_x + 1, curr_x + dist + 1):
        if board[x][curr_y] != 0 and (fewest == -1 or fewest > steps + board[x][curr_y]): # abs(closest_x - center) + abs(closest_y - center) > abs(x - center) + abs(curr_y - center):
          print("crossed", x, curr_y, fewest)
          fewest = steps + board[x][curr_y]
          closest_x = x
          closest_y = curr_y
        steps += 1
      curr_x += dist
    elif dir == 'L':
      for x in range(curr_x - 1, curr_x - dist - 1, -1):
        if board[x][curr_y] != 0 and (fewest == -1 or fewest > steps + board[x][curr_y]): # abs(closest_x - center) + abs(closest_y - center) > abs(x - center) + abs(curr_y - center):
          print("crossed", x, curr_y, fewest)
          fewest = steps + board[x][curr_y]
          closest_x = x
          closest_y = curr_y
        steps += 1
      curr_x -= dist
    elif dir == 'U':
      for y in range(curr_y + 1, curr_y + dist + 1):
        if board[curr_x][y] != 0 and (fewest == -1 or fewest > steps + board[curr_x][y]): # abs(closest_x - center) + abs(closest_y - center) > abs(curr_x - center) + abs(y - center):
          print("crossed", curr_x, y, fewest)
          fewest = steps + board[curr_x][y]
          closest_x = curr_x
          closest_y = y
        steps += 1
      curr_y += dist
    else:
      for y in range(curr_y - 1, curr_y - dist - 1, -1):
        if board[curr_x][y] != 0 and (fewest == -1 or fewest > steps + board[curr_x][y]): # abs(closest_x - center) + abs(closest_y - center) > abs(curr_x - center) + abs(y - center):
          print("crossed", curr_x, y, fewest)
          fewest = steps + board[curr_x][y]
          closest_x = curr_x
          closest_y = y
        steps += 1
      curr_y -= dist

  # print(abs(closest_x - center) + abs(closest_y - center))
  print(fewest)

main()
