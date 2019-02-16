def swap_rows(matrix, row_1, row_2):
    row_temp = matrix[row_1]
    matrix[row_1] = matrix[row_2]
    matrix[row_2] = row_temp
    return matrix

def scale_row(matrix, row_index, scalar):
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] *= scalar
    return matrix

def add_rows(matrix, row_1, row_2):
    for i in range(len(matrix[row_1])):
        matrix[row_1][i] += matrix[row_2][i]
    return matrix

# manage first column
def row_reduce(matrix):
    # get 1 in top left corner
    matrix = scale_row(matrix, 0, 1/matrix[0][0])

    # get zeros in initial column
    for row_index in range(1, len(matrix)):
        print(matrix[row_index][0])
        matrix = scale_row(matrix, row_index, -1/matrix[row_index][0])
        matrix = add_rows(matrix, row_index, 0)

    # get ones in diagonal
    for row_index in range(1, len(matrix)):
        matrix = scale_row(matrix, row_index, 1/matrix[row_index][row_index])
    print(matrix)

    # for each row of each column, scale to -1 and add to diagonaled row
    for col_index in range(1, len(matrix[0])-1):
        for row_index in range(0, len(matrix)):
            if row_index == col_index:
                continue
            print("B" + " " + str(-matrix[col_index][col_index]/matrix[row_index][col_index]))
            matrix = scale_row(matrix, row_index, -matrix[col_index][col_index]/matrix[row_index][col_index])
            matrix = add_rows(matrix, row_index, col_index)
            print(matrix[0])
            print(matrix[1])
            print(matrix[2])
            #input()
    
    # scale to 1
    for row_index in range(len(matrix)):
        matrix = scale_row(matrix, row_index, 1/matrix[row_index][row_index])
    return matrix
