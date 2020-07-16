"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3392/
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution:
    # Solution 1 - 24 ms
    """
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        if x == 1 or n == 0:
            return 1.0

        power = abs(n)
        power_bank = {}
        res = self.get_power(x, power, power_bank)
        return 1 / res if n < 0 else res

    def get_power(self, x, power, power_bank):
        if power == 1:
            return x
        if power == 2:
            return x * x

        if power_bank.get(power):
            return power_bank[power]

        prev_power = 1
        next_power = 2
        prev_val = x

        while next_power < power:
            prev_val = prev_val * prev_val
            power_bank[next_power] = prev_val
            prev_power = next_power
            next_power *= 2

        power_bank[power] = prev_val * self.get_power(x, power - prev_power, power_bank)
        return power_bank[power]
    """
    # Solution 2 - 8 ms
    """
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
    """

    # Solution 3 - 12 ms
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        temp = self.myPow(x, int(n / 2))

        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x


# Main Call
solution = Solution()
x = 2.00000
n = 10
print(solution.myPow(x, n))
