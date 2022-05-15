from Lagrange import lagrange
from Splines import splines
from ImportAndPrepareData import prepareData
import matplotlib.pyplot as plt
import numpy as np


xarr = [1, 3 ,5]
yarr = [6, -2, 4]

#TODO: Pobieranie danych z innych plików

x_val = np.linspace(1,5,40)

#y_res = lagrange(xarr, yarr, x_val)
#plt.plot(x_val, y_res)

elevations_all_values,elevations_all_x, elevations_interpolation_values, elevations_interpolation_x = prepareData("glownagran.csv", 40)

#interpolation_result = lagrange(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

interpolation_result = splines(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

#interpolation_result = splines(xarr,yarr, x_val)

plt.scatter(elevations_interpolation_x, elevations_interpolation_values, marker='o', s=10, color="black", label="punkty interpolacji")
plt.plot(elevations_all_x, elevations_all_values, color="blue", linewidth="1", label="wyskość faktyczna")
plt.plot(elevations_all_x, interpolation_result, color="red", linewidth="1", label="rezultat interpolacji")
#plt.plot(x_val, interpolation_result)
plt.legend()
plt.grid()
#plt.margins(x=0)
plt.show()

#splines(elevations_interpolation_x, elevations_interpolation_values, elevations_all_x)

