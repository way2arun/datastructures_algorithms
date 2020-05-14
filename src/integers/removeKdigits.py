"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Solution 1 - 32ms
        """
        stack = []
        for number in num:
            # Pop element from stack if the current element is smaller than last added element in stack
            while k and stack and stack[-1] > number:
                stack.pop()
                k -= 1
            stack.append(number)

        # If still k elements left to remove, then remove them from the stack.
        while k > 0:
            stack.pop()
            k -= 1
        # Remove leading zeros
        output = "".join(stack).lstrip("0")

        if output:
            return output
        else:
            return "0"
        """
        # Solution 2 20 ms
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        stack = stack[:-k] if k else stack
        # print(stack)
        return "".join(stack).lstrip('0') or "0"


# Main Call
solution = Solution()
num = "1432219"
k = 3
print(solution.removeKdigits(num, k))