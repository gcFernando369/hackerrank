def urlify(s: str) -> str:
  len_s = len(s)
  start, end = 0, len_s

  for start in range(len_s):
    if s[start] != ' ': break
  
  for end in range(len_s - 1, -1, -1):
    if s[end] != ' ': break

  new_string = []
  isSpace = False
  
  for i in range(start, end+1, 1):
    if s[i] != ' ':
      new_string.append(s[i])
      isSpace = False
    else:
      if isSpace: pass
      else:
        isSpace = True
        new_string.append('%20')

  new_string = ''.join(new_string)
  return new_string

print('|'+urlify("Mr John  Smith    ")+'|')