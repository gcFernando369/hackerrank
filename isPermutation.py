import string
from cv2 import sort


def isPermutation(string_a, string_b) -> bool:
  len_a = len(string_a)
  if len(string_b) != len_a:
    return False    
  
  list_a = list(string_a)
  list_b = list(string_b)
  
  list_a.sort()
  list_b.sort()  
  
  for i in range(len_a):
    if list_a[i] != list_b[i]:
      return False
  return True

tests = [
  ["ababab", "baabab", True],
  ["ababab", "bcabab", False],
  ["ababab", "baabababa", False],
  ["qwertyu854vbn", "qwe54rtyu8nvb", True],
]

for i, test in enumerate(tests):
  print(i, isPermutation(test[0], test[1]) == test[-1])