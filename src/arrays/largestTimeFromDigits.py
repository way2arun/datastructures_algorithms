"""
Largest Time for Given Digits
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
"""
import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # Solution 1 - 32 ms
        """
        # help function to turn number to clock-format:
        def to_clock(num):
            right = str(num % 100)
            while len(right) < 2: right = '0' + right
            num //= 100
            left = str(num)
            while len(left) < 2: left = '0' + left
            return left + ':' + right

        # get all permutations of number list
        per = list(itertools.permutations(A))
        nums = [int(''.join(map(str, per[i]))) for i in range(len(per))]

        # find permutations which can be a valid time
        valids = [num for num in nums if num < 2359 and num % 100 < 60]

        if len(valids) == 0:
            return ""

        # use maximum of list
        num = max(valids)
        return to_clock(num)
        """
        # Solution 2 - 16 ms
        def getMaxLessThan(A, upperChar):
            maxChar = -1
            for char in A:
                if (maxChar == -1 and char <= upperChar) or (char >= maxChar and char <= upperChar):
                    maxChar = char
            return maxChar

        solution = ''

        digits = A.copy()
        if 0 in digits:
            h1 = 0
            digits.remove(0)

            h2 = max(digits)
            digits.remove(h2)

            if min(digits) <= 5:
                m1 = getMaxLessThan(digits, 5)
                digits.remove(m1)

                m2 = max(digits)
                digits.remove(m2)

                solution = '{}{}:{}{}'.format(h1, h2, m1, m2)

        digits = A.copy()
        if 1 in digits:
            h1 = 1
            digits.remove(1)

            h2 = max(digits)
            digits.remove(h2)

            if min(digits) <= 5:
                m1 = getMaxLessThan(digits, 5)
                digits.remove(m1)

                m2 = max(digits)
                digits.remove(m2)

                solution = '{}{}:{}{}'.format(h1, h2, m1, m2)

        digits = A.copy()
        if 2 in digits:
            h1 = 2
            digits.remove(2)

            if min(digits) <= 3:
                h2 = getMaxLessThan(digits, 3)
                digits.remove(h2)

                if min(digits) <= 5:
                    m1 = getMaxLessThan(digits, 5)
                    digits.remove(m1)

                    m2 = max(digits)
                    digits.remove(m2)

                    solution = '{}{}:{}{}'.format(h1, h2, m1, m2)

        return solution


# Main Solution
solution = Solution()
A = [1,2,3,4]
print(solution.largestTimeFromDigits(A))
