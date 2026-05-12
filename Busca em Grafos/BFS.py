def BFS(grafo, v):
    Q = [] 
    Q.append(v)
    sequencia = []
    while len(Q) !=  0:
        v = Q.pop(0)
        for adj in grafo[v]:
            if adj not in Q and adj not in sequencia:
                Q.append(adj)
        sequencia.append(v)
        
    #Grafo desconexo
    for vert in grafo:
        if vert not in sequencia:
            sequencia.append(vert)
    print(sequencia)

grafo = {0: [2], 1: [0, 4], 2:[1, 4], 3: [2], 4: [1, 3]}
BFS(grafo, 4)