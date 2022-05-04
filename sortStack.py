from cv2 import sort


def pop(stack):
  if len(stack) == 0: return None
  else: return stack.pop()

def push(stack, val):
  stack.append(val)

def bubleSort(stack, temp):
  temp = []
  b0 = None
  b1 = None
  while True:
    if b0 is None: b0 = pop(stack)
    if b1 is None: b1 = pop(stack)
    if b0 == b1 and b1 is None: break    
    if b0 is not None and b1 is None:      
      push(temp, b0)
      b0 = None
    elif b0 is None and b1 is not None:
      push(temp, b1)
      b1 = None
    elif b0 >= b1:
      push(temp, b0)
      b0 = None
    else:
      push(temp, b1)
      b1 = None
  return stack, temp
    

def sortStack(stack):
    temp = []
    stack, temp = bubleSort(stack, temp)    
    is_valid = True
    curr = None
    while True:
      val = pop(temp)
      if val is None: break
      if curr is not None and curr >= val:        
        is_valid = False
      curr = val
      push(stack, val)
    if is_valid:
      while True:
        val = pop(stack)
        if val is None: break
        push(temp, val)
      return temp
    return sortStack(stack)

stack = [3, 7, 1, 5, 0, 6, 9, 8, 2]
print(stack)
print(sortStack(stack))





