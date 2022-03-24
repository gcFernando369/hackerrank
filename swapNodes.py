def indexes2leves(indexes):
    levels = []
    start, end = 0, 1
    while True:               
        nodes = indexes[start:end]
        levels.append(nodes)        
        start = end
        for node in nodes:
            left, right = node            
            if left > 0: end += 1
            if right > 0: end += 1        
        if start == end: break
    return levels

def swap(levels, qs):
    for q in qs:
        k = q-1
        nodes = levels[k]        
        levels[k] = [ [node[1], node[0]] for node in nodes ]        
    return levels
            
def swapNodes(indexes, queries):
    results = []
    levels = indexes2leves(indexes)
    n = len(levels)

    queries_exp = [ [ i for i in range(q, n, q) ] for q in queries]

    print(levels)
    for qs in queries_exp:
        levels = swap(levels, qs)
        print(levels)
    
    return results


indexes = [ [2, 3], [4, -1], [5, -1], [6, -1],
            [7, 8], [-1, 9], [-1, -1], [10, 11],
            [-1, -1], [-1, -1], [-1, -1] ]

queries = [2, 4]

result = swapNodes(indexes, queries)
#print(result)