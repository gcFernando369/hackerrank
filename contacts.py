class Node:
    def __init__(self, value, count=0):
        self.value = value
        self.count = count
        self.childs = {}

class Tree:
    def __init__(self):
        self.root = Node('*')
    
    def add_name(self, name):
        current = self.root
        for item in name:
            if item in current.childs: current.childs[item].count += 1
            else: current.childs[item] = Node(item, 1)
            current = current.childs[item]
            
    def find(self, prefix):
        current = self.root
        for item in prefix:
            if item in current.childs:
                current = current.childs[item]
            else: return 0
        return current.count

def contacts(queries):
    t = Tree()
    counts = []
    for query in queries:
        op, s = query
        if op == 'add': t.add_name(s)
        else: counts.append(t.find(s))
    return counts