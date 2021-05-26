"""
 Partitioning Into Minimum Number Of Deci-Binary Numbers
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.



Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
Example 2:

Input: n = "82734"
Output: 8
Example 3:

Input: n = "27346209830709182346"
Output: 9


Constraints:

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.
   Hide Hint #1
Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
   Hide Hint #2
If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.
   Hide Hint #3
Thus the answer is equal to the max digit.
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        # Solution 1 - 188 ms
        """
        res = 0
        for x in n:
            if int(x) > res:
                res = int(x)

        return res
        """
        # Solution 2 - 48 ms
        """
        return max(n)
        """

        # Solution 3 - 16 ms

        if '9' in n:
            return 9
        if '8' in n:
            return 8
        if '7' in n:
            return 7
        if '6' in n:
            return 6
        if '5' in n:
            return 5
        if '4' in n:
            return 4
        if '3' in n:
            return 3
        if '2' in n:
            return 2
        if '1' in n:
            return 1


# Main Call
n = "32"
solution = Solution()
print(solution.minPartitions(n))