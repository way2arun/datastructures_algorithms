"""
Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
from functools import reduce
from operator import mul
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Solution 1 - 172 ms
        """
        n = len(nums)
        A = -sum(nums) + n * (n + 1) // 2
        B = -sum(i * i for i in nums) + n * (n + 1) * (2 * n + 1) // 6
        return [(B - A * A) // 2 // A, (B + A * A) // 2 // A]
        """

        # Solution 2 - 194 ms
        expectedSum = sum(range(1, len(nums) + 1))
        realSum = sum(nums)
        sumDiff = realSum - expectedSum

        expectedProd = reduce(mul, range(1, len(nums) + 1))
        realProd = reduce(mul, nums)
        prodDivision = realProd / expectedProd

        # Math:
        # sumDiff == duplicate - missing
        # prodDivision == duplicate / missing
        # duplicate == prodQuot * missing
        # sumDiff == prodQuot * missing - missing
        # sumDiff == missing * (prodQuot - 1)
        # sumDiff / (prodQuot - 1) == missing
        missing = round(sumDiff / (prodDivision - 1))
        duplicate = sumDiff + missing

        return (duplicate, missing)


# Main Call
nums = [1, 2, 2, 4]
solution = Solution()
print(solution.findErrorNums(nums))