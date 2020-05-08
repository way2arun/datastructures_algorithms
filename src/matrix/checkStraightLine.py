"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
   Hide Hint #1
If there're only 2 points, return true.
   Hide Hint #2
Check if all other points lie on the line defined by the first 2 points.
   Hide Hint #3
Use cross product to check collinearity.

https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        # 64 ms
        # Solution 1
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x, y in coordinates:
            if (x2 - x1) * (y - y2) != (x - x2) * (y2 - y1):
                return False
        return True
        """

        # Solution 2
        # 40 ms
        n = len(coordinates)
        if n < 2:
            return False
        if n == 2:
            return True
        xs = [coordinates[i][0] for i in range(n)]

        if max(xs) == min(xs):
            return True

        i = 1
        while coordinates[i][0] == coordinates[1][0]:
            i += 1

        k = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
        b = coordinates[0][1] - k * coordinates[0][0]

        for i in range(2, n):
            if abs(coordinates[i][1] - k * coordinates[i][0] - b) > 0.0001:
                return False

        return True


# Main Call
solution = Solution()
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(solution.checkStraightLine(coordinates))
coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
print(solution.checkStraightLine(coordinates))
