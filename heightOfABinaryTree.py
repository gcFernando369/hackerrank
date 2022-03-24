def height(root):    
    level = 0
    
    current = root
    current.level = 0
    
    childs = []
    while True:
        next_level = current.level + 1
        if current.left is not None:
            current.left.level = next_level
            childs.append(current.left)
        if current.right is not None:
            current.right.level = next_level
            childs.append(current.right)
        if len(childs) > 0:
            current = childs.pop()
            if current.level > level: level = current.level
        else: break
    
    return level