"""
Number of Steps to Reduce a Number to Zero
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.



Example 1:

Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation:
Step 1) 8 is even; divide by 2 and obtain 4.
Step 2) 4 is even; divide by 2 and obtain 2.
Step 3) 2 is even; divide by 2 and obtain 1.
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12


Constraints:

0 <= num <= 10^6
   Hide Hint #1
Simulate the process to get the final answer.
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Solution 1 - 28 ms
        """
        count = 0
        while num > 1:
            count += [1, 2][num % 2]
            num //= 2
        return [count, count + 1][num]
        """
        # Solution 2 - 12 ms
        step = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
                step += 1
            else:
                num -= 1
                step += 1
        return step


# Main Call
num = 14

solution = Solution()
print(solution.numberOfSteps(num))