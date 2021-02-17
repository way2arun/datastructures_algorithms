"""
Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2


Constraints:

n == height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104
   Hide Hint #1
The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.
Area = length of shorter vertical line * distance between lines
We can definitely get the maximum width container as the outermost lines have the maximum distance between them. However, this container might not be the maximum in size as one of the vertical lines of this container could be really short.


   Hide Hint #2
Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. This way we are compromising on the width but we are looking forward to a longer length container.

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Solution 1 - 156 ms
        """
        # length of input array
        size = len(height)

        # two pointers, left init as 0, right init as size-1
        left, right = 0, size - 1

        # maximal width between leftmost stick and rightmost stick
        max_width = size - 1

        # area also known as the amount of water
        area = 0

        # trade-off between width and height
        # scan each possible width and compute maxximal area
        for width in range(max_width, 0, -1):

            if height[left] < height[right]:
                # the height of lefthand side is shorter
                area = max(area, width * height[left])

                # update left index to righthand side
                left += 1

            else:
                # the height of righthand side is shorter
                area = max(area, width * height[right])

                # update right index to lefthand side
                right -= 1

        return area
        """
        # Solution 2 -132 ms
        maximum = 0
        inner_node = 0
        outer_node = len(height) - 1

        while outer_node > inner_node:
            if height[inner_node] >= height[outer_node]:
                volume = (outer_node - inner_node) * height[outer_node]
                outer_node -= 1
            else:
                volume = (outer_node - inner_node) * height[inner_node]
                inner_node += 1
            if maximum < volume:
                maximum = volume
        return maximum


# Main Call
height = [4, 3, 2, 1, 4]
solution = Solution()
print(solution.maxArea(height))