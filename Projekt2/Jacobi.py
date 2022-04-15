from datetime import time

import Functions
from Functions import \
    matrixMultiplication, \
    matrixAddition, \
    matrixSubtraction, \
    inverseDiagonalMatrix, \
    getLUD, \
    scalarMatrixMultiplication, \
    calculateResiduumNorm



def jacobi(matrix,vector, epsilon):

    L, U, D = getLUD(matrix)

    D = scalarMatrixMultiplication(D, -1)
    D_1 = inverseDiagonalMatrix(D)

    L_plus_U = matrixAddition(L,U)
    D_1_b = matrixMultiplication(D_1, vector)
    DLU = matrixMultiplication(D_1, L_plus_U) # bardzo kosztowne ale tylko raz

    #inicjalne przybliżenie rozwiązania
    xk = []
    for i in range(len(matrix)):
        xk.append([1])

    while calculateResiduumNorm(matrix, xk, vector) > epsilon:
        xk = matrixAddition(matrixMultiplication(DLU, xk), D_1_b)





    Functions.printMatrix(xk)


    #TODO: metoda jacobiego