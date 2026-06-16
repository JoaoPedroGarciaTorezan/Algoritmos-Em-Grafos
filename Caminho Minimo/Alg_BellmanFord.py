def bellmanford(grafo, inicio, fim):
    custo = []
    rota = []
    E = []
    for i in range(len(grafo)):
        custo.append(0xFFFFFF)
        rota.append(inicio)

    #Todas as arestas do grafo
    for i in range(len(grafo)):
        for j in range(len(grafo)):
            if grafo[i][j] != 0:
                E.append((i,j))
    
    custo[inicio] = 0
    for i in range(len(grafo)):
        for (v, u) in E:
            if custo[u] > custo[v] + grafo[v][u]:
                custo[u] = custo[v] + grafo[v][u] 
                rota[u] = v

    # Verifica se o grafo forma um ciclo de peso negativo
    for i in E:
        if custo[u] > custo[v] + grafo[v][u]:
            return False
    # Monta o caminho (igual ao Dijkstra)
    caminho = []
    fim2 = fim
    for i in range(len(rota)):
        caminho.append(fim)
        fim = rota[fim]
        if fim == caminho[-1]:
            break
    caminho.reverse()
    cust = custo[fim2]
    print(caminho, cust)    

grafo = [[0, 6, 0, 7, 0], [ 0, 0, 5, 8, -4], [ 0, -2, 0, 0, 0], [ 0, 0, -3, 0, 9], [2, 0, 7, 0, 0]]
bellmanford(grafo, 0, 4)