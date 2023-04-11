import numpy as np


a, b, c, d, e, f, g, h, i = 3, 5, -2, 4, 2, 3, 2, -4, 1


"""
# Define a 2x2 matrix
matrix_2x2 = np.array([[a, b],
                       [c, d]])
"""
# Define a 3x3 matrix
matrix_3x3 = np.array([[a, b, c], [d, e, f], [g, h, i]])


"""
# Calculate the determinant of the 2x2 matrix
determinant_2x2 = np.linalg.det(matrix_2x2)
print("Determinant of 2x2 matrix:", determinant_2x2)
"""
# Calculate the determinant of the 3x3 matrix
determinant_3x3 = np.linalg.det(matrix_3x3)
print("Determinant of 3x3 matrix:", determinant_3x3)
