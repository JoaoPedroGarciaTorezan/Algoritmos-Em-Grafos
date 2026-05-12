def criaDicionario(matriz):
    dic_L = dict()
    for i in range(len(matriz)):
        dic_L[i] = []
        for j in range(len(matriz)):
            if matriz[i][j] != 0:
                dic_L[i].append(j)
                if matriz[i][j] > 1:
                    for k in range(1,matriz[i][j]):
                        dic_L[i].append(j)   


    return dic_L    

matriz = [[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]]
md = criaDicionario(matriz)
print(md)