"""
Sequential Digits
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
   Hide Hint #1
Generate all numbers with sequential digits and check if they are in the given range.
   Hide Hint #2
Fix the starting digit then do a recursion that tries to append all valid digits.

"""
from typing import List
from math import log10


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Solution 1 - 32 ms
        """
        s = '123456789'
        ans = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                st = int(s[i:j + 1])
                if low <= st <= high:
                    ans.append(st)
        ans.sort()
        return ans
        """
        # Solution 2 - 12 ms
        low_digits = int(log10(low)) + 1
        high_digits = int(log10(high)) + 1
        all_digits = [str(i) for i in range(10)]
        res = []

        for digits in range(low_digits, high_digits + 1):
            if digits > low_digits:
                tmp = [int(''.join(all_digits[i:i + digits])) for i in range(1, 11 - digits)]
                res.extend([*filter(lambda x: low <= x <= high, tmp)])
            else:  # digits == low_digits
                tmp = [int(''.join(all_digits[i:i + digits])) for i in range(11 - digits)]
                res.extend([*filter(lambda x: low <= x <= high, tmp)])

        return res


# Main Call
solution = Solution()
low = 100
high = 300
print(solution.sequentialDigits(low, high))
low = 1000
high = 13000
print(solution.sequentialDigits(low, high))
low = 1000
