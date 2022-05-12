import pandas as pd


def importFromCSV(filename):
    """

    :param filename: nazwa pliku csv z danymi z pliku gpx
    :return: listy punktow w formacie (x,y,z) gdzie z to wysokosc
    """
    filepath = "Data/" + filename
    column_names = ["X", "Y", "ele"]
    df = pd.read_csv(filepath, usecols=column_names)
    x = df.X.to_list()
    y = df.Y.to_list()
    z = df.ele.to_list()

    points = [(x[i], y[i], z[i]) for i in range(len(x))]
    return points

def prepareData(filename, n):
    """

    :param filename: nazwa pliku csv
    :param n: liczba węzłów interpolacji
    :return: lista wszytskich wysokosci, lista wszysktich x dla wysokosci, lista wysokosic punktow interpolacji i lista xow interpolacji
    """

    points = importFromCSV(filename)

    # musimy wziąć n punktów w równych odstępach

    interval = len(points) // (n-1)
    interpolation_points = []
    for idx, point in enumerate(points):
        if idx % interval == 0:
            interpolation_points.append((point[2], idx))

    elevations_all_values = [elevation[2] for elevation in points]
    elevations_all_x = [i for i in range(len(points))]
    elevations_interpolation_values = [point[0] for point in interpolation_points]
    elevations_interpolation_x = [point[1] for point in interpolation_points]

    return elevations_all_values,elevations_all_x, elevations_interpolation_values, elevations_interpolation_x
