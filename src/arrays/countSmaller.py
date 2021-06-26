"""
Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Solution 1 - 2112 ms
        """
        n = len(nums)
        ans = [0] * n
        sortedList = SortedList()
        for i in range(n - 1, -1, -1):
            index = sortedList.bisect_left(nums[i])
            ans[i] = index
            sortedList.add(nums[i])
        return ans
        """

        # Solution 2 - 1908 ms
        # implement Binary Index Tree
        def update(index, value, tree, size):
            index += 1  # index in BIT is 1 more than the original index
            while index < size:
                tree[index] += value
                index += index & -index

        def query(index, tree):
            # return sum of [0, index)
            result = 0
            while index >= 1:
                result += tree[index]
                index -= index & -index
            return result

        offset = 10 ** 4  # offset negative to non-negative
        size = (2 * 10 ** 4) + 1 + 1  # total possible values in nums plus one dummy
        tree = [0] * size

        result = []
        for num in reversed(nums):
            smaller_count = query(num + offset, tree)

            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)


# Main Call
nums = [5, 2, 6, 1]
solution = Solution()
result = solution.countSmaller(nums)
for r in result:
    print(r)
print(result)
