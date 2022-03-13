

import miscFunctions


def buyShares(sharePrice, capital, shares):
    while(True):
        if capital >= sharePrice:
            capital -= sharePrice
            shares = shares + 1
        else:
            break
    return capital, shares

def sellShares(sharePrice, capital, shares):
    while(True):
        if shares > 0:
            capital += sharePrice
            shares = shares - 1
        else:
            break
    return capital, shares
# definicja plików wejsciowych i nazwy indeksu ktory bedziemy analziowac
csvFilepath = 'CDP.csv'
indexname = 'CD PROJEKT RED'

# pobranie danych z pliku csv
dates, values = miscFunctions.importCSVData(csvFilepath)

#obliczenie srednich kroczacych ema12 i ema26
ema12 = miscFunctions.calculateMovingAverage(12, values)
ema26 = miscFunctions.calculateMovingAverage(26, values)

#obliczenie macd i signal dla podanych srednich kroczacych
macd, signal = miscFunctions.calculateMACDandSignal(ema12, ema26)

# utworzenie wykresu
miscFunctions.drawMainPlot(dates, values, macd, signal, indexname)



# algorytm kupowania

start = 1000
shares = 0
# od 35 poniewaz od 35 daty zaczynają sięwszystkie wskaźniki
for i in range(1, len(signal)):
    prevDifference = macd[i - 1 + 9] - signal[i - 1]
    currentDifference = macd[i + 9] - signal[i]


    if currentDifference > 0 and prevDifference < 0:
        start,shares = buyShares(values[i+35], start, shares)
    elif currentDifference < 0 and prevDifference > 0:
        start,shares = sellShares(values[i+35], start, shares)

# sprzedajemy ostatniego dnia analizy całą resztę
start += shares*values[-1]

print("Wynik algorytmu: " + str(start))
