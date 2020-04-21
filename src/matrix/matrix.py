"""
Matrix traversing using Python
"""

def display_matrix(mat):
    row = len(mat)
    print(row)
    col = len(mat[0])
    print(col)
    print(row // 2)
    print(mat)

    # Top Row and col
    for r in range(row):
        for c in range(col):
            print(mat[r][c], end=' ')

    print("Top")
    # Left Side
    for r in range(row):
        for c in range(col):
            print(mat[c][r], end=' ')

    print("Left")

    print("Left 2")
    # Left side, with different indexes jumping
    for r in range(row):
        for c in range(col):
            print(mat[-c][r], end=' ')

    print("Left 3")
    # Left side now with different row index's jumping
    for r in range(row):
        for c in range(col):
            print(mat[-c][-r], end=' ')

    print("Left 4")
    # Left side rows with different rows
    for r in range(row):
        for c in range(col):
            print(mat[c][-r], end=' ')

    print("Bottom")
    # Bottom rows
    for r in range(row):
        for c in range(col):
            print(mat[-r - 1][-c - 1], end=' ')

    print("Right")
    # Right rows
    for r in range(row):
        for c in range(col):
            print(mat[c][-r - 1], end=' ')


mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

display_matrix(mat)

college_years = ['f', 'a', 'c']
print(list(enumerate(college_years, 2019)))
