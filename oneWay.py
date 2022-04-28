def oneWay(s1:str, s2:str) -> bool:
  len_s1, len_s2 = len(s1), len(s2)
  if abs(len_s1 - len_s2) > 1: return False

  if len_s1 >= len_s2: a, b = s1, s2
  else: a, b = s2, s1

  i, j = 0, 0
  diffs = 0
  len_a, len_b = len(a), len(b)

  while i < len_a and j < len_b:    
    if a[i] == b[j]:
      i += 1
      j += 1
    else:
      diffs += 1
      next_i = i + 1
      next_j = j + 1
      if next_i < len_a and a[next_i] == b[j]:
        i = next_i
      elif next_i < len_a and next_j < len_b and a[next_i] == b[next_j]:
        i = next_i
        j = next_j
      else: break
    
  is_valid = diffs < 2
  return is_valid

print(oneWay('pale', 'ple'))
print(oneWay('pales', 'pale'))
print(oneWay('pale', 'bale'))
print(oneWay('pale', 'bake'))
print(oneWay('pale', 'pala'))
