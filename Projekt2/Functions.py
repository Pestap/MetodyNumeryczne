import math

def generateMatrixExA():
    # dla numeru indeksu: 184531
    N = 27
    a1 = 10
    a2 = -1
    a3 = -1
    matrix = []
    for i in range(N):
        row = [0] * N
        for j in range(27):
            if i == j:
                row[j] = a1
            elif i == j - 1 or i == j + 1:
                row[j] = a2
            elif i == j - 2 or i == j + 2:
                row[j] = a3
            else:
                row[j] = 0
        matrix.append(row)

    return matrix

def generateVectorBexA():
    N = 27
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
            if i == j:
                row[j] = matrix[i][j]
                break #interesuje nas tylko przekatna
        D.append(row)

    #macierz L
    for i in range(rows):
        row = [0]*cols
        for j in range(cols):
            if j < i:
                row[j] = matrix[i][j]
        L.append(row)

    #macierz U
    for i in range(rows):
        row = [0]*cols
        for j in range(cols):
            if j > i:
                row[j] = matrix[i][j]
        U.append(row)

    return L, U, D


def sumMatrices(A, B):
    if not (len(A) == len(B) and len(A[0]) == len(B[0])):
        raise Exception("Błędne rozmiary macierzy prz dodawaniu")

    result = []

    for i in range(len(A)):
        row = [0]* len(A)
        for j in range(len(A[0])):
            row[j] = A[i][j] + B[i][j]
        result.append(row)

    return result


def multiplyMatrices(A,B):
    #sprawdzam rozmiar macierzy
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if not(colsA == rowsB):
        raise Exception("Błędny rozmiar macierzy - mnożenie")

    #TODO: faktycznie mnożenie macierzy
#TODO: i tak


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