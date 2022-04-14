import Functions



if __name__ == '__main__':
    matrix = Functions.generateBandMatrix(10, -1, -1, 27)
    vectorB = Functions.generateBVector()

    L, U, D = Functions.getLUD(matrix)


    Functions.printMatrix(vectorB)
    Functions.printMatrix(D)
    D_1 = Functions.inverseDiagonalMatrix(D)
    Functions.printMatrix(D_1)
    Functions.printMatrix(U)
    Functions.printMatrix(L)

    R = Functions.matrixAddition(U, L)


