import Functions
from Jacobi import jacobi


if __name__ == '__main__':
    N = 131
    matrix = Functions.generateBandMatrix(10, -1, -1, N)
    vectorB = Functions.generateBVector(N)

    L, U, D = Functions.getLUD(matrix)

    D_1 = Functions.inverseDiagonalMatrix(D)

    jacobi(matrix, vectorB, 10 ** (-6))

