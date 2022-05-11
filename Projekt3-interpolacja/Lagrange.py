def phi(i, x_arr, x):
    """
    :param i: ktora funkjca phi_i
    :param x_arr: lista punktów pomiaru
    :param x: dla tego x liczymy funkcje
    :return: wartosc funkcji phi_i  w punkcie x
    """
    result = 1
    for j in range(len(x_arr)):
        if j != i:
            result *= (x - x_arr[j])/(x_arr[i] - x_arr[j])
    return result


def lagrange(x_arr, y_arr, all_x):
    """

    :param x_arr: współrzędne x punktów pomiaru
    :param y_arr: wpsółrzędne y puktów pomiaru
    :param all_x: wszystkie x dla których chcemy uzysakć wartość interpolowanej funkcji
    :return: wartości funkcji w punktach all_x
    """
    #inicjalizacja tablicy wyników - taka sama długośc jak tablica x dla których będziemy liczyć wartości funkcji

    result = [0]*len(all_x)

    for i in range(len(all_x)):
        #liczymy i-ty wyraz
        for j in range(len(x_arr)):
            #j-ta funkcja phi * y_j
            result[i] += phi(j, x_arr, all_x[i]) * y_arr[j]

    return result

