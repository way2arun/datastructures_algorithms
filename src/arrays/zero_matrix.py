"""
 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""
from typing import List

# Time Complexity :- O(n^2 + n^2) = O(2n^2)
# Space Complexity :- O(n)


def zero_matrix(matrix_input):
    # Checking the Empty Matrix
    if len(matrix_input) == 0 or len(matrix_input[0]) == 0:
        return False

    # Initialize the row and column with False boolean
    row: List[bool] = [False] * len(matrix_input)
    column: List[bool] = [False] * len(matrix_input[0])

    # check if the row or column is 0 , if so add the row and column to initialize True
    for r in range(len(matrix_input)):
        for c in range(len(matrix_input[0])):
            # check the matrix[row][col] == 0
            if matrix_input[r][c] == 0:
                row[r] = True
                column[c] = True

    # Traverse through the matrix and check the row and column and set it 0 if its True
    for r in range(len(matrix_input)):
        for c in range(len(matrix_input[0])):
            if row[r] == True or column[c] == True:
                matrix_input[r][c] = 0

    # Print the matrix
    print(matrix_input)


# Driver Call
mat = [[1, 1, 1],
       [2, 0, 1],
       [3, 0, 1],
       [4, 0, 1]]
print(zero_matrix(mat))
