import gauss


# uses our homemade multiple regression algorithm
def calculate_coefficients(input_matrix, output_matrix, order=2):
    augmented = input_matrix
    for row in range(len(input_matrix)):
        augmented[row].append(output_matrix[row])
    reduced = gauss.row_reduce(augmented)
    
    coefficients = []
    for row in range(len(reduced)):
        coefficients.append(reduced[row][-1])
    return coefficients

#input_mat = [[2,3,5,3], [6,7,8,2], [10,11,12,5], [4,3,1,2]]
#output = [4,9,13,19]
