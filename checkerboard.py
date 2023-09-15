import numpy as np
matrix = np.zeros((8, 8), dtype=int)
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1

print(matrix)
