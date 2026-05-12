def tipoGrafo(grafo):
    dirigido = False
    for i in range(len(grafo)):    
        for j in range(len(grafo[i])):
            if grafo[i][j] != grafo[j][i]:
                dirigido = True

    if dirigido == True:
        for i in range(len(grafo)):
            if grafo[i][i] == 1:
                return 31
            for j in range(len(grafo[i])):
                if grafo[i][j] > 1:
                    return 21
        return 1
    else:
        for i in range(len(grafo)):
            if grafo[i][i] == 1:
                return 30
            for j in range(len(grafo[i])):
                if grafo[i][j] > 1:
                    return 20
        return 0

    
grafo = [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
print(tipoGrafo(grafo))