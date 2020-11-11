"""
Valid Square
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True


Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

"""
import math
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Solution 1 - 36 ms
        """
        return self.check(p1, p2, p3, p4) or self.check(p1, p3, p2, p4) or self.check(p1, p4, p2, p3)
        """
        # Solution 2 - 16 ms
        points = [[p1, p2], [p1, p3], [p1, p4], [p2, p3], [p2, p4], [p3, p4]]
        res = []

        for i in points:
            res.append(self.distance(i[0], i[1]))

        h = {}

        for i in res:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        for i in h.values():
            if (i == 2 or i == 4) and len(h) == 2:
                continue
            else:
                return False
        return True

    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    def distance_square(self, p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

    def check(self, p1, p2, p3, p4):
        if p1[0] + p2[0] != p3[0] + p4[0] or p1[1] + p2[1] != p3[1] + p4[1]:
            return False
        if self.distance_square(p1, p2) != self.distance_square(p3, p4) or self.distance_square(p1, p4) != self.distance_square(p2, p4):
            return False
        if p1 == p2:
            return False
        return True


# Main Call
p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]

solution = Solution()
print(solution.validSquare(p1, p2, p3, p4))
