

import functions



# definicja plików wejsciowych i nazwy indeksu ktory bedziemy analziowac
csvFilepath = 'PKOBP.csv'
indexname = 'PKO BP'

csvFilepath = 'CSV/' + csvFilepath

# pobranie danych z pliku csv
dates, values = functions.importCSVData(csvFilepath)

#obliczenie srednich kroczacych ema12 i ema26
ema12 = functions.calculateMovingAverage(12, values)
ema26 = functions.calculateMovingAverage(26, values)

#obliczenie macd i signal dla podanych srednich kroczacych
macd, signal = functions.calculateMACDandSignal(ema12, ema26)

# utworzenie wykresu
functions.drawMainPlot(dates, values, macd, signal, indexname)



# algorytm inwestujący

cash = 0
shares = 1000
startVal = shares*values[35] + cash


cash, shares = functions.simpleAlgorithm(shares, cash, values, macd, signal)

profit = (shares*values[-1] + cash)/(1000*values[36])


cash_a = 0
shares_a = 1000

cash_a,shares_a = functions.advancedAlgorithm(shares_a,cash_a,values,macd,signal)

profit_a = (shares_a*values[-1] + cash_a)/(1000*values[36])
print("Początkowy kapitał: 1000 akcji")
print("Wynik algorytmu podstawowego: " + str(profit) + "\nJest stosunek posiadanego kapitału do kapitału z początku działania algorytmu")
print("===== Algorytm rozszerzony =====")
print("Początkowy kapitał: 1000 akcji")
print("Wynik algorytmu rozszerzonego: " + str(profit_a) + "\nJest stosunek posiadanego kapitału do kapitału z początku działania algorytmu")


