def rooted(graph: list, node_1: int, node_2: int) -> bool:
  to_search = [node_1]
  visited_1 = {}
  n = len(graph[0])
  
  while len(to_search) > 0:
    next = to_search.pop(0)
    if not (next in visited_1.keys()):
      visited_1[next] = True
      for i in range(n):
        if graph[i][next]: to_search.append(i)
  
  to_search = [node_2]
  visited_2 = {}

  while len(to_search) > 0:
    next = to_search.pop(0)
    if next in visited_1.keys():
      return next
    if not (next in visited_2.keys()):
      visited_2[next] = True
      for i in range(n):
        if graph[i][next]: to_search.append(i)

  return None

graph = [
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
]

print(rooted(graph, 3, 2))