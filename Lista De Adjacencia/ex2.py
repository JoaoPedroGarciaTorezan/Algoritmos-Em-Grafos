def tipoGrafoLista(listaAdj):
    dirigido = False
    arestas = []
    for i in listaAdj:
        for j in listaAdj[i]:
            if i not in listaAdj.get(j, []):
                dirigido = True

    if dirigido == False:
        for i in listaAdj:
            if i in listaAdj[i]:
                return 30
            for j in listaAdj[i]:
                if list(listaAdj[i]).count(j) > 1:
                    return 20
        return 0
    else:
        for i in listaAdj:
            if i in listaAdj[i]:
                return 31
            for j in listaAdj[i]:
                if list(listaAdj[i]).count(j) > 1:
                    return 21
        return 1
    
        


lista = {0: [], 1: [0, 0, 2], 2: [3], 3: [1]}
res = tipoGrafoLista(lista)
print(res)