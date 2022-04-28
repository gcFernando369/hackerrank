import string


def stringCompression(s: str) -> str:
  len_s = len(s)
  current = s[0]
  count = 0
  comp = []

  for i in range(len_s):
    if s[i] == current: count += 1
    else:
      comp.append(f'{count}{current}')
      count = 1
      current = s[i]
  comp.append(f'{count}{current}')
  comp = ''.join(comp)
  if len(comp) < len_s: return comp
  return s

print(stringCompression('aabcccccaaa'))
print(stringCompression('aaabbccaadd'))