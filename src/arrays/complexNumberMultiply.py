"""
Complex Number Multiplication
A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.



Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.


Constraints:

num1 and num2 are valid complex numbers.
"""


class Solution:
    # Solution 1 - 32 ms
    """
    def solve(self, num):
        f1 = num.find("+", 0, len(num))
        return int(num[0:f1]), int(num[f1 + 1:len(num) - 1])
    """

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        a, b = self.solve(num1)  # Getting the values for first pair
        x, y = self.solve(num2)  # Getting the values for second pair
        return str(x * a - b * y) + "+" + str(a * y + b * x) + "i"
        """
        # Solution 2 - 16 ms
        a, b = num1.split('+'), num2.split('+')
        if len(a) == 2:
            a[1] = a[1].split('i')[0]
        if len(b) == 2:
            b[1] = b[1].split('i')[0]
        real = (int(a[0]) * int(b[0])) - (int(a[1]) * int(b[1]))
        img = (int(a[0]) * int(b[1])) + (int(a[1]) * int(b[0]))
        return str(real) + '+' + str(img) + 'i'


# Main Call
solution = Solution()
num1 = "1+1i"
num2 = "1+1i"
print(solution.complexNumberMultiply(num1, num2))
