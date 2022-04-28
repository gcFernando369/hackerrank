from copy import copy
import pprint

def rotateMatrix(matrix: list) -> list:  
  N = len(matrix)
  last_col = N - 1
  new_matrix = [[0 for _ in range(N)] for _ in range(N)]

  for i, row in enumerate(matrix):    
    col = last_col - i
    for j in range(N):
      new_matrix[j][col] = row[j]
  return new_matrix

pp = pprint.PrettyPrinter(indent = 4)
pp.pprint(rotateMatrix([[1,2],[3,4]]))
pp.pprint(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))