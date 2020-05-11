"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
   Hide Hint #1
Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # Solution 2 60 ms
        if not image or len(image) == 0: return 0
        m = len(image)
        n = len(image[0])
        neighs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        # [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(row, col, oldColor):
            q = [[row, col]]
            while q:
                x, y = q.pop(0)
                for neigh in neighs:
                    x = row + neigh[0]
                    y = col + neigh[1]
                    if m > x >= 0 and n > y >= 0 and image[x][y] == oldColor:
                        image[x][y] = newColor
                        bfs(x, y, oldColor)

        if image[sr][sc] == newColor:
            return image
        else:
            oldColor = image[sr][sc]
            image[sr][sc] = newColor
            bfs(sr, sc, oldColor)
            return image

        # Solution 1 80 ms
        """
        self.newColor = newColor
        self.rows = len(image)
        self.cols = len(image[0])
        if newColor != image[sr][sc]:
            self.fill_color(image, sr, sc, image[sr][sc])
        return image
        """

    """
    def fill_color(self, image, x, y, oldColor):
        if 0 <= x < self.rows and 0 <= y < self.cols and image[x][y] == oldColor:
            image[x][y] = self.newColor
            self.fill_color(image, x + 1, y, oldColor)
            self.fill_color(image, x, y - 1, oldColor)
            self.fill_color(image, x - 1, y, oldColor)
            self.fill_color(image, x, y + 1, oldColor)
    """





# Main Call
solution = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
response = solution.floodFill(image, sr, sc, newColor)
print(newColor)
