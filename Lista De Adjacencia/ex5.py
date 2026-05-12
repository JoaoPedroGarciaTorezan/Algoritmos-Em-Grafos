def insereVerticeLista(listaAdj):
    vert = list(listaAdj.keys())
    listaAdj[vert[-1] + 1] = []
    print(listaAdj)




grafo = {0: [1, 1, 2, 2, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 1, 2], 4: [2]}
insereVerticeLista(grafo)

