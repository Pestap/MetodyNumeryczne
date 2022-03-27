import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd


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


def drawMainPlot(dates, values, macd, signal, indexname):
    #formatowanie daty
    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    # od 26 poniewaz dla pierwszych 26 elementow nie policzymy MACD (wymaga EMA26)

    fig, (ax1,ax2) = plt.subplots(2, sharex=True)

    # dziwne początki pozwalają na rozpoczęcie 3 linii jednocześnie
    # w pierwszym można usunąc oba
    # w drugim dates[26:], macd
    # singal jest najpóźniej dostępną wartością
    ax1.plot(dates[35:], values[35:], color='#000066', label='Cena udziałów', linewidth =1.2)
    ax2.plot(dates[35:], macd[9:], color='b', label="MACD", linewidth=0.8)
    ax2.plot(dates[35:], signal, color='r', label="SIGNAL", linewidth=0.8)

    # zaczynamy od 1 bo będziemy sprawdzać poprzedni

    # rozmiar wykresu
    fig.set_size_inches(30, 15)
    fig.set_dpi(40)

    # tytuł wykresu - wyśrodkowany

    mid = (fig.subplotpars.right + fig.subplotpars.left)/2
    fig.suptitle(indexname, fontsize=40, x=mid)


    #ustawienie znaczników na osi X
    tickinterval = int(len(signal)/20)
    ax1.set_xticks(dates[::tickinterval])
    plt.xticks(rotation=25)

    #usunięcie marginesów wewnątrz
    ax1.margins(x=0)

    # tytuł osi X (wspólnej)
    plt.xlabel("Data", fontsize=20, loc="left")

    #tytuły wykresów
    ax1.set_title("Wartość udziałów", fontsize=25)
    ax1.set_ylabel("Cena", fontsize=20)

    ax2.set_title("MACD oraz Signal", fontsize=25)
    ax2.set_ylabel("Wartości wskaźników", fontsize=20)

    # rozmiar wartości na osiach
    plt.tick_params('y', labelsize=14)
    plt.tick_params('x', labelsize=14)


    #legendy
    ax1.legend(loc=2, prop={'size': 15})
    ax2.legend(loc=2, prop={'size': 15})

    # kratka
    ax1.grid()
    ax2.grid()

    #zapis w katalogu graphs
    resultpath = "Graphs/" + indexname + ".png"
    plt.tight_layout(pad=8)
    plt.savefig(resultpath)

    #wyswietlenie wykresu
    plt.show()


# funckje dla algorytmu inwestującego
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


def simpleAlgorithm(initial_shares, initial_balance, values, macd, signal):
    cash = initial_balance
    shares = initial_shares
    for i in range(1, len(signal)):
        prevDifference = macd[i - 1 + 9] - signal[i - 1]
        currentDifference = macd[i + 9] - signal[i]

        if currentDifference > 0 and prevDifference < 0:
            cash, shares = buyShares(values[i + 35], cash, shares)
        elif currentDifference < 0 and prevDifference > 0:
            cash, shares = sellShares(values[i + 35], cash, shares)

    return cash,shares


def advancedAlgorithm(initial_shares, initial_balance, values, macd, signal):
    cash = initial_balance
    shares = initial_shares

    last_sold_price = -1000 * values[0]
    last_bought_price = -1000 *values[0]
    last_bought_at = 0
    last_sold_at =0
    for i in range(1, len(signal)):
        prevDifference = macd[i - 1 + 9] - signal[i - 1]
        currentDifference = macd[i + 9] - signal[i]

        if i - last_sold_at == 31:
           last_bought_price = -1000 * values[0]
        elif currentDifference > 0 and prevDifference < 0:
            cash, shares = buyShares(values[i + 35], cash, shares)
            last_bought_price = values[i+35]
            last_bought_at = i

        elif currentDifference < 0 and prevDifference > 0 and values[i+35] > last_bought_price:
            cash, shares = sellShares(values[i + 35], cash, shares)
            last_sold_at = i
            last_sold_price = values[i+35]

    return cash, shares