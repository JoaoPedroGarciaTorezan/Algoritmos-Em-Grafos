import numpy as np

def insereVertice(matriz):
    novo_v = []
    novo_v.append(0)
    for i in range(len(matriz)):
        novo_v.append(0)
        matriz[i].append(0)
    matriz.append(novo_v)

    return matriz

matriz = [[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]]
md = insereVertice(matriz)
print(md)