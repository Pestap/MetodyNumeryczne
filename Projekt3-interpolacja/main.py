import os

from Lagrange import lagrange
from Splines import splines
from ImportAndPrepareData import prepareData
import matplotlib.pyplot as plt


def generate_plots(filename, n, random_point_distibution=False):
    """

    :param filename: nazwa pliku .gpx
    :param random_point_distibution: czy rozkłąd punktów ma być losowy
    :param n: liczba węzłów interpolacji
    :return: zapis wykresu
    """
    elevations_all_values, elevations_all_x, elevations_interpolation_values, elevations_interpolation_x = prepareData(filename, n, random_point_distibution)

    # interpolacja Lagrange tylko dla n <=10
    if n <= 10:
        interpolation_result_lagrange = lagrange(elevations_interpolation_x, elevations_interpolation_values,
                                                 elevations_all_x)

    interpolation_result_splines = splines(elevations_interpolation_x, elevations_interpolation_values,
                                           elevations_all_x)

    suffix = "regularne" if not random_point_distibution else "losowe"
    title = (filename.split('.')[0]).replace("_", " ") + " (" + str(i) + ") " + suffix
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
    plt.savefig("Plots/plot_" + str(i) + "_points_" + filename.split('.')[0] + "_"+suffix+".png")


# różne ilości węzłów interpolacji
interpolationPoints = [5, 8, 10, 25, 50, 75, 100, 200]
# interpolationPoints = [100, 200]
data = os.listdir("Data")


# dla różnych liczb punktów interpolacji
for i in interpolationPoints:
    # dla wszystkich plików znajdujących się w folderze
    for file_csv in data:
        generate_plots(file_csv, i, False)
        generate_plots(file_csv, i, True)
