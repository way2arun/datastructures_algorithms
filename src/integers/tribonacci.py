"""
N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
   Hide Hint #1
Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
   Hide Hint #2
Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].
"""


class Solution:
    mem = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        # Solution 1 - 24 ms
        """
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c

        return c
        """
        # Solution 2 - 12 ms
        if n in self.mem:
            return self.mem[n]
        self.mem[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.mem[n]


# Main Call
n = 25
solution = Solution()
print(solution.tribonacci(n))
