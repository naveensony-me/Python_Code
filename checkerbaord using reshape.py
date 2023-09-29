import numpy as np

matrix = np.arange(64).reshape(8, 8)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i % 2 != 0:
            matrix[i][j] %= 2
        else:
            if matrix[i][j] %2 == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
            
print(matrix)
