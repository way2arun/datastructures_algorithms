"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        # Solution 1 - 32 ms
        if num < 2:
            return True
        middle = num // 2
        stack = set([middle])
        print(stack)
        while middle * middle != num:
            middle = (middle + (num // middle)) // 2
            print(middle)
            print(stack)
            if middle in stack:
                return False
            stack.add(middle)
        return True
        """
        # Solution 2 - 12 ms
        if num < 2:
            return True
        start = 1
        end = num // 2
        while start <= end:
            middle = (start + end) // 2
            get_square = middle * middle
            if get_square == num:
                return True
            elif get_square > num:
                end = middle - 1
            else:
                start = middle + 1
        return False


# Main Call
solution = Solution()
num = 16
print(solution.isPerfectSquare(num))
num = 14
print(solution.isPerfectSquare(num))
