import curves.gauss


# uses gauss elimination to determine the curve fitting coefficients
def calculate_coefficients(input_matrix, output_matrix):
    augmented = input_matrix
    for row in range(len(input_matrix)):
        augmented[row].append(output_matrix[row])
    reduced = curves.gauss.row_reduce(augmented)
    
    coefficients = []
    for row in range(len(reduced)):
        coefficients.append(reduced[row][-1])
    return coefficients


# uses our homemade regression algorithm to get a polynomial regression
def polynomial_regression(input_data, output_data):
    variables = len(input_data[0])  # number of input variables present: x^2, x, y^2, y
    entries = len(input_data)  # number of training data
    if entries < variables:
        print("Not enough data")
        return
    
    coefficients = [.5] * variables  # initializes all coefficients to .5
    trainings = 0  # iterator count for trainings
    # uses the input data to determine/adjust the coefficients
    for i in range(0, entries, variables):
        trainings += 1
        input_matrix = input_data[i:i+variables]  # gets a subset of the input data
        output_matrix = output_data[i:i+variables]  # gets a subset of the output data
        results = calculate_coefficients(input_matrix, output_matrix)  # finds the coefficients using these subsets
        # adjusts each coefficient slightly (less so with more input)
        # NOTE: We may get better results with using a non-one power of n (sqrt n, n^2, etc), so training converges slower
        for coefficient_index in range(len(results)):  
            adjustment = (results[coefficient_index]-coefficients[coefficient_index]) / (trainings ** 2)
            if adjustment > 1:
                coefficients[coefficient_index] += 0
            elif adjustment < -1:
                coefficients[coefficient_index] += 0
            else:
                coefficients[coefficient_index] += adjustment
    
    return coefficients
    
