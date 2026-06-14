def boruvka(grafo):
    C = []
    for v in range(len(grafo)):
        C.append([v])
    E = []
    T = []

    for i in range(len(grafo)):
        for j in range(len(grafo)):
            if grafo[i][j] != 0:
                E.append((i,j))

     # Função para verificar se dois vértices estão conectados (formam ciclo)
    def estao_conectados(T, u, v):
        adj = {i: [] for i in range(len(grafo))}
        for edge in T:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        queue = [u]
        visited.add(u)
        
        while queue:
            atual = queue.pop(0)
            if atual == v:
                return True
            for vizinho in adj[atual]:
                if vizinho not in visited:
                    visited.add(vizinho)
                    queue.append(vizinho)
        return False

        
    while len(C) > 1:
        for c in C:
            for (v, u) in E:
                if v in c and u not in c:
                    E_min = min(grafo[c[v]][u], grafo[c[v][v]])
                    if (v, u) not in T and not estao_conectados(T,u, v):
                        C = c.append((v, u))
                        T.append((v,u))

        print(T)

grafo = [[0,3,8,4,0,10],[3,0,0,6,0,0],[8,0,0,0,7,0],[4,6,0,0,1,3],[0,0,7,1,0,1],[10,0,0,3,1,0]]
boruvka(grafo)