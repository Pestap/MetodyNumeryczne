import math

def generateBandMatrix(a1, a2, a3, N):
    # dla numeru indeksu: 184531
    matrix = []
    for i in range(N):
        row = [0] * N
        for j in range(N):
            # główna przekątna
            if i == j:
                row[j] = a1
            # drugie przekątne
            elif i == j - 1 or i == j + 1:
                row[j] = a2
            # trzecie przekątnę
            elif i == j - 2 or i == j + 2:
                row[j] = a3
            # cała reszta
            else:
                row[j] = 0
        matrix.append(row)

    return matrix

def generateBVector(N):
    f = 4
    vector = []
    for i in range(N):
        vector.append([math.sin(i*(f+1))])
    return vector


def getLUD(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    L = []
    U = []
    D = []

    #macierz D
    for i in range(rows):
        row = [0]*cols
        for j in range(cols):
            # interesuje nas tylko przekatna
            if i == j:
                row[j] = matrix[i][j]
                break
        D.append(row)

    #macierz L
    for i in range(rows):
        row = [0]*cols
        for j in range(cols):
            # macierz górna trójkątna
            if j < i:
                row[j] = matrix[i][j]
        L.append(row)

    #macierz U
    for i in range(rows):
        row = [0]*cols
        # macierz dolna trójkątna
        for j in range(cols):
            if j > i:
                row[j] = matrix[i][j]
        U.append(row)

    return L, U, D


def matrixAddition(A, B):
    if not (len(A) == len(B) and len(A[0]) == len(B[0])):
        raise Exception("Error: matrix sizes do not match: A(" +
                        str(len(A)) + " x " + str(len(A[0])) + ")" +
                        ", B(" + str(len(B)) + " x " + str(len(B[0])) + ")")

    result = []
    for i in range(len(A)):
        row = [0]*len(A[0])
        for j in range(len(A[0])):
            row[j] = A[i][j] + B[i][j]
        result.append(row)

    return result

def matrixSubtraction(A, B):
    if not (len(A) == len(B) and len(A[0]) == len(B[0])):
        raise Exception("Error: matrix sizes do not match: A(" +
                        str(len(A)) + " x " + str(len(A[0])) + ")" +
                        ", B(" + str(len(B)) + " x " + str(len(B[0])) + ")")

    result = []
    for i in range(len(A)):
        row = [0]*len(A[0])
        for j in range(len(A[0])):
            row[j] = A[i][j] - B[i][j]
        result.append(row)

    return result


def matrixMultiplication(A, B):
    # sprawdzam rozmiar macierzy
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    result = []

    if not(colsA == rowsB):
        raise Exception("Error: matrix sizes do not match: A(" +
                        str(len(A)) + " x " + str(len(A[0])) + ")" +
                        ", B(" + str(len(B)) + " x " + str(len(B[0])) + ")")

    for i in range(rowsA):
        row = [0]*colsB
        for j in range(colsB):
            sum = 0
            for k in range(colsA):
                sum += A[i][k]*B[k][j]
            row[j] = sum
        result.append(row)

    return result

def scalarMatrixMultiplication(matrix, scalar):
    result = []
    for i in range(len(matrix)):
        row = [0]*len(matrix[0])
        for j in range(len(matrix[0])):
            row[j] = matrix[i][j] * scalar
        result.append(row)

    return result


def inverseDiagonalMatrix(matrix):
    result = []
    for i in range(len(matrix)):
        row = [0] * len(matrix[0])
        for j in range(len(matrix[0])):
            if i == j:
                row[j] = 1 / matrix[i][j]
                break # intersuje nas tylko przekątna
        result.append(row)

    return result


def calculateResiduumNorm(matrix, aprox, b):
    bApprox = matrixMultiplication(matrix, aprox)
    residuum = matrixSubtraction(bApprox, b)

    norm = 0
    for i in range(len(residuum)):
        for j in range(len(residuum[0])):
            norm += residuum[i][j]**2

    return math.sqrt(norm)


def printMatrix(matrix):
    rows = len(matrix)
    print()
    for i in range(rows):
        for j in matrix[i]:
            print(j, end=" ")
        print()
    print()


def printVector(vector):
    print()
    for i in vector:
        print(i)
    print()