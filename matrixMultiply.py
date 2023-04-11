def matrix_multiply(A, B):
    # Get the dimensions of the input matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError(
            "The number of columns in matrix A must be equal to the number of rows in matrix B."
        )

    # Create an empty result matrix with the appropriate dimensions
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform the matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Example usage:
A = [[1, 2, 3], [4, 5, 6]]

B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

C = matrix_multiply(A, B)
print(C)
