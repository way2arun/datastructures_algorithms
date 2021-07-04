"""
Count Vowels Permutation
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4
   Hide Hint #1
Use dynamic programming.
   Hide Hint #2
Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
   Hide Hint #3
Deduce the recurrence from the given relations between vowels.

"""
from symbol import power

MOD = 10 ** 9 + 7


def mul(a, b):
    n, m, l = len(a), len(b), len(b[0])
    res = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j] % MOD
                res[i][j] %= MOD
    return res


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def power(a, b):
    res = identity(len(a))
    while b > 0:
        if b % 2 == 1:
            res = mul(res, a)
        a = mul(a, a)
        b //= 2
    return res


m = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0]
]


def entrySum(A):
    tot = 0
    for i in range(5):
        for j in range(5):
            tot += A[i][j]
    return tot % (10 ** 9 + 7)


class Solution:

    def countVowelPermutation(self, n: int) -> int:
        # Solution 1 = 112 ms
        """
        a, e, i, o, u, M = 1, 1, 1, 1, 1, 10 ** 9 + 7
        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % M, (a + i) % M, (e + o) % M, i % M, (i + o) % M

        return (a + e + i + o + u) % M
        """
        # Solution 2 - 60 ms
        """
        a = power(m, n - 1)
        res = 0
        for i in range(5):
            for j in range(5):
                res += a[i][j]
                res %= MOD
        return res
        """

        # Solution 3 - 48 ms
        """
        M = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]]

        def Mpower(m):
            if m == 1:
                return M
            else:
                P, Q = Mpower(m // 2), [[0] * 5 for _ in range(5)]
                for i in range(5):
                    for j in range(5):
                        for k in range(5):
                            Q[i][j] = (Q[i][j] + P[i][k] * P[k][j]) % (10 ** 9 + 7)
                if m % 2 == 0: return Q
                R = [[0] * 5 for _ in range(5)]
                for i in range(5):
                    for j in range(5):
                        for k in range(5):
                            R[i][j] = (R[i][j] + M[i][k] * Q[k][j]) % (10 ** 9 + 7)
                return R

        N = Mpower(n - 1) if n > 1 else [[5]]
        return sum([sum(C) for C in N]) % (10 ** 9 + 7)
        """
        # Solution 4 - 44 ms
        A = [[0, 1, 0, 0, 0, ], [1, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 1], [1, 0, 0, 0, 0]]

        return entrySum(power(A, n - 1))

    # Main Call


solution = Solution()
n = 1
print(solution.countVowelPermutation(n))
