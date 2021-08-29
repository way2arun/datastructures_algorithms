"""
Patching Array
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.



Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
"""
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Solution 1 - 64 ms
        """
        reach, ans, idx = 0, 0, 0

        while reach < n:
            if idx < len(nums) and nums[idx] <= reach + 1:
                reach += nums[idx]
                idx += 1
            else:
                ans += 1
                reach = 2 * reach + 1

        return ans
        """
        # Solution 2 - 48 ms
        miss = 1
        count = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                count += 1
        return count


# Main Call
nums = [1, 5, 10]
n = 20
solution = Solution()
print(solution.minPatches(nums, n))
