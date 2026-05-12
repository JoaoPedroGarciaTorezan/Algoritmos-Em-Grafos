def insereArestaLista(listaAdj, vi, vj):
    pos = 0
    dirigido = False
    for i in listaAdj:
        for j in listaAdj[i]:
            if i not in listaAdj.get(j, []):
                dirigido = True

    for i in listaAdj[vj]:
        if vi > i:
            pos += 1
        else:
            break
    
    if dirigido == False:
        listaAdj[vi].append(vj)
        listaAdj[vj].insert(pos, vi)
    else: 
        listaAdj[vi].append(vj)
    print(listaAdj)



grafo = {0: [], 1: [0, 2], 2: [3], 3: [1]}
insereArestaLista(grafo, 0, 3)