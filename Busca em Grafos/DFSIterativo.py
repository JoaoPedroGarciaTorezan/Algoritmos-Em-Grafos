
def DFS_iterativo(grafo, v):
    naoVisitados = grafo.keys()
    visitados = []
    pilha = [v]
    while naoVisitados:
        while pilha:
            t = pilha[-1]
            if t not in visitados:
                visitados.append(t)
            adjViaveis = [u for u in grafo[t] if u not in visitados]
            if adjViaveis:
                pilha.append(adjViaveis[0])
            else:
                pilha.pop()
        naoVisitados = [u for u in naoVisitados if u not in visitados]
        if naoVisitados:
            pilha.append(naoVisitados[0])
    print(visitados)



grafo = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}
DFS_iterativo(grafo, 0)