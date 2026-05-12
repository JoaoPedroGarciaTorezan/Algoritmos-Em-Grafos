import numpy as np

def warshall(matriz):
    num_vertices = len(matriz)
    R = np.array(matriz)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if R[i][j] == 1 or (R[i][k] == 1 and R[k][j] == 1):
                    R[i][j] = 1
                else:
                    R[i][j] = R[i][j]
    print(R)


matriz = [[1, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
warshall(matriz)
