"""
Add Digits
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3402/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

   Hide Hint #1
A naive implementation of the above process is trivial. Could you come up with other methods?
   Hide Hint #2
What are all the possible results?
   Hide Hint #3
How do they occur, periodically or randomly?
   Hide Hint #4
You may find this Wikipedia article useful.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        # Solution - 1 28 ms
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
        """

        # Solution 2 - 8 ms

        if num in range(0, 10):
            return num
        if num % 9 == 0:
            return 9
        return num % 9

        """
        # Solution 3 - 12 ms
        return 1 + (num - 1) % 9 if num else 0
        """


# Main Call
num = 38
solution = Solution()
print(solution.addDigits(num))
