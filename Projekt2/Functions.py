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
    vector = [0]*N
    for i in range(N):
        vector[i] = math.sin(i*(f+1))
    return vector


def printMatrix(matrix):
    rows = len(matrix)
    for i in range(rows):
        for j in matrix[i]:
            print(j, end=" ")
        print()

def printVector(vector):
    for i in vector:
        print(i, end=" ")
    print()