def kruskal(grafo):
    Pesos = []
    H = []
    T = []
    custo_total = 0
    for i in range(len(grafo)):
        for j in range(i, len(grafo)):
            if grafo[i][j] != 0:
                Pesos.append((grafo[i][j], i, j))


    Pesos.sort()
    for (p,u,v) in Pesos:
        H.append((u, v))

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

    # Kruskal: adiciona arestas se não formarem ciclo
    while len(T) < len(grafo) - 1:
        for i in H:
            if len(T) == 0:
                T.append(i)
            elif not estao_conectados(T, i[0], i[1]):
                T.append(i)
        

    for i in T:
        custo_total += grafo[i[0]][i[1]]

    print(T, custo_total)

grafo = [[0,3,8,4,0,10],[3,0,0,6,0,0],[8,0,0,0,7,0],[4,6,0,0,1,3],[0,0,7,1,0,1],[10,0,0,3,1,0]]
kruskal(grafo)