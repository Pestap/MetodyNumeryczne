import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np


def importCSVData(filepath):
    column_names = ['Data', 'Zamkniecie']
    df = pd.read_csv(filepath, usecols=column_names)
    values = df.Zamkniecie.to_list()
    dates = df.Data.to_list()
    return dates, values

def calculateMovingAverage(periods, values):
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

def calculateMACDandSignal(ema12, ema26):
    macd = []
    for i in range(len(ema26)):
        # + 14 ponieważ EMA12 jest o 14 dluzsze
        macd.append(ema12[i+14] - ema26[i])
    signal = calculateMovingAverage(9, macd)
    return macd, signal


def calculateBuyAndSellPoints(dates, macd, signal):
    sellPoints = []
    buyPoints = []
    for i in range(1, len(signal)):

        prevDifference = macd[i - 1 + 9] - signal[i - 1]
        currentDifference = macd[i + 9] - signal[i]

        if prevDifference >= 0 and currentDifference <= 0:
            # moment sprzedarzy
            sellPoints.append(dates[i + 35])
        elif prevDifference <= 0 and currentDifference >= 0:
            # moment kupna
            buyPoints.append(dates[i + 35])
    return buyPoints, sellPoints


# potrzebna jeszcze funckja do obliczenia SIGNAL
# do rysowania wykresu SIGNAL i MACD
def drawMainPlot(dates, values, macd, signal, indexname):
    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    # od 26 poniewaz dla pierwszych 26 elementow nie policzymy MACD (wymaga EMA26)

    fig, (ax1,ax2) = plt.subplots(2, sharex=True)

    # dziwne początki pozwalają na rozpoczęcie 3 linii jednocześnie
    # w pierwszym można usunąc oba
    # w drugim dates[26:], macd
    # trzeci musi zostać
    ax1.plot(dates[35:], values[35:], color='#000066', label='Cena udziałów', linewidth =1.2)
    ax2.plot(dates[35:], macd[9:], color='b', label="MACD", linewidth=0.8)
    ax2.plot(dates[35:], signal, color='r', label="SIGNAL", linewidth=0.8)

    # zaczynamy od 1 bo będziemy sprawdzać poprzedni
    buyPoints, sellPoints = calculateBuyAndSellPoints(dates, macd, signal)


    for i in sellPoints:
        ax1.axvline(i, linewidth=0.75, color='r', linestyle='dashed')
    for i in buyPoints:
        ax1.axvline(i, linewidth=0.75, color='g', linestyle='dashed')

    # legendy do linii kupna i sprzedaży
    ax1.plot([], [], 'r--', label='Sell')
    ax1.plot([], [], 'g--', label='Buy')

    # rozmiar wykresu
    fig.set_size_inches(30, 15)
    fig.set_dpi(50)

    # tytuł wykresu
    fig.suptitle(indexname, fontsize=40)


    #ustawienie znaczników na osi X
    tickinterval = int(len(signal)/20)
    ax1.set_xticks(dates[::tickinterval])
    plt.xticks(rotation=25)

    #usunięcie marginesów
    ax1.margins(x=0)

    # wygląd wykresu
    plt.xlabel("Data", fontsize=20, loc="left")

    ax1.set_title("Wartość udziałów", fontsize=20)
    ax1.set_ylabel("Cena", fontsize=18)

    ax2.set_title("MACD oraz Signal", fontsize=20)
    ax2.set_ylabel("Wartość", fontsize=18)
    plt.tick_params('y', labelsize=14)
    plt.tick_params('x', labelsize=14)

    ax1.legend(loc=2, prop={'size': 20})
    ax2.legend(loc=2, prop={'size': 20})

    # kratka
    ax1.grid()
    ax2.grid()

    #zapis w katalogu graphs
    resultpath = "Graphs/" + indexname + ".png"
    plt.savefig(resultpath)

    #wyswietlenie wykresu
    plt.show()

