from Functions import \
    matrixMultiplication, \
    matrixAddition, \
    inverseDiagonalMatrix, \
    getLUD, \
    scalarMatrixMultiplication, \
    calculateResiduumNorm
import time


def jacobi(matrix,vector, epsilon):

    L, U, D = getLUD(matrix)

    #początkowe przybliżenie rozwiązania
    xk = []

    for i in range(len(matrix)):
        xk.append([1])

    iterations = 0 # liczba iteracji

    start = time.time()
    invD = inverseDiagonalMatrix(D)

    LU = matrixAddition(L,U)
    invDb = matrixMultiplication(invD, vector)
    DLU = scalarMatrixMultiplication(LU, invD[0][0])
    # D_1 możemy przedstwaić jako macierz jednostkową pomnożoną przez skalar

    DLU = scalarMatrixMultiplication(DLU, -1) # mnożymy razy -1
    initialRes = calculateResiduumNorm(matrix, xk, vector)
    while calculateResiduumNorm(matrix, xk, vector) > epsilon:
        iterations += 1
        first = matrixMultiplication(DLU, xk)
        xk = matrixAddition(first, invDb)
        if iterations == 100 and calculateResiduumNorm(matrix, vector,xk) > initialRes:
            print("Metoda Jacobiego rozbiega się")
            xk = None
            break

    stop = time.time()

    return xk, iterations, stop - start
