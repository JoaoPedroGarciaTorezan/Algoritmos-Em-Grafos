def DFS(Grafo, v):
    listaVisitado = []
    
    def recursao(v):
        listaVisitado.append(v)
        
        for adj in Grafo[v]:
            if adj not in listaVisitado:
                recursao(adj)
        
    recursao(v)                                                                                                                                                                                                                                         
    print(listaVisitado)


grafo = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}
DFS(grafo, 0)
