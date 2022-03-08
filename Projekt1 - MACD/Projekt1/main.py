import matplotlib

import miscFunctions
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def calculateEMA(periods, values):
    result = []
    alfa = 2/(periods+1)
    for i in range(periods, len(values)):
        upper = 0
        lower = 0
        for j in range(periods+1):
            upper += (1-alfa)**j * values[i-j]
            lower += (1-alfa)**j
        result.append(upper/lower)
    return result

# narysowanie wykresu

csvFilepath = 'asseco.csv'
dates, values = miscFunctions.importCSVData(csvFilepath)
ema12 = calculateEMA(12, values)
ema26 = calculateEMA(26,values)
miscFunctions.drawPlot(dates, values, ema12,ema26)
