import pandas as pd


def importFromCSV(filename):
    """

    :param filename: nazwa pliku csv z danymi z pliku gpx
    :return: listy punktow w formacie (x,y,z) gdzie z to wysokosc
    """
    filepath = "Data/" + filename
    column_names = ["X", "Y", "ele"]
    #wczytujemy interesujace nas kolumny
    df = pd.read_csv(filepath, usecols=column_names)

    #przekształcamy do list
    x = df.X.to_list()
    y = df.Y.to_list()
    z = df.ele.to_list()

    #pakujemy do jednej listy krotek
    points = [(x[i], y[i], z[i]) for i in range(len(x))]
    return points

def prepareData(filename, n):
    """

    :param filename: nazwa pliku csv
    :param n: liczba węzłów interpolacji
    :return: lista wszytskich wysokosci, lista wszysktich x dla wysokosci, lista wysokosic punktow interpolacji i lista xow interpolacji
    """
    if n < 2:
        raise Exception("Invalid number of interpolation points - cannot be lower than 2, was: " + str(n))
    points = importFromCSV(filename)

    # musimy wziąć n punktów w równych odstępach

    interval = (len(points) - 1) // (n-1)

    #w liscie interpolation points mamy: wartośc funkcji w punkcie x,y oraz indeks
    interpolation_points = []
    for idx, point in enumerate(points):
        if idx % interval == 0:
            interpolation_points.append((point[2], idx))

    #dodajemy ostatni punkt pomiarowy
    interpolation_points.append((points[-1][2], len(points)-1))
    #usuwamy przedostatni - ostatni przedział będzie dłuższy niż pozostałe(lepiej niż bardzo mały)
    interpolation_points.pop(-2)


    #rozpakowujemy punkty
    #pobieramy wartosci funkcji dla wszystkich punktów
    elevations_all_values = [elevation[2] for elevation in points]
    #pobieramy wszystkie wartosci xow - kolejne numery pomiarów
    elevations_all_x = [i for i in range(len(points))]

    #pobieramy wartości funkcji w węzłach interpolacji
    elevations_interpolation_values = [point[0] for point in interpolation_points]
    #pobieramy wartości x-ow w węzłach interpolacji
    elevations_interpolation_x = [point[1] for point in interpolation_points]

    return elevations_all_values, elevations_all_x, elevations_interpolation_values, elevations_interpolation_x
