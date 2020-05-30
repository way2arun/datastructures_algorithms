"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

"""
import math
from heapq import heappushpop, heappush
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Solution 1 - 1340 ms
        """
        if K >= len(points):
            return points
        result = []
        for x_axis, y_axis in points:
            dis = math.sqrt(x_axis ** 2 + y_axis ** 2)
            if len(result) == K:
                heappushpop(result, [-dis, x_axis, y_axis])
            else:
                heappush(result, [-dis, x_axis, y_axis])
        return [[x, y] for _, x, y in result]
        """
        # Solution 2 - 608 ms
        points.sort(key=lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:K]


# Main Call
points = [[1, 3], [-2, 2]]
K = 1
solution = Solution()
print(solution.kClosest(points, K))
