"""
Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 - 44 ms
        """
        def dfs(counter, built):
            if counter == len(nums):
                result.append(built)
                return

            stop = built.index(nums[counter]) if nums[counter] in built else counter

            for i in range(stop + 1):
                dfs(counter + 1, built[:i] + [nums[counter]] + built[i:])

        result = []
        dfs(0, [])
        return result
        """
        # Solution 2 - 32 ms
        res = [[]]
        for x in nums:
            # only insert up to the first occurrence rest.index(head)
            # because any slot after the first occurrence can be thought as
            # the duplicate of the first occurrence as the inserted element
            # and the slot being the existing one.
            res = [path[:i] + [x] + path[i:] for path in res for i in range((path + [x]).index(x) + 1)]

        return res




# Main Call
nums = [1, 1, 2]
solution = Solution()
print(solution.permuteUnique(nums))
