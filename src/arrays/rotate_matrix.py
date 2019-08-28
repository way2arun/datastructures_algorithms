"""Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. """

# Time Complexity - O(n^2)
# Space Complexity - O(x+y)  


def rotate_90_degrees(matrix):
    # Get the matrix length
    matrix_length = len(matrix)

    for x in range(matrix_length // 2):
        start = x
        end = matrix_length - x - 1
        for y in range(start, end):
            # Copy the top
            top = matrix[x][y]

            # Top = Left [Left --> Top ]
            matrix[x][y] = matrix[-y - 1][x]

            # Left = Bottom [ Bottom --> Left ]
            matrix[-y - 1][x] = matrix[-x - 1][-y - 1]

            # Bottom = Right [ right -> bottom ]
            matrix[-x - 1][-y - 1] = matrix[y][- x - 1]

            # right = top [ top -> right ]
            matrix[y][- x - 1] = top

    # Print the output
    print(matrix)


# Driver Call
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

rotate_90_degrees(mat)
