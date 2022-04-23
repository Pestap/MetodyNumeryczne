
def LUDecomposition(matrix):
    U = []
    Li = []
    for i in range(len(matrix)):
        U.append([0]*len(matrix[0]))
        Li.append([0]*len(matrix[0]))

    for i in range(len(Li)):
        for j in range(len(Li[0])):
            if i == j:
                Li[i][j] = 1



    for i in range(len(matrix) -1):
        pass