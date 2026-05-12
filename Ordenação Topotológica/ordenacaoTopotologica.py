def ordenacaoTopologica(listaAdj):
    cor = []
    tempoD = []
    tempoT = []
    ord_top = []
    ord_temp = []
    tempo = 0


    for c in listaAdj:
        cor.append('branco')
        tempoD.append(0)
        tempoT.append(0)

    def recursao (v):
        nonlocal tempo
        cor[v] = 'cinza'
        tempo += 1
        tempoD[v] = tempo 
        for adj in listaAdj[v]:
            if cor[adj] == 'branco':
                recursao(adj)
        cor[v] = 'preto'
        tempo += 1
        tempoT[v] = tempo 

    for ver in listaAdj:
        if cor[ver] == 'branco':
            recursao(ver)

    for vert in listaAdj:
        ord_temp.append(tempoT[vert])
    ord_temp.sort(reverse=True)

    chaves = list(listaAdj.keys())
    for vert in chaves:
        pos = tempoT.index(ord_temp[vert])
        ord_top.append(chaves[pos])

    print(ord_top)

grafo = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
ordenacaoTopologica(grafo)