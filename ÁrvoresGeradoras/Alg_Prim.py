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
        custo_total += E_min
        T.append((w, u))
        E_min = 0x3F3F3F3F3F
    print(T, custo_total)


grafo = [[0,3,8,4,0,10],[3,0,0,6,0,0],[8,0,0,0,7,0],[4,6,0,0,1,3],[0,0,7,1,0,1],[10,0,0,3,1,0]]
prim(grafo)