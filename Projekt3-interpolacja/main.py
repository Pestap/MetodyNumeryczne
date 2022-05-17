import os

from Lagrange import lagrange
from Splines import splines
from ImportAndPrepareData import prepareData
import matplotlib.pyplot as plt


#TODO: Wykresy


#różne ilości węzłów interpolacji
interpolationPoints = [5,10,50,100]
data = os.listdir("Data")

#Dane do interpolacji
for i in interpolationPoints:
    for file in data:
        elevations_all_values,elevations_all_x, elevations_interpolation_values, elevations_interpolation_x = prepareData(file, i)

        if i <= 10:
            interpolation_result_lagrange = lagrange(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

        interpolation_result_splines = splines(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

        plt.clf()
        plt.scatter(elevations_interpolation_x, elevations_interpolation_values, marker='o', s=10, color="black", label="Węzły interpolacji")
        plt.plot(elevations_all_x, elevations_all_values, color="blue", linewidth="1", label="Faktyczne wartości funkcji")
        plt.plot(elevations_all_x, interpolation_result_splines, color="red", linewidth="1", label="Interpolacja funkcjami sklejanymi")
        if i <= 10:
            plt.plot(elevations_all_x, interpolation_result_lagrange, color="green", linewidth="1", label="Interpolacja metodą Lagrange'a")
        #plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=3)
        plt.legend(prop={'size': 8})
        plt.xlabel("Kolejne punkty pomiarowe")
        plt.ylabel("Wysokośc nad poziomem morza [m]")

        plt.title((file.split('.')[0]).replace("_"," "))
        plt.grid()

        plt.savefig("Plots/plot_"+ str(i)+"_points_" + file.split('.')[0] + ".png")



