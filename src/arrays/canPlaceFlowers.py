"""
Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Solution - 1 - 176 ms
        """
        l = [0] + flowerbed + [0]
        for i in range(1, len(l) - 1):
            if sum(l[i - 1:i + 2]) == 0:
                l[i] = 1
                n -= 1
        return n <= 0
        """
        # Solution 2 - 136 ms
        num_flower = sum(flowerbed)
        bed_len = len(flowerbed)
        if (num_flower + n) > (bed_len + 1) // 2:
            return False
        else:
            count = 0
            for i in range(bed_len):
                if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                        i == bed_len - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    count += 1
                if count >= n:
                    return True
            return count >= n


# Main Call
solution = Solution()
flowerbed = [1, 0, 0, 0, 1]
n = 1

solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))
