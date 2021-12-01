from collections import defaultdict

def dfs(orbit, closed, current, depth):
  return sum([depth + dfs(orbit, closed + [current], next, depth + 1) for next in orbit[current] if next not in closed])

def bfs(orbit, start, end):
  q = [(0, start)]
  closed = []

  while len(q):
    (cost, planet) = q.pop(0)
    if planet == end:
      return cost - 2
    
    for i in orbit[planet]:
      if i in closed:
        continue
      q.append((cost + 1, i))

    closed.append(planet)
    q = sorted(q, key=lambda item: item[0])

def main():
  example = open("6.in", "r")

  # build the graph
  orbit = defaultdict(list)

  for line in example:
    a, b = line.strip().split(")")
    orbit[a].append(b)
    orbit[b].append(a)

  # part 1
  print(dfs(orbit, [], "COM", 1))

  # part 2
  print(bfs(orbit, "YOU", "SAN"))


main()
