from Functions import \
    matrixMultiplication, \
    matrixAddition, \
    inverseDiagonalMatrix, \
    getLUD, \
    scalarMatrixMultiplication, \
    calculateResiduumNorm

from Jacobi import jacobi

def gaussSeidel(matrix, vector, epsilon):
    L,U,D = getLUD(matrix)
    DL = matrixAddition(D, L)

    # początkowe przybliżenie rozwiązania
    xk = []

    for i in range(len(matrix)):
        xk.append([1])

    iterations = 0  # liczba iteracji


    while calculateResiduumNorm(matrix, xk, vector) > epsilon:
        #TODO: zamiast jacobi'ego podstawianie w przód/tył
        second = jacobi(DL, vector, epsilon)[0]
        UR = matrixMultiplication(U, xk)
        first = scalarMatrixMultiplication(jacobi(DL,UR, epsilon)[0], -1)
        iterations += 1
        xk = matrixAddition(first, second)


    return xk, iterations

