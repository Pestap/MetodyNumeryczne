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
    #TODO: Lepsze nazwy zmiennych (pamiętaj o minusie),
    # może lepiej zrobićwykładową implementacje ?
    # tam nie ma minusów na końcu

    D_1 = inverseDiagonalMatrix(D)

    L_plus_U = matrixAddition(L,U)
    D_1_b = matrixMultiplication(D_1, vector)
    DLU = matrixMultiplication(D_1, L_plus_U) # bardzo kosztowne ale tylko raz
    DLU = scalarMatrixMultiplication(DLU, -1) # mnożymy razy -1


    #początkowe przybliżenie rozwiązania
    xk = []
    for i in range(len(matrix)):
        xk.append([1])

    while calculateResiduumNorm(matrix, xk, vector) > epsilon:
        first = matrixMultiplication(DLU, xk)
        xk = matrixAddition(first, D_1_b)





    Functions.printMatrix(xk)


    #TODO: metoda jacobiego