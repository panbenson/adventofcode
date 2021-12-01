from collections import defaultdict
def main():
  image = ""
  code = open("8.in", "r")
  for line in code:
    image = line.strip()

  layers = []
  layer_num = 0
  data_frame = 25 * 6
  while layer_num*data_frame < len(image):
    m = defaultdict(int)
    for digit in image[layer_num*data_frame:(layer_num + 1)*data_frame]:
      m[digit] += 1
    layers.append(m)
    layer_num += 1


  # part 1
  # layers = sorted(layers, key=lambda m: m["0"])
  fewest_zeros = layers[0]
  print(fewest_zeros)
  print(fewest_zeros['1'] * fewest_zeros['2'])

  # part 2
  # from the top down, we find the first non-two
  for i in range(data_frame):
    # new line if its the width = 25
    if i % 25 == 0:
      print()
    layer = 0

    while image[layer * data_frame + i] == '2':
      layer += 1
    if image[layer * data_frame + i] == '1':
      print('X', end='')
    else:
      print(' ', end='')
  print('\n')



main()
