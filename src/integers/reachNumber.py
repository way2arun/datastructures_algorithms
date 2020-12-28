"""
Reach a Number
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        # Solution  1-  104 ms
        """
        target = abs(target)
        total = n = 0
        while True:
            if total < target or (target - total) % 2 == 1:
                n += 1
                total += n
            else:
                return n
        """
        # Solution 2 - 12 ms
        target = ((target > 0) - (target < 0)) * target

        n = int((2 * target) ** 0.5)

        while (n * (n + 1) / 2) < target:
            n += 1

        if target % 2 == 0:
            while (n * (n + 1) / 2) % 2 != 0:
                n += 1
        elif target % 2 != 0:
            while (n * (n + 1) / 2) % 2 == 0:
                n += 1

        return n


# Main Call
solution = Solution()
target = 3
print(solution.reachNumber(target))
