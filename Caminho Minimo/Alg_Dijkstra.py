import numpy as np

def dijkstra(grafo, inicio, fim):
    INF = 0x3F3F3F3F3F

    custo = []
    rota = []
    list_A = []
    list_F = []
    list_N = []

    #Inicialização
    for i in range(len(grafo)):
        if grafo[inicio][i] != 0:
            custo.append(grafo[inicio][i])
        else: custo.append(INF)
        rota.append(inicio)
        list_A.append(i)

    custo[inicio] = 0
    while list_A:
        #Vertice com menor custo
        min_custo = INF
        v = 0
        for i in list_A:
            if custo[i] < min_custo and i in list_A:
                min_custo = custo[i]
                v = i
        list_F.append(v)
        list_A.remove(v)
        #adjacentes de v
        for i in list_A:
            if grafo[v][i] != 0 and custo[i] > custo[v] + grafo[v][i]:
                custo[i] = custo[v] + grafo[v][i]
                rota[i] = v
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

grafo = [[0, 3, 8, 4, 0, 10], [ 3, 0, 0, 6, 0, 0], [ 8, 0, 0, 0, 7, 0], [ 4,  6, 0, 0,  1,  3], [0, 0,  7,  1, 0, 1], [10, 0, 0,  3,  1, 0]]
dijkstra(np.array(grafo), 0, 5)