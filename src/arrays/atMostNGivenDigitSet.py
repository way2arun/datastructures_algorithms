"""
Numbers At Most N Given Digit Set
Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.



Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1


Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109
"""
import bisect
import math
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Solution 1 - 32 ms
        """
        ans = 0
        n_str = str(n)

        # number of positive integers with lengths smaller than the length of n
        for length in range(1, len(n_str)):
            ans += len(digits) ** length

        # for intergers with the same length as l, we do the following: iterate i from 0 -> length(n) - 1 for each
        # digit d in digits: if d is smaller than n[i], the rest of n (i.e. n[i+1:]) can be constructed by using
        # every combination in digits if d is greater than n[i], there is no way to construct the rest of n if there
        # is a case of d = n[i], we continue with the next iteration of i, otherwise we can stop the program.
        equal_digit = True  # if d == n[i]
        for i in range(len(n_str)):
            if not equal_digit:
                return ans
            equal_digit = False
            for d in digits:
                if d < n_str[i]:
                    ans += len(digits) ** (len(n_str) - i - 1)
                if d == n_str[i]:
                    equal_digit = True
        return ans + equal_digit
        """
        # Solution 2 - 16 ms
        ORD0 = ord('0')
        digits = sorted([ord(_) - ORD0 for _ in digits])
        s = len(digits)
        l = int(math.log(n) / math.log(10))
        t = 10 ** l
        leading = n // t
        if leading > 9:
            t *= 10
            l += 1
            leading = n // t

        def getnum():
            leading0 = leading
            n0 = n
            l0 = l
            t0 = t
            m9 = digits[-1] * (10 ** (l0 + 1) - 1) // 9
            m0 = m9 // digits[-1] * digits[0]
            scope = locals()
            if n0 >= m9:
                for i in range(l0 + 1):
                    yield s - 1
                return
            if n0 < m0:
                for i in range(l0):
                    yield s - 1
                return
            if n0 == m0:
                for i in range(l0 + 1):
                    yield 0
                return
            while n0:
                x = bisect.bisect_left(digits, leading0)
                scope = locals()
                if x == s:
                    for i in range(l0 + 1):
                        yield s - 1
                    return
                if leading0 == digits[x]:
                    candidate = x
                else:
                    candidate = x - 1
                remain = n0 - digits[candidate] * (10 ** l0)
                l0 -= 1
                m9 //= 10
                m0 //= 10
                scope = locals()
                if remain < m0 and t0 > 1:
                    print()
                    candidate -= 1
                    remain = n0 - digits[candidate] * (10 ** l0)
                scope = locals()
                yield candidate

                if t0 == 1:
                    break
                t0 //= 10
                leading0 = remain // t0
                n0 = remain
                # m0 //= 10

        nums = list(getnum())
        l = len(nums)
        if s == 1:
            return l
        ans = (s ** l - s) // (s - 1)
        t = s ** l
        for i in nums:
            t //= s
            ans += i * t
        ans += 1
        return ans



# Main Call
digits = ["1", "4", "9"]
n = 1000000000

solution = Solution()
print(solution.atMostNGivenDigitSet(digits, n))