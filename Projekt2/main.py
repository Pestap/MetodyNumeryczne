import Functions
from Jacobi import jacobi
from GaussSeidel import gaussSeidel
from LU import LU


if __name__ == '__main__':
    N = 2000
    matrix = Functions.generateBandMatrix(10, -1, -1, N)
    vectorB = Functions.generateBVector(N)


    jacobiResult, jacobiIterations, jacobiTime = jacobi(matrix, vectorB, 10 ** (-6))

    #Functions.printMatrix(jacobiResult)
    #print("Liczba iteracji (Jc): " + str(jacobiIterations))

    gaussSeidelResult, gaussSeidelIterations, gaussSeidelTime = gaussSeidel(matrix, vectorB, 10**(-6))

    #Functions.printMatrix(gaussSeidelResult)
    #print("Liczba iteracji (GS): " + str(gaussSeidelIterations))




    LUresult, LUtime  = LU(matrix,vectorB)

    print("Jacobi --- Gauss-Seidl --- LU")
    for i in range(len(jacobiResult)):
        print(str(jacobiResult[i]) + " --- " + str(gaussSeidelResult[i]) + " --- " + str(LUresult[i]))

    print("\nPorównanie wyników:")
    print("Jacobi: czas - " + str(jacobiTime) + "s , iteracje - " + str(jacobiIterations))
    print("Gauss-Seidl: czas - " + str(gaussSeidelTime)+ "s , iteracje - " + str(gaussSeidelIterations))
    print("Faktoryzacja LU: czas -  " + str(LUtime) + "s")