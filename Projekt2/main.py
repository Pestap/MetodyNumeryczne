import Functions
import matplotlib.pyplot as plt
from Jacobi import jacobi
from GaussSeidel import gaussSeidel
from LU import LU


if __name__ == '__main__':
    N = 931
    epsilon = 10 ** (-9)
    matrixA = Functions.generateBandMatrix(10, -1, -1, N)
    matrixC = Functions.generateBandMatrix(3,-1,-1, N)
    vectorB = Functions.generateBVector(N)

    #zadanie B
    print("Zadanie B")
    jacobiResult, jacobiIterations, jacobiTime = jacobi(matrixA, vectorB, epsilon)
    gaussSeidelResult, gaussSeidelIterations, gaussSeidelTime = gaussSeidel(matrixA, vectorB, epsilon)

    #To w sumie jest dodatkowo
    LUresult, LUtime  = LU(matrixA,vectorB)

    print("Jacobi --- Gauss-Seidl --- LU")
    for i in range(len(jacobiResult)):
        print(str(jacobiResult[i]) + " --- " + str(gaussSeidelResult[i]) + " --- " + str(LUresult[i]))

    print("\nPorównanie wyników:")
    print("Jacobi: czas - " + str(jacobiTime) + "s , iteracje - " + str(jacobiIterations) + ", norma z wektora residuum: " + str(Functions.calculateResiduumNorm(matrixA, jacobiResult, vectorB)))
    print("Gauss-Seidl: czas - " + str(gaussSeidelTime)+ "s , iteracje - " + str(gaussSeidelIterations) + ", norma z wektora residuum: " + str(Functions.calculateResiduumNorm(matrixA, gaussSeidelResult, vectorB)))
    print("Faktoryzacja LU: czas -  " + str(LUtime) + " s, " + "norma z wektora residuum: " + str(Functions.calculateResiduumNorm(matrixA, LUresult, vectorB)))
    print()

    #Zad C i D

    print("Zadanie C i D: \n")
    LUResultC, LUTimeC = LU(matrixC, vectorB)
    JacobiResultC,JacobiIterationsC, JacobiTimeC = jacobi(matrixC, vectorB, epsilon)
    GSResultC, GSIterationsC, GSTimeC = gaussSeidel(matrixC,vectorB, epsilon)
    print("Faktoryzacja LU: czas -  " + str(LUTimeC) + "s, " + "norma z wektora residuum: " + str(
        Functions.calculateResiduumNorm(matrixC, LUResultC, vectorB)))


    #TODO: Wykres czasu trwania od liczby niewiadomych

    #nArray = [100, 500, 1000, 2000, 3000]
    nArray = [10, 20, 30, 50, 100, 200, 500]
    timesJacobi = []
    timesGS = []
    timesLU = []

    for i in nArray:
        matrixI = Functions.generateBandMatrix(10, -1, -1, i)
        vectorBI = Functions.generateBVector(i)

        jacobiItime = jacobi(matrixI, vectorBI, epsilon)[2]
        gsItime = gaussSeidel(matrixI, vectorBI, epsilon)[2]
        luTime = LU(matrixI, vectorBI)[1]
        timesJacobi.append(jacobiItime)
        timesGS.append(gsItime)
        timesLU.append(luTime)


    plt.plot(nArray, timesJacobi)
    plt.plot(nArray, timesGS)
    plt.plot(nArray, timesLU)
    plt.title("Porównanie czasu działania metod w zależności od liczby zmiennych")
    plt.xlabel("Liczba zmiennych N")
    plt.ylabel("Czas [s]")
    plt.yscale('log')
    plt.legend(["Jacobi", "Gauss-Seidel", "Faktoryzacja LU"])
    plt.savefig("Images/wykresZadE.png")
    plt.show()


    #TODO: Porównanie z gotowcami z numpy, ale to zrobić w oddzielnym pliku