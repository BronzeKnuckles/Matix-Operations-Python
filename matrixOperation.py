import numpy as np


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def solve_3x3_integer_linear_system(A, b):
    A = A.astype(int)
    b = b.astype(int)
    augmented_matrix = np.column_stack((A, b))
    n = len(augmented_matrix)

    # Perform Gaussian elimination with integer arithmetic
    for i in range(n):
        # Find the pivot row
        max_row = i + np.argmax(np.abs(augmented_matrix[i:, i]))

        # Swap rows if necessary
        if max_row != i:
            augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
            print(f"Swap row {i+1} with row {max_row+1}:\n{augmented_matrix}")

        # Zero out below pivot
        for j in range(i + 1, n):
            lcm_value = lcm(augmented_matrix[j, i], augmented_matrix[i, i])
            factor1 = lcm_value // augmented_matrix[j, i]
            factor2 = lcm_value // augmented_matrix[i, i]
            augmented_matrix[j] = (
                factor1 * augmented_matrix[j] - factor2 * augmented_matrix[i]
            )
            print(
                f"Row {j+1} = {factor1} * Row {j+1} - {factor2} * Row {i+1}:\n{augmented_matrix}"
            )

    # Perform back-substitution
    x = np.zeros(n, dtype=int)
    for i in range(n - 1, -1, -1):
        x[i] = (
            augmented_matrix[i, -1]
            - np.sum(augmented_matrix[i, i + 1 : n] * x[i + 1 : n])
        ) // augmented_matrix[i, i]

    return x


# Example usage
A = np.array([[1, 1, 1], [1, 5, 10], [0, 0, 0]])

b = np.array([32, 100, 0])


x = solve_3x3_integer_linear_system(A, b)
print(f"\nSolution: {x}")
