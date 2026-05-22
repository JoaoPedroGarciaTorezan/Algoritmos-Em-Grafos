def prim(grafo):
    v = 0
    E_min = 0x3F3F3F3F3F
    S = [v]
    V = list(range(len(grafo)))
    N = list(range(len(grafo)))
    N.remove(v)
    T = []
    custo_total = 0
    while len(T) < len(V)-1:
        for i in S:
            for j in N:
                if grafo[i][j] != 0 and grafo[i][j] < E_min:
                    E_min = grafo[i][j]
                    w = i
                    u = j
        S.append(u)
        N.remove(u)
        T.append((w, u))
        E_min = 0x3F3F3F3F3F
    for i in T:
        custo_total += grafo[i[0]][i[1]]
    print(T, custo_total)

   
grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]]
prim(grafo)