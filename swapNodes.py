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
class Node:
    def __init__(self, val, level=0):
        self.val = val
        self.left = None
        self.right = None
        self.level = level

def levels2tree(levels):
    root = Node(1, 1)    
    leafs = [root] 
    for li, level in enumerate(levels):        
        nodes = [node for node in level]
        while len(nodes) > 0:                                       
            curr = leafs.pop(0)            
            if curr.val > 0:
                left, right = nodes.pop(0)
                level_ = li + 2
                curr.left = Node(left, level_)
                curr.right = Node(right, level_)
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

def swap(root, qs):
    path = [root]
    while len(path) > 0:
        curr = path.pop(0)        
        if curr.level in qs:
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
        
        if curr.left is not None: path.append(curr.left)
        if curr.right is not None: path.append(curr.right)
        
    return root
            
def swapNodes(indexes, queries):
    results = []
    levels = indexes2leves(indexes)    
    root = levels2tree(levels)    

    n = len(levels)
    queries_exp = [ [ i for i in range(q, n, q) ] for q in queries] 

    for qs in queries_exp:
        root = swap(root, qs)            
        results.append(in_orden(root))
    return results

indexes= [ [2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], 
           [10, 11], [12, 13], [-1, 14], [-1, -1],
           [15, -1], [16, 17], [-1, -1], [-1, -1],
           [-1, -1], [-1, -1], [-1, -1],[-1, -1] ]

queries = [2, 3]

result = swapNodes(indexes, queries)
for res in result: print(res)



