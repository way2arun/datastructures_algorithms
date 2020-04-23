"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

# Time Complexity - O(n)
# Space Complexity - O(1)


def reverse_integer(x):
    reverse_x = 0
    check_zero = 0
    neg = 1

    if x < 0:
        neg = -1
        x = -x

    while x != 0:
        mod = x % 10
        if 0 != check_zero:
            reverse_x = reverse_x * 100 + mod
            check_zero = 0
        elif mod != 0:
            reverse_x = reverse_x * 10 + mod
        else:
            check_zero += 1
        x = x // 10

    if (reverse_x > 2 ** 31 - 1) or (reverse_x < -2 ** 31):
        return 0

    return neg * reverse_x


# Driver Call
print(reverse_integer(125))
