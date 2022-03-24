def isBalanced(s):
    balanced = 'YES'
    bs = {
        '(':')',
        '[':']',
        '{':'}',
    }
    open_b = '([{'
    stack = []
    for item in s:
        if item in open_b:
            stack.append(item)
        else:
            if len(stack) > 0:
                expected = bs[stack.pop()]
                if expected != item: return 'NO'
            else: return 'NO'
    if len(stack) > 0: return 'NO'
    return balanced