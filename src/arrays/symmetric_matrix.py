"""
Check a matrix is symmetric or not

"""


def isSymmetric(matrix , row):
    for r in range(row):
        for c in range(row):
            if matrix[r][c] != matrix[c][r]:
                return False
    return True


# Driver code
matrix = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
if isSymmetric(matrix, 3):
    print("Symmetric Matrix")
else:
    print("Not a Symmetric Matrix")
