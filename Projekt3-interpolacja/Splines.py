import numpy as np
import scipy.linalg as scipy
from LU import LU

def find_section_number(x, x_arr):
    section_number = 0
    for i in range(len(x_arr)-1):
        if x > x_arr[i] and x <= x_arr[i+1]:
            return i

    return section_number

def construct_equations(x_arr, y_arr):
    section_amount = len(x_arr) - 1

    # macierz współczynników (4*n równań, gdzie n to liczba przedziałów)
    main_matrix = []
    vector = []
    for i in range(section_amount * 4):
        main_matrix.append([0] * section_amount * 4)
        vector.append([0])
    # wektor b


    # Si(xi) = f(xi)
    for i in range(section_amount):
        # Si(xi) = f(xi)
        main_matrix[i * 4][4 * i] = 1
        vector[4 * i][0] = y_arr[i]

        # Si(xi+1) = f(xi+1)
        for j in range(4):
            main_matrix[i * 4 + 1][j + 4 * i] = (x_arr[i + 1] - x_arr[i]) ** j
        vector[i * 4 + 1][0] = y_arr[i + 1]

        if i < section_amount - 1:
            # Si'(xi+1) = Si+1'(xi+1)
            for j in range(1, 4):
                main_matrix[i * 4 + 2][4 * i + j] = j * (x_arr[i + 1] - x_arr[i]) ** (j - 1)

            main_matrix[i * 4 + 2][4 * i + 5] = -1
            vector[i * 4 + 2][0] = 0

            # Si"(xi+1) = Si+1"(xi+1)
            main_matrix[i * 4 + 3][4 * i + 2] = 2
            main_matrix[i * 4 + 3][4 * i + 3] = 6 * (x_arr[i + 1] - x_arr[i])
            main_matrix[i * 4 + 3][4 * i + 6] = -2

            vector[i * 4 + 3][0] = 0

    # S0"(x0) = 0
    main_matrix[-2][2] = 2

    # Sn-1"(xn) = 0
    main_matrix[-1][-2] = 2
    main_matrix[-1][-1] = (x_arr[-1] - x_arr[-2]) * 6




    return main_matrix, vector

def splines(x_arr, y_arr, all_x):

    main_matrix, vector = construct_equations(x_arr, y_arr)



    result_partial = LU(main_matrix, vector)[0]

    result = [0]*len(all_x)


    for i in range(len(all_x)):
        #section nr
        section = find_section_number(all_x[i], x_arr)
        for idx, j in enumerate(range(4*section, 4*section+4)):
            result[i] += result_partial[j][0]*(all_x[i]-x_arr[section])**idx


    return result
