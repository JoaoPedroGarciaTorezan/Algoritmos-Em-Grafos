import numpy as np

def floydWarshall(W):
    n = len(W)
    dim = (n+1,n,n) #São n+1 matrizes, arrumar isso
    D = np.zeros(dim)
    #Monta a matriz D[0]: valores 0 em W, sem ser diagonais, são infinitos
    for i in range(len(W)):
        for j in range(len(W)):
            if W[i][j] == 0 and i != j:
                W[i][j] = 0xFFFFFFF

    D[0] = W
    for k in range(n+1):
        for v in range(n):
            for u in range(n):
                if k == 0:
                    D[k][v][u] = W[v][u]
                else:
                    D[k][v][u] = min(D[k-1][v][u], D[k-1][v][k-1] + D[k-1][k-1][u])

    print(D[-1])


W = [[0, 3, 8, 0, -4], [ 0, 0, 0, 1, 7], [ 0, 4, 0, 0, 0], [ 2, 0, -5, 0, 0], [0, 0, 0, 6, 0]]
floydWarshall(W)