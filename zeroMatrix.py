def zeroMatrix(mat: list) -> list:
  M, N = len(mat), len(mat[0])
  rows, cols = {}, {}

  for m in range(M):
    for n in range(N):
      if mat[m][n] == 0:
        rows[m] = True
        cols[n] = True
  
  for m in rows.keys():
    for n in range(N): mat[m][n] = 0

  for n in cols.keys():
    for m in range(M): mat[m][n] = 0

  return mat

print(zeroMatrix([[1,2,3],[4,0,6],[7,8,9]]))