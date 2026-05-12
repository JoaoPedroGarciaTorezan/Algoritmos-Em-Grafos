def removeVertice(matriz, v):
    for i in range(len(matriz)):
        matriz[i][v] = -1;
    for j in range(len(matriz)):
        matriz[v][j] = -1;
    print(matriz)

matriz = [[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]]
removeVertice(matriz, 3)