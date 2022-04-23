from Functions import \
    matrixMultiplication, \
    matrixAddition, \
    forwardSubstitution, \
    getLUD, \
    scalarMatrixMultiplication, \
    calculateResiduumNorm

import time
def gaussSeidel(matrix, vector, epsilon):
    L,U,D = getLUD(matrix)

    # początkowe przybliżenie rozwiązania
    xk = []
    for i in range(len(matrix)):
        xk.append([1])

    iterations = 0  # liczba iteracji

    start = time.time()

    DL = matrixAddition(D, L)

    while calculateResiduumNorm(matrix, xk, vector) > epsilon:
        # Jako, że macierz DL jest macierzą dolną trójkątną, to do rozwiązania układów równań możemy skorzystać
        # z metody podstawiania w przód, co daje dużo lepsze wyniki niż użycie do tego celu metody Jacobiego
        second = forwardSubstitution(DL, vector)
        UR = matrixMultiplication(U, xk)
        first = scalarMatrixMultiplication(forwardSubstitution(DL, UR), -1)
        iterations += 1
        xk = matrixAddition(first, second)
    stop = time.time()


    return xk, iterations, stop - start

