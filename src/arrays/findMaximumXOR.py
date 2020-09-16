"""
Maximum XOR of Two Numbers in an Array
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3462/
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

"""
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Solution 1 - 136 ms
        """
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            found = {num & mask for num in nums}
            start = ans | 1 << i
            if any(start ^ pref in found for pref in found):
                ans = start
        return ans
        """
        # Solution 2 - 80 ms
        res = 0
        for i in range(30, -1, -1):
            mySet = set()
            res <<= 1
            res += 1
            isValid = False
            for num in nums:
                if (num >> i) in mySet:
                    isValid = True
                    break
                mySet.add((num >> i) ^ res)
            if not isValid:
                res -= 1
        return res


# Main Call
nums = [3, 10, 5, 25, 2, 8]
solution = Solution()
print(solution.findMaximumXOR(nums))
