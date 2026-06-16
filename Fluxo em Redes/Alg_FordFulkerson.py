def fordFulkerson(G, s, t):
    fluxoMax = 0
    Gr = G
    
    # Algoritmo de busca usado
    def BFS(Gr, s, t):
        visitados = []
        #Guardar de onde cada nó vem
        pai = []
        for i in range(len(Gr)):
            visitados.append(False)
            pai.append(-1)
        
        Q = [] 
        Q.append(s)
        visitados[s] = True
        caminho = []
        while len(Q) !=  0:
            v = Q.pop(0)
            for adj, val in enumerate(Gr[v]):
                if visitados[adj] == False and val > 0:
                    Q.append(adj)
                    visitados[adj] = True
                    pai[adj] = v
                    if adj == t:
                        fim = t
                        while pai[fim] != -1:
                            caminho.append((pai[fim], fim))
                            fim = pai[fim]
                        caminho.reverse()
                        return caminho
        # Não achou mais camihos até o terminal        
        return None
    
    p = BFS(Gr, s ,t)
    # Equanto houver caminho disponivel
    while p != None:
        cr = Gr[p[0][0]][p[0][1]]
        for (v, u) in p:
            cr = min(cr, Gr[v][u])
        for (v,u) in p:
            Gr[v][u] -= cr
            Gr[u][v] += cr
        fluxoMax += cr
        p = BFS(Gr, s ,t)

    print(fluxoMax)

grafo = [[0, 5, 0, 4, 0, 0], [ 0, 0, 6, 0, 0, 0], [0, 0, 0, 0, 8, 5], [0, 3, 0, 0, 1, 0], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0]]
fordFulkerson(grafo, 0, 5)
        
    