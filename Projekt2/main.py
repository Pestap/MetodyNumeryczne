import Functions
from Jacobi import jacobi
from GaussSeidel import gaussSeidel
import LU


if __name__ == '__main__':
    N = 131
    matrix = Functions.generateBandMatrix(10, -1, -1, N)
    vectorB = Functions.generateBVector(N)


    jacobiResult, jacobiIterations, jacobiTime = jacobi(matrix, vectorB, 10 ** (-6))

    Functions.printMatrix(jacobiResult)
    print("Liczba iteracji: " + str(jacobiIterations))

    gaussSeidelResult, gaussSeidelIterations, gaussSeidelTime = gaussSeidel(matrix, vectorB, 10**(-6))

    Functions.printMatrix(gaussSeidelResult)
    print("Liczba iteracji: " + str(gaussSeidelIterations))

    print("\nPorównanie wyników:")
    print("Jacobi: czas - " + str(jacobiTime) + ", iteracje - " + str(jacobiIterations))
    print("Gauss-Seidl: czas - " + str(gaussSeidelTime)+ ", iteracje - " + str(gaussSeidelIterations))
    #for i in range(len(jacobiResult)):
    #    print(str(jacobiResult[i]) + " --- " + str(gaussSeidelResult[i]))

    LU.LUDecomposition(matrix)