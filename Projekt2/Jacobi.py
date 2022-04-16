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

    invD = inverseDiagonalMatrix(D)

    LU = matrixAddition(L,U)
    invDb = matrixMultiplication(invD, vector)
    #DLU = matrixMultiplication(D_1, L_plus_U) # bardzo kosztowne ale tylko raz

    DLU = scalarMatrixMultiplication(LU, invD[0][0])
    # D_1 możemy przedstwaić jako macierz jednostkową pomnożoną przez skalar

    DLU = scalarMatrixMultiplication(DLU, -1) # mnożymy razy -1


    #początkowe przybliżenie rozwiązania
    xk = []
    for i in range(len(matrix)):
        xk.append([1])

    while calculateResiduumNorm(matrix, xk, vector) > epsilon:
        first = matrixMultiplication(DLU, xk)
        xk = matrixAddition(first, invDb)





    Functions.printMatrix(xk)


    #TODO: metoda jacobiego