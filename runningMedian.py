class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.hl = 0
        self.hr = 0

class Heap:
    def __init__(self, value, op):
        self.root = Node(value)
        self.op = op
        self.deleted = 0

    def shift(self, a, b):
        c = a.value
        a.value = b.value
        b.value = c
        return a, b
    
    def add(self, value):
        current = self.root
        new_node = Node(value)
        
        while True:
            if self.op == '>': comp = new_node.value >= current.value
            elif self.op == '<': comp = new_node.value < current.value
            else: break

            if comp: current, new_node = self.shift(current, new_node)
            else:                
                if current.hl <= current.hr:
                    current.hl += 1
                    if current.left is not None: current = current.left                        
                    else:                        
                        current.left = new_node
                        break
                else:   
                    current.hr += 1         
                    if current.right is not None: current = current.right
                    else:
                        current.right = new_node
                        break

    def comp(self, a, b):        
        best = None
        if self.op == '>': best = a if a.value >= b.value else b
        elif self.op == '<': best = a if a.value < b.value else b
        return best

    def fit_root(self):
        self.deleted += 1
        current = self.root
        while True:            
            to_comp = []
            if current.left is not None: to_comp.append(current.left)
            if current.right is not None: to_comp.append(current.right)
            if len(to_comp) == 0: break
            elif len(to_comp) == 1: best = to_comp[0]
            else: best = self.comp(to_comp[0], to_comp[1])

            if self.op == '>': comp = best.value >= current.value
            elif self.op == '<': comp = best.value < current.value

            if comp:            
                current, best = self.shift(current, best)
                current = best
            else: break

    def size(self): return self.root.hl + self.root.hr + 1 - self.deleted


def runningMedian(a):
    medians = []
    len_a = len(a)  

    if len_a > 0: medians.append(a[0])
    if len_a > 1: medians.append((a[0] + a[1]) / 2)
    if len_a > 2:
        m = medians[1]            
        if a[0] < a[1]: h_max, h_min = Heap(a[0], '>'), Heap(a[1], '<')
        else: h_max, h_min = Heap(a[1], '>'), Heap(a[0], '<')

        for i, item in enumerate(a[2:]):
            if item < m: h_max.add(item)
            else: h_min.add(item)

            h_min_size, h_max_size = h_min.size(), h_max.size()                     
            if abs(h_min_size - h_max_size) > 1:
                if h_min_size > h_max_size:
                    val = h_min.root.value
                    h_max.add(val)
                    h_min.root.value = 1e10
                    h_min.fit_root()
                else:
                    val = h_max.root.value
                    h_min.add(val)
                    h_max.root.value = 1e-10
                    h_max.fit_root()
            
            print(h_max.root.value, h_min.root.value)
            
            h_min_size, h_max_size = h_min.size(), h_max.size()                     
            if i%2 == 0:
                if h_min_size > h_max_size: medians.append(h_min.root.value)
                else: medians.append(h_max.root.value)
            else: medians.append((h_max.root.value + h_min.root.value)/2)                
    return medians


a = [12, 4, 5, 3, 8, 7]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

medians = runningMedian(a)
print(medians)

#t = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
#print(t)
