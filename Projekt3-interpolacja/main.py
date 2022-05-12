from Lagrange import lagrange
from Splines import splines
from ImportAndPrepareData import prepareData
import matplotlib.pyplot as plt
import numpy as np


xarr = [0, 2 ,3, 4]
yarr = [4, 1, 6, 1]

#TODO: Pobranie danych z pliku, wyznaczenie punktów pomiarowych (np. co 10)
#TODO: splajny

#x_val = np.linspace(0,4,10)

#y_res = lagrange(xarr, yarr, x_val)
#plt.plot(x_val, y_res)

elevations_all_values,elevations_all_x, elevations_interpolation_values, elevations_interpolation_x = prepareData("track_points.csv", 6)

interpolation_result = lagrange(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

plt.scatter(elevations_interpolation_x, elevations_interpolation_values, marker='o', s=10, color="black", label="punkty interpolacji")
plt.plot(elevations_all_x, elevations_all_values, color="blue", linewidth="1", label="wyskość faktyczna")
plt.plot(elevations_all_x, interpolation_result, color="red", linewidth="1", label="rezultat interpolacji")
plt.legend()
plt.grid()
#plt.margins(x=0)
plt.show()

#splines(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

