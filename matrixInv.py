import numpy as np
from fractions import Fraction

a, b, c, d, e, f, g, h, i = 3, 4, 2, 5, 2, -4, -2, 3, 1


A = np.array([[a, b, c], [d, e, f], [g, h, i]])


def to_fraction(matrix):
    fraction_matrix = []
    for row in matrix:
        fraction_row = [Fraction(x).limit_denominator() for x in row]
        fraction_matrix.append(fraction_row)
    return fraction_matrix


try:
    A_inverse = np.linalg.inv(A)
    A_inverse_fraction = to_fraction(A_inverse)

    print("Matrix A:")
    for row in A:
        print(row)
    print("\nInverse of A:")
    for row in A_inverse:
        print(row)
    print("\n Inverse of A in fraction: ")
    for row in A_inverse_fraction:
        print(row)
except np.linalg.LinAlgError:
    print("Matrix A is singular and has no inverse.")


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


"""
B = np.array([[-4], [14], [8]])
print(matrix_multiply(A_inverse, B))
"""
