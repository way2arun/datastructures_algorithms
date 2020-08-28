"""
Implement Rand10() Using Rand7()
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().



Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]


Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.


Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
from random import randint


class Solution:
    def rand7(self):
        return randint(1, 7)

    s = 0

    def rand10(self):
        """
        :rtype: int
        """
        # Solution 1 - 356 ms
        """
        val = self.rand7() - 1
        max_val = 6

        while val >= ((max_val // 10) * 10):
            val = val % 10 * 7 + self.rand7() - 1  # This is where we draw only one random number at each step
            max_val = max_val % 10 * 7 + 6  # This is maximum possible value

        return (val % 10) + 1
        """
        # Solution 2 - 176 ms
        # Wrong way of implementing
        # return randint(1, 10)

        # Solution 3 - 220 ms
        self.s += 7
        return 1 + ((self.rand7() + self.s) % 10)


# Main Call
solution = Solution()
print(solution.rand10())
