def kruskal(grafo):
    Pesos = []
    V = list(range(len(grafo)))
    H = []
    T = []
    custo_total = 0
    for i in range(len(grafo)):
        for j in range(i, len(grafo)):
            if grafo[i][j] != 0:
                Pesos.append((grafo[i][j], i, j))


    Pesos.sort()
    for i in Pesos:
        H.append((i[1], i[2]))

    # Função para verificar se dois vértices estão conectados
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

grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
kruskal(grafo)