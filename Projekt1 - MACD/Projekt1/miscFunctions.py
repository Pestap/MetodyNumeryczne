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


def drawPlot(dates, values, ema1, ema2):
    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

    plt.plot(dates, values, color ='r', label='Cena udziałów')
    ema1period = len(dates) - len(ema1)
    plt.plot(dates[ema1period:], ema1, color='b', label="$EMA_{" + str(ema1period) + "}$")

    ema2period = len(dates) - len(ema2)
    plt.plot(dates[ema2period:], ema2, color='g', label="$EMA_{" + str(ema2period) + "}$" )
    # ustawiamy rozmiar wykresu
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

