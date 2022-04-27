def palindromePermutation(s: str) -> bool:
  items = {}
  s = s.lower()
  for item in s:
    if item == ' ': continue
    if item in items: items[item] += 1
    else: items[item] = 1
  
  uneven_count = 0
  for count in items.values():
    uneven_count += (count % 2)
  can_be_palindrome = uneven_count < 2
  return can_be_palindrome

print(palindromePermutation('Tact Coa'))
print(palindromePermutation('Aniinata la laav t'))
print(palindromePermutation('This is not a palindrome'))