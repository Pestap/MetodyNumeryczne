

import functions





# definicja plików wejsciowych i nazwy indeksu ktory bedziemy analziowac
csvFilepath = 'CDP-krótki.csv'
indexname = 'CD PROJEKT RED - 4 lata'

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

start = 0
shares = 1000
# od 35 poniewaz od 35 daty zaczynają sięwszystkie wskaźniki
for i in range(1, len(signal)):
    prevDifference = macd[i - 1 + 9] - signal[i - 1]
    currentDifference = macd[i + 9] - signal[i]


    if currentDifference > 0 and prevDifference < 0:
        start, shares = functions.buyShares(values[i+35], start, shares)
    elif currentDifference < 0 and prevDifference > 0:
        start, shares = functions.sellShares(values[i+35], start, shares)

# sprzedajemy ostatniego dnia analizy całą resztę
start += shares*values[-1]

print("Wynik algorytmu: " + str(start))
