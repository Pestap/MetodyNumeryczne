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


def drawPlot(dates,values, ema):
    # dates, values = importCSVData(filepath)
    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

    plt.plot(dates, values, color ='r', label='cena udziałów')
    emaN = len(dates) - len(ema)
    plt.plot(dates[emaN:], ema, color='b',label='EMA')

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
    plt.savefig('Graphs/asseco.png')
    plt.show()

