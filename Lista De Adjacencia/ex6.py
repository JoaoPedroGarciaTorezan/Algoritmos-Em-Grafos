def removeArestaLista(listaAdj, vi, vj):
    dirigido = False
    for i in listaAdj:
        for j in listaAdj[i]:
            if i not in listaAdj.get(j, []):
                dirigido = True
    
    if dirigido == True:
        listaAdj[vi].remove(vj)
    else:
        listaAdj[vi].remove(vj)
        listaAdj[vj].remove(vi)
    prin



grafo = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}
removeArestaLista(grafo, 0, 2)