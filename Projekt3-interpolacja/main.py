from Lagrange import lagrange
import matplotlib.pyplot as plt
import numpy as np


xarr = [0, 2 ,3, 4]
yarr = [4, 1, 6, 1]

#TODO: Pobranie danych z pliku, wyznaczenie punktów pomiarowych (np. co 10)
#TODO: splajny

x_val = np.linspace(0,4,10)

y_res = lagrange(xarr, yarr, x_val)


plt.plot(x_val, y_res)
plt.show()

