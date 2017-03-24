def get_max_sized_square_sub_matrix(matrix):
    max_size = []
    # print matrix[0]
    # max_size.append(matrix[0])

    for idx, array in enumerate(matrix):
        max_size.append([])
        for idy, value in enumerate(array):
            if (idx == 0) or (idy == 0):
                max_size[idx].append(value)
            else:
                max_size[idx].append(0)

    for i in range(1, len(max_size) - 1):
        for j in range(1, len(max_size[0]) - 1):

            if matrix[i][j] == 1:
                max_size[i][j] = min(max_size[i - 1][j], max_size[i - 1][j - 1], max_size[i][j - 1]) + 1
            else:
                max_size[i][j] = 0

    return max(max(max_size))

print get_max_sized_square_sub_matrix([[0, 1, 1, 0, 1],
                                       [1, 1, 0, 1, 0],
                                       [0, 1, 1, 1, 0],
                                       [1, 1, 1, 1, 0],
                                       [1, 1, 1, 1, 1],
                                       [0, 0, 0, 0, 0]])
