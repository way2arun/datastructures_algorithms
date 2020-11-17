"""
Mirror Reflection
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:

1 <= p <= 1000
0 <= q <= p
"""
import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Solution 1 - 20 ms
        """
        k = 1
        while k * q % p: k += 1
        return 2 if k % 2 == 0 else (k * q // p) % 2
        """
        # Solution 2 - 16 ms
        x = p // math.gcd(p, q)
        y = q // math.gcd(p, q)

        if x % 2 == 1 and y % 2 == 1:
            return 1
        elif x % 2 == 0 and y % 2 == 1:
            return 2
        else:
            return 0


# Main Call
p = 2
q = 1
solution = Solution()
print(solution.mirrorReflection(p, q))
