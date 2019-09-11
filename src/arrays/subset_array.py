"""
This is to find an array is a subset of an another array.
"""


def isArraySubset(array1, array2, m, n):
    i = 0
    j = 0
    for i in range(n):
        for j in range(m):
            if array2[i] == array1[j]:
                break
        # If the above inner loop was
        # not broken at all then array2[i]
        # is not present in array1[]
        if j == m:
            return 0

    # If we reach here then all
    # elements of array2[] are present
    # in array1[]
    return 1


# Driver code
if __name__ == "__main__":
    array1 = [11, 1, 13, 21, 3, 7]
    array2 = [11, 3, 7, 1]
    m = len(array1)
    n = len(array2)
    if isArraySubset(array1, array2, m, n):
        print("array2 is subset of array1 ")
    else:
        print("array2  is not a subset of array1")
