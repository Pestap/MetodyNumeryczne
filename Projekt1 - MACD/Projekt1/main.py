

import miscFunctions



# definicja plików wejsciowych i nazwy indeksu ktory bedziemy analziowac
csvFilepath = 'ORLEN.csv'
indexname = 'PKN ORLEN'

# pobranie danych z pliku csv
dates, values = miscFunctions.importCSVData(csvFilepath)

#obliczenie srednich kroczacych ema12 i ema26
ema12 = miscFunctions.calculateMovingAverage(12, values)
ema26 = miscFunctions.calculateMovingAverage(26, values)

#obliczenie macd i signal dla podanych srednich kroczacych
macd, signal = miscFunctions.calculateMACDandSignal(ema12, ema26)

# utworzenie wykresu
miscFunctions.drawMainPlot(dates, values, macd, signal, indexname)

