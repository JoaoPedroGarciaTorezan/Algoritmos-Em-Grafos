import numpy as np

def valorCelula(matriz, linha, coluna):
    dimensao = np.shape(matriz)
    if linha > dimensao[0] or coluna > dimensao[1]:
        print('Erro')
    else:
        print(f"Celula[{linha}][{coluna}] = ", matriz[linha][coluna])

matriz = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
valorCelula(matriz,2,6)
