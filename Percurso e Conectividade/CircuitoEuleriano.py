def caminhoEuleriano(grafo):
    num_vetices = len(grafo)
    total = 0
    i = 0
    while ((total <= 2) and (i < num_vetices)):
        grafo_vertice = sum(grafo[i])
        #grau ímpar
        if grafo_vertice % 2 != 0:
            total += 1
        i = i + 1
    if (total > 2) | (total == 1):
        print(False)
    else:
        print(True)

grafo = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0]]
caminhoEuleriano(grafo)