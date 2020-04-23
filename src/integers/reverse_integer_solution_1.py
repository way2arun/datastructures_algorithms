"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


# Time Complexity - O(n)
# Space Complexity - O(1)


def reverse_integer(number):

    sign = 1
    res = 0
    if number < 0:
        sign = -1
        number = -number

    while number != 0:
        res = (res * 10) + number % 10
        number = number // 10

    if (res > 2 ** 31 - 1) or (res < -2 ** 31):
        return 0

    return sign * res


# Driver Call
print(reverse_integer(12501))
