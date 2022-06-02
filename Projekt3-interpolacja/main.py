import os

from Lagrange import lagrange
from Splines import splines
from ImportAndPrepareData import prepareData
import matplotlib.pyplot as plt

def get_results(file, n, random_point_distibution=False):
    """

    :param file: nazwa pliku .gpx
    :param n: liczba węzłów interpolacji
    :return: zapis wykresu
    """
    elevations_all_values, elevations_all_x, elevations_interpolation_values, elevations_interpolation_x = prepareData(file, n, random_point_distibution)

    #interpolacja Lagrange tylko dla n <=10
    if n <= 10:
        interpolation_result_lagrange = lagrange(elevations_interpolation_x, elevations_interpolation_values,
                                                 elevations_all_x)

    interpolation_result_splines = splines(elevations_interpolation_x, elevations_interpolation_values,
                                           elevations_all_x)


    suffix = "regularne" if random_point_distibution == False else "losowe"
    title = (file.split('.')[0]).replace("_", " ") + " (" + str(i) + ")_" + suffix
    plt.clf()
    plt.scatter(elevations_interpolation_x, elevations_interpolation_values, marker='o', s=10, color="black",
                label="Węzły interpolacji")
    plt.plot(elevations_all_x, elevations_all_values, color="blue", linewidth="1", label="Faktyczne wartości funkcji")
    plt.plot(elevations_all_x, interpolation_result_splines, color="red", linewidth="1",
             label="Interpolacja funkcjami sklejanymi")
    if i <= 10:
        plt.plot(elevations_all_x, interpolation_result_lagrange, color="green", linewidth="1",
                 label="Interpolacja metodą Lagrange'a")

    plt.legend(prop={'size': 8})
    plt.xlabel("Kolejne punkty pomiarowe")
    plt.ylabel("Wysokośc nad poziomem morza [m]")

    plt.title(title)
    plt.grid()
    plt.savefig("Plots/plot_" + str(i) + "_points_" + file.split('.')[0] + "_"+suffix+".png")




#różne ilości węzłów interpolacji
interpolationPoints = [5, 8 ,10, 25 ,50,100, 200]
data = os.listdir("Data")


el_all, ell_all_x, el_int, el_int_x = prepareData("Rysy.csv", 10, True)
interpolation_result_splines = splines(el_int_x, el_int, ell_all_x)

plt.scatter(el_int_x, el_int, marker='o', s=10, color="black",
            label="Węzły interpolacji")
plt.plot(ell_all_x, el_all, color="blue", linewidth="1", label="Faktyczne wartości funkcji")
plt.plot(ell_all_x, interpolation_result_splines, color="red", linewidth="1",label="Interpolacja funkcjami sklejanymi")
plt.show()
#Dane do interpolacji


for i in interpolationPoints[:3]: # dla różnych liczb punktów interpolacji
    for file in data: # dla wszystkich plików znajdujących się w folderze
        get_results(file,i,False)
        get_results(file,i,True)






