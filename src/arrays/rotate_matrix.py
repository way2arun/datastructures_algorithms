"""Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. """

# Time Complexity - O(n^2)
# Space Complexity - O(x+y)  


def rotate_90_degrees(matrix):
    # Get the matrix length
    matrix_length = len(matrix)

    for row in range(matrix_length // 2):
        start = row
        end = matrix_length - row - 1
        for col in range(start, end):
            # Copy the top
            top = matrix[row][col]

            # Top = Left [Left --> Top ]
            matrix[row][col] = matrix[-col - 1][row]

            # Left = Bottom [ Bottom --> Left ]
            matrix[-col - 1][row] = matrix[-row - 1][-col - 1]

            # Bottom = Right [ right -> bottom ]
            matrix[-row - 1][-col - 1] = matrix[col][- row - 1]

            # right = top [ top -> right ]
            matrix[col][- row - 1] = top

    # Print the output
    print(matrix)


# Driver Call
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

rotate_90_degrees(mat)
