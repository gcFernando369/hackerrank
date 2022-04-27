def oneWay(a:str, b:str) -> bool:
  len_a = len(a)
  len_b = len(b)

  if abs(len_a - len_b) > 1: return False

  if len_a >= len_b:
    s1 = a
    s2 = b
  else:
    s1 = b
    s2 = a

  diffs = 0
  j = 0
  i = 0

  while i < len(s1) and j < len(s2):

    if s1[i] == s2[j]:
      i += 1
      j += 1
    else:
      i += 1
      diffs += 1

    if i+1 < len(s1) and j+1 < len(s2) and s1[i+1] == s2[j+1]:
      i += 1
      j += 1
    
  is_valid = diffs < 2
  return is_valid

print(oneWay('pale', 'ple'))
print(oneWay('pales', 'pale'))
print(oneWay('pale', 'bale'))
print(oneWay('pale', 'bake'))
