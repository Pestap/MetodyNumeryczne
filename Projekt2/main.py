import Functions
from Jacobi import jacobi
from GaussSeidel import gaussSeidel


if __name__ == '__main__':
    N = 131
    matrix = Functions.generateBandMatrix(10, -1, -1, N)
    vectorB = Functions.generateBVector(N)


    jacobiResult, jacobiIterations = jacobi(matrix, vectorB, 10 ** (-6))

    Functions.printMatrix(jacobiResult)
    print("Liczba iteracji: " + str(jacobiIterations))

    gaussSeidelResult, gaussSeidelIterations, time = gaussSeidel(matrix, vectorB, 10**(-6))

    Functions.printMatrix(gaussSeidelResult)
    print("Liczba iteracji: " + str(gaussSeidelIterations))
    print("TIME: " + str(time))

    print("Porównanie wyników:")
    for i in range(len(jacobiResult)):
        print(str(jacobiResult[i]) + " --- " + str(gaussSeidelResult[i]))

