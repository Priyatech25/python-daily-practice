# DAY 25 - DSA Practice (2D Array / Matrix)

def matrix_operations(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    print("Matrix:")
    for row in matrix:
        print(row)

    # Row-wise sum
    print("\nRow-wise sum:")
    for i in range(rows):
        print(f"Row {i} sum:", sum(matrix[i]))

    # Column-wise sum
    print("\nColumn-wise sum:")
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(f"Column {j} sum:", col_sum)

    # Maximum element
    max_element = matrix[0][0]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]

    print("\nMaximum element:", max_element)


# Testing
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_operations(matrix)