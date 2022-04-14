import Functions



if __name__ == '__main__':
    matrix = Functions.generateMatrixExA()
    vectorB = Functions.generateVectorBexA()

    L, U, D = Functions.getLUD(matrix)


    Functions.printMatrix(vectorB)
    Functions.printMatrix(D)
    D_1 = Functions.inverseDiagonalMatrix(D)
    Functions.printMatrix(D_1)
    Functions.printMatrix(U)
    Functions.printMatrix(L)

    R = Functions.sumMatrices(U, L)


