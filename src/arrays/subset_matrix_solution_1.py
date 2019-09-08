"""
Given 2 matrices. One big matrix(say, A) and one small matrix(say, B). You need to find out whether the smaller
one matrix is the sub-matrix(part) of bigger matrix. Input:

Matrix A= 1   2   3   4

5   6   7   8

9  10 11 12

13 14 15 16

Matrix B = 6   7    8

10 11 12

14 15 16

Output: YES


"""

# Time Complexity :- O(sr*sc) * O(br*bc)
# Space Complexity - O(1)


def isSubset(big_matrix, small_matrix):
    small_matrix_col_count = 0
    for srow in range(len(small_matrix)):
        for scol in range(len(small_matrix[0])):
            for brow in range(len(big_matrix)):
                for bcol in range(len(big_matrix[0])):
                    if big_matrix[brow][bcol] == small_matrix[srow][scol]:
                        small_matrix_col_count += 1

    print(small_matrix_col_count)
    if small_matrix_col_count >= len(small_matrix[0]):
        print("The small matrix is a subset of the bigger one.")
    else:
        print("The small matrix is not a subset of the bigger one.")


# Driver code
big_matrix = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
small_matrix = [[3, 5, 1]]

isSubset(big_matrix, small_matrix)


big_matrix = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
small_matrix = [[3, 5, 1], [1,2,3]]
isSubset(big_matrix, small_matrix)

big_matrix = [[1, 3, 5], [3, 2, 4], [5, 4, 1]]
small_matrix = [[9,8,9], [8,8,8]]
isSubset(big_matrix, small_matrix)
