import Functions
from Jacobi import jacobi


if __name__ == '__main__':
    N = 931
    matrix = Functions.generateBandMatrix(10, -1, -1, N)
    vectorB = Functions.generateBVector(N)

    L, U, D = Functions.getLUD(matrix)

    D_1 = Functions.inverseDiagonalMatrix(D)

    jacobiResult, jacobiIterations = jacobi(matrix, vectorB, 10 ** (-6))


    Functions.printMatrix(jacobiResult)
    print("Liczba iteracji: " + str(jacobiIterations))
