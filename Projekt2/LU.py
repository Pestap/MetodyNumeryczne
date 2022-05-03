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
        for j in range(i+1, len(matrix)):
            L[j][i] = U[j][i]/U[i][i]
            for k in range(i, len(matrix)):
                U[j][k] = U[j][k] - L[j][i]*U[i][k]


    return L, U

def LU(matrix, vector):

    start = time.time()
    L, U = LUDecomposition(matrix)

    y = forwardSubstitution(L, vector)
    x = backwardSubstitution(U, y)

    stop = time.time()
    return x, stop-start
