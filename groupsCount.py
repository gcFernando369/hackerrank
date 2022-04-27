def countGroups(related):
    n = 0
    h = len(related)
    nodes = list(range(h))    

    while len(nodes) > 0:
        node = nodes.pop(0)
        to_explore = [node]
        explored = []

        while len(to_explore) > 0:
            i = to_explore.pop(0)
            for j, val in enumerate(related[i]):
                if j != i and val > 0:
                    if not (j in explored or j in to_explore):
                        to_explore.append(j)
                        del nodes[nodes.index(j)]
            explored.append(i)
        n+=1
    return n

#x = [[1,1,0],[1,1,0],[0,0,1]]
x = [[1,1,0,0,0,0],
     [1,1,1,0,0,0],
     [0,1,1,0,0,0],
     [0,0,0,1,1,0],
     [0,0,0,1,1,0],
     [0,0,0,0,0,1]]
print(countGroups(x))