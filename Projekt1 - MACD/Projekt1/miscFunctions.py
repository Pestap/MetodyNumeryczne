import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd


def importCSVData(filepath):
    column_names = ['Data', 'Zamkniecie']
    df = pd.read_csv(filepath, usecols=column_names)
    values = df.Zamkniecie.to_list()
    dates = df.Data.to_list()
    return dates, values

def calculateMACD(ema12, ema26):
    # bedzie zwracac MACD ( i moze SIGNAL??)
    pass
# potrzebna jeszcze funckja do obliczenia SIGNAL
# do rysowania wykresu SIGNAL i MACD
def drawMainPlot(dates, values, ema1, ema2):
    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    # od 26 poniewaz dla pierwszych 26 elementow nie policzymy MACD

    plt.plot(dates[26:], values[26:], color ='r', label='Cena udziałów')
    ema1period = len(dates) - len(ema1)
    ema2period = len(dates) - len(ema2)

    # to jest chwilowe rozwiązanie zahardkodowane - to bedzie sie znajdowac w funkcji calculateMACD
    # drawPlot - > ma tylko rysowac wykres wartosci akcji
    plt.plot(dates[26:], ema1[14:], color='b', label="$EMA_{" + str(ema1period) + "}$")


    plt.plot(dates[26:], ema2, color='g', label="$EMA_{" + str(ema2period) + "}$" )
    # ustawiamy rozmiar wykresu

    # liczymy MACD

    #macd =[]

    # zakładamy że ema1 jest ema o krótszym okresie - mamy więcej rekordów
    #for i in range(len(ema2)):
     #   macd.append(ema1[i] - ema2[i])

    #plt.plot(dates[ema2period:], macd, color='y',label="MACD", linewidth=2)

    fig = plt.gcf()
    fig.set_size_inches(30, 15)
    fig.set_dpi(50)

    # wygląd wykresu

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))

    plt.title("Asseco Poland SA", fontsize=50)
    plt.xlabel("Data", fontsize=30)
    plt.ylabel("Wartość akcji", fontsize=30)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.grid()
    plt.legend(loc=2,prop={'size':30})

    plt.savefig('Graphs/asseco.png')
    plt.show()

