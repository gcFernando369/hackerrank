import string


def stringRotation(s1: str, s2: str) -> str:
  n = len(s1)
  if len(s2) != n: return False

  start = 0
  while start < n:
    valid = False
    for i in range(n - start):
      if s1[i] == s2[start + i]: valid = True
      else:
        start += 1
        break
    if valid: break

  if start == n: return False
  return s2[:start] in s1

print(stringRotation('waterbottle', 'erbottlewat'))
print(stringRotation('abbaabbaa', 'bbaabbaaa'))
print(stringRotation('waterbottle', 'erbottelwat'))