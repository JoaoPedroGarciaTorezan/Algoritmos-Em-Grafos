def calcDensidade(grafo):
    dirigido = False
    aresta = 0
    vert = len(grafo)
    for i in range(len(grafo)):    
        for j in range(len(grafo[i])):
            if grafo[i][j] != grafo[j][i]:
                dirigido = True
            aresta += grafo[i][j]

    if dirigido:
        dens = aresta / (vert * (vert-1))
    else:
        dens = (2 * aresta) / (vert * (vert-1))
    return dens

grafo = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
print("{:.3f}".format(calcDensidade(grafo)))