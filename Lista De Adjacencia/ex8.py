def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vi in listaAdj[vj] and vj in listaAdj[vi]:
        return True
    return False





grafo = {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}
print(verificaAdjacenciaLista(grafo, 0, 3))