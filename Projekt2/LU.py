import Functions
import Jacobi
from Functions import matrixMultiplication, forwardSubstitution, backwardSubstitution
import time

def LUDecomposition(matrix):
    U = []
    L = []
    for i in range(len(matrix)):
        U.append([0]*len(matrix[0]))
        L.append([0]*len(matrix[0]))

    #inicjalizacja macierzy L
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i == j:
                L[i][j] = 1

    #kopiujmey macierz matrix do U

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            U[i][j] = matrix[i][j]

    for i in range(len(matrix) - 1):
        #tworzymy macierz pomocniczą Li
        Li = []
        for j in range(len(matrix)):
            row = []
            for k in range(len(matrix[0])):
                if j == k:
                    row.append(1)
                else:
                    row.append(0)
            Li.append(row)

        #for j in range(i+1, len(matrix)):
        #    Li[j][i] = matrix[j][i] / matrix[i][i]
        # zoptymalizowane dla naszego konkretnego przypadku
        # zabezpieczenie przed wyjściem poza tablice
        lastRow = i+3
        if lastRow > len(matrix):
            lastRow = len(matrix)
        for j in range(i+1, lastRow):
            Li[j][i] = (U[j][i] / U[i][i]) * (-1)
            L[j][i] = (-1)*Li[j][i]

        U = matrixMultiplication(Li, U)

    return L, U

def LU(matrix, vector):

    start = time.time()
    L, U = LUDecomposition(matrix)

    y = forwardSubstitution(L, vector)
    x = backwardSubstitution(U, y)

    stop = time.time()
    return x, stop-start
