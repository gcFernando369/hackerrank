from operator import le
from turtle import left


class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def list2tree(nums: list) -> Node:
  n = len(nums)
  if n == 0: return None
  if n == 1: return Node(nums[0])
  if n == 2: return Node(nums[1], left = Node(nums[0]))
  mid = n // 2
  return Node( nums[mid],
               left = list2tree(nums[:mid]),
               right = list2tree(nums[mid+1:]))

nums = [0, 1, 2, 3, 5, 7, 8, 9]
root = list2tree(nums)

queue = [root]
while len(queue) > 0:
  next = queue.pop(0)
  print(next.val)
  if next.left is not None: queue.append(next.left)
  if next.right is not None: queue.append(next.right)


    