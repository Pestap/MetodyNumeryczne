def splines(x_arr, y_arr, all_x):
    section_amount = len(x_arr) - 1

    #macierz współczynników (4*n równań, gdzie n to liczba przedziałów)
    main_matrix = [[0]*section_amount*4]*section_amount*4

    #wektor b
    vector = [0]*section_amount*4


    # Si(xi) = f(xi)
    for i in range(len(section_amount)):
        #Si(xi) = f(xi)
        main_matrix[i*section_amount][4*i] = 1
        vector[4*i] = y_arr[i]

        #Si(xi+1) = f(xi+1)
        for j in range(4):
            main_matrix[i*section_amount + 1][j] = (x_arr[i+1] -x_arr[i])**j
        vector[4*i +1] = y_arr[i+1]


