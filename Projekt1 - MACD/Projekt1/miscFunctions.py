import csv

# pobranie danych o cenie akcji z pliku csv
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates


def importCSVData(filepath):
    file = open(filepath, 'r')
    values = []
    dates = []
    next(file)
    reader = csv.reader(file)
    for line in reader:
        values.append(float(line[4]))
        dates.append(line[0])

    return dates, values


def drawPlot(filepath):
    dates, values = importCSVData(filepath)
    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

    plt.plot(dates, values, color ='r')

    # ustawiamy rozmiar wykresu
    fig = plt.gcf()
    fig.set_size_inches(30, 15)
    fig.set_dpi(50)

    # wygląd wykresu

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plt.title("Asseco Poland SA", fontsize=50)
    plt.xlabel("Data", fontsize=30)
    plt.ylabel("Wartość akcji", fontsize=30)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.grid()
    plt.savefig('Graphs/asseco.png')
    plt.show()


