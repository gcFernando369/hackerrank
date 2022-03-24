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

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levels2tree(levels):
    root = Node(1)    
    leafs = [root] 
    for level in levels:        
        nodes = [node for node in level]
        while len(nodes) > 0:                                       
            curr = leafs.pop(0)            
            if curr.val > 0:
                left, right = nodes.pop(0)
                curr.left = Node(left)
                curr.right = Node(right)
                leafs.append(curr.left)
                leafs.append(curr.right)  
    return root

def in_orden(root):
    vals = []
    path = [root]
    current = root.left
    
    while True:        
        if current.val != -1:
            path.append(current)
            current = current.left
        else:
            if len(path) == 0: break
            current = path.pop()
            vals.append(current.val)            
            current = current.right
                
    return vals
            
def swapNodes(indexes, queries):
    results = []
    levels = indexes2leves(indexes)
    n = len(levels)
    queries_exp = [ [ i for i in range(q, n, q) ] for q in queries] 

    print(levels)
    for qs in queries_exp:
        levels = swap(levels, qs)    
        print(levels)
        root = levels2tree(levels)
        results.append(in_orden(root))
    return results


indexes = [ [2, 3], [4, -1], [5, -1], [6, -1],
            [7, 8], [-1, 9], [-1, -1], [10, 11],
            [-1, -1], [-1, -1], [-1, -1] ]

queries = [2, 4]
"""
indexes= [ [2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], 
           [10, 11], [12, 13], [-1, 14], [-1, -1],
           [15, -1], [16, 17], [-1, -1], [-1, -1],
           [-1, -1], [-1, -1], [-1, -1],[-1, -1] ]

queries = [2, 3]
"""
result = swapNodes(indexes, queries)
for res in result: print(res)



