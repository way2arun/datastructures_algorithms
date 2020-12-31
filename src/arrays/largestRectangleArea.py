"""
Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Solution 1 - 100 ms
        """
        stack, ans = [], 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] - 1
                ans = max(ans, H * W)
            stack.append(i)
        return ans
        """
        # Solution 2 - 76 ms
        if not heights:
            return 0

        n = len(heights)

        if n == 1:
            return heights[0]

        stack = [(heights[0], 0)]

        max_area = 0

        for i, height in enumerate(heights):
            # print(stack)

            if height < stack[-1][0]:
                while stack and height < stack[-1][0]:
                    height2, i2 = stack.pop()
                    area = height2 * (i - i2)
                    max_area = max(max_area, area)
                stack.append((height, i2))

            if not stack or height > stack[-1][0]:
                stack.append((height, i))

            # for height2, i2 in stack:
            #   area = min(height, height2) * (i - i2 + 1)
            #  max_area = max(max_area, area)

        while stack:
            height, i = stack.pop()
            area = height * (n - i)
            max_area = max(max_area, area)

            # print(area, stack)
            # print("")

        return max_area


# Main Call
heights = [2, 1, 5, 6, 2, 3]
solution = Solution()
print(solution.largestRectangleArea(heights))
