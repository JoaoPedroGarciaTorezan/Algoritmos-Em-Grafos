
def  temposVertices(listaAdj, v):
    cor = []
    tempoD = []
    tempoT = []
    dic = dict()
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

    if cor[v] == 'branco':
            recursao(v)

    for ver in listaAdj:
        if cor[ver] == 'branco':
            recursao(ver)
    
    for vert in listaAdj:
        dic[vert] = '{}/{}'.format(tempoD[vert],tempoT[vert])
    
    print(dic)

grafo = {0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}
temposVertices(grafo, 3)