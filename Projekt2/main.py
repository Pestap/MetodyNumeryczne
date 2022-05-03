import Functions
import matplotlib.plot as plt
from Jacobi import jacobi
from GaussSeidel import gaussSeidel
from LU import LU


if __name__ == '__main__':
    N = 131
    epsilon = 10 ** (-9)
    matrixA = Functions.generateBandMatrix(10, -1, -1, N)
    matrixC = Functions.generateBandMatrix(3,-1,-1, N)
    vectorB = Functions.generateBVector(N)

    #zadanie B
    print("Zadanie B")
    jacobiResult, jacobiIterations, jacobiTime = jacobi(matrixA, vectorB, 10 ** (-9))
    gaussSeidelResult, gaussSeidelIterations, gaussSeidelTime = gaussSeidel(matrixA, vectorB, 10**(-9))

    #To w sumie jest dodatkowo
    LUresult, LUtime  = LU(matrixA,vectorB)

    print("Jacobi --- Gauss-Seidl --- LU")
    for i in range(len(jacobiResult)):
        print(str(jacobiResult[i]) + " --- " + str(gaussSeidelResult[i]) + " --- " + str(LUresult[i]))

    print("\nPorównanie wyników:")
    print("Jacobi: czas - " + str(jacobiTime) + "s , iteracje - " + str(jacobiIterations) + "norma z wektora residuum: " + str(Functions.calculateResiduumNorm(matrixA, jacobiResult, vectorB)))
    print("Gauss-Seidl: czas - " + str(gaussSeidelTime)+ "s , iteracje - " + str(gaussSeidelIterations) + "norma z wektora residuum: " + str(Functions.calculateResiduumNorm(matrixA, gaussSeidelResult, vectorB)))
    print("Faktoryzacja LU: czas -  " + str(LUtime) + "s, " + "norma z wektora residuum: " + str(Functions.calculateResiduumNorm(matrixA, LUresult, vectorB)))
    print()

    #Zad C i D

    print("Zadanie C i D: \n")
    LUResultC, LUTimeC = LU(matrixC, vectorB)
    JacobiResultC,JacobiIterationsC, JacobiTimeC = jacobi(matrixC, vectorB, epsilon)
    GSResultC, GSIterationsC, GSTimeC = gaussSeidel(matrixC,vectorB, epsilon)
    print("Faktoryzacja LU: czas -  " + str(LUTimeC) + "s, " + "norma z wektora residuum: " + str(
        Functions.calculateResiduumNorm(matrixC, LUResultC, vectorB)))


    #TODO: Wykres czasu trwania od liczby niewiadomych

    nArray = [100, 500, 1000, 2000, 3000]
    timesJacobi = [0]*len(nArray)
    timesGS = [0]*len(nArray)
    timesLU = [0]*len(nArray)

    for i in nArray:
        jacobiItime = jacobi(matrixA, vectorB, epsilon)[2]
        gsItime = gaussSeidel(matrixA, vectorB, epsilon)[2]
        luTime = LU(matrixA, vectorB)[1]
        timesJacobi[i] = jacobiItime
        timesGS[i] = gsItime
        timesLU[i] = luTime






    #TODO: Porównanie z gotowcami z numpy, ale to zrobić w oddzielnym pliku