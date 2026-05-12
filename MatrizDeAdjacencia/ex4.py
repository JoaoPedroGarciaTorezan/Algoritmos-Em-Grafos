def insereAresta(matriz, vi, vj):
    matriz[vi][vj] = matriz[vi][vj] + 1
    matriz[vj][vi] = matriz[vj][vi] + 1 
    return matriz

