def removeVerticeLista(listaAdj, v):
    for chave in listaAdj:
        if v in listaAdj[chave]:    
            while v in listaAdj[chave]:      
                listaAdj[chave].remove(v)

    del listaAdj[v]

    print(listaAdj)




grafo = {0: [1, 1, 2, 2, 3, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 0, 1, 2]}
removeVerticeLista(grafo, 0)