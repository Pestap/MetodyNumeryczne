from Functions import matrixMultiplication, forwardSubstitution, backwardSubstitution
import time

def LUDecomposition(matrix):
    U = []
    L = []
    P = []
    for i in range(len(matrix)):
        U.append([0]*len(matrix[0]))
        L.append([0]*len(matrix[0]))
        P.append([0]*len(matrix[0]))

    #inicjalizacja macierzy L
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i == j:
                L[i][j] = 1
                P[i][j] = 1

    #kopiujmey macierz matrix do U

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            U[i][j] = matrix[i][j]

    for i in range(len(matrix) - 1):
        #pivoting
        #find pivot

        pivot_index = 0
        max_value = U[0][i]

        for idx in range(i, len(U)):
            if abs(U[idx][i]) > abs(max_value):
                pivot_index = idx
                max_value = abs(U[idx][i])



        #interchange rows

        U[i][i:len(matrix)], U[pivot_index][i:len(matrix)] = U[pivot_index][i:len(matrix)], U[i][i:len(matrix)]

        L[i][:i], L[pivot_index][:i] = L[pivot_index][:i], L[i][:i]

        P[i], P[pivot_index] = P[pivot_index], P[i]


        #Standard LU
        for j in range(i+1, len(matrix)):
            L[j][i] = U[j][i]/U[i][i]
            for k in range(i, len(matrix)):
                U[j][k] = U[j][k] - L[j][i]*U[i][k]


    return L, U, P

def LU(matrix, vector):

    start = time.time()
    L, U, P = LUDecomposition(matrix)

    vector = matrixMultiplication(P, vector)
    y = forwardSubstitution(L, vector)
    x = backwardSubstitution(U, y)

    stop = time.time()
    return x, stop-start
