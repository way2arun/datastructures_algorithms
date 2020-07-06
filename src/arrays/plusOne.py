"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3382/
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Solution 1 - 52
        """
        position = len(digits) - 1
        while position >= 0:
            if digits[position] == 9:
                digits[position] = 0
                position -= 1
            else:
                digits[position] += 1
                return digits
        return [1] + digits
        """
        # Solution 2 - 12 ms
        """
        for i in range(0, len(digits)):
            idx = -1 + (-1 * i)
            val = digits[idx] + 1
            if val < 10:
                digits[idx] = val
                break
            if val == 10:
                digits[idx] = 0
                if i == (len(digits) - 1):
                    digits = [1] + digits[:]

        return digits
        """
        # Solution 3 16 ms
        """
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0 and digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
            else:
                digits[i - 1] += 1
            i -= 1
        return digits
        """
        # Solution 4 20 ms
        num = 1
        for idx, x in enumerate(digits[::-1]):
            num += (x * 10 ** idx)
        return list(str(num))


# Main Call
solution = Solution()
digits = [1, 2, 3]
print(solution.plusOne(digits))
