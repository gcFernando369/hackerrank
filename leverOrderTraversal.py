def levelOrder(root):
    leafs = [root]
    values = []
    while len(leafs) > 0:
        curr = leafs.pop(0)
        values.append(str(curr.info))
        if curr.left is not None: leafs.append(curr.left)
        if curr.right is not None: leafs.append(curr.right)
    outs = ' '.join(values)
    print(outs)