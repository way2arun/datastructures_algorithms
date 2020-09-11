"""
Maximum Product Subarray
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Solution 1 - 72 ms
        """
        if nums:
            dp = [(0, 0) for _ in nums]  # max, min at the current index
            dp[0] = nums[0], nums[0]
            maximum = dp[0][0]
            # could have just kept track of the previous max/min to optimize space complexity
            for i in range(1, len(nums)):
                # maximum at current index is either (current * maximum at index i-1)
                # or (current * minimum at index i-1) [in case both values are negative, which makes a positive number]
                # or current
                # the minimum follows a very similar logic
                dp[i] = max(max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]), nums[i]), \
                        min(min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]), nums[i])
                # global max
                maximum = max(maximum, dp[i][0])  # compare with maximum at current index
            return maximum
            """
        # Solution 2 - 36 ms
        """
        max_num = min_num = 1
        max_product = float('-inf')
        for num in nums:
            num1 = max_num * num
            num2 = min_num * num
            max_num = max(num, num1, num2)
            min_num = min(num, num1, num2)
            max_product = max(max_product, max_num)
        return max_product
        """

        # Solution 3 32 ms

        if len(nums) == 1:
            return nums[0]
        if 0 in nums:
            nums = self.splitByZero(nums)
            products = []

            for arr in nums:
                products.append(self.maxProductNoZeros(arr))

            products.append(0)
            print(products)
            return max(products)
        else:
            return self.maxProductNoZeros(nums)


    def splitByZero(self, nums):
        retArr = []  # 2d array
        row = []
        for num in nums:
            if num == 0:
                if len(row) > 0:
                    retArr.append(row)
                    row = []
            else:
                row.append(num)
        if len(row) > 0:
            retArr.append(row)
        return retArr

    def maxProductNoZeros(self, nums):
        if (len(nums) == 1):
            return nums[0]

        countNeg = 0
        for num in nums:
            if num < 0:
                countNeg += 1

        if (countNeg % 2) == 0:
            # include whole array
            prod = 1
            for num in nums:
                prod *= num
            return prod

        # odd number of negatives in array - find whether we should eliminate the last or the first
        elimFirstProd = 1
        i = 0
        while nums[i] > 0 and i < len(nums):
            i += 1
        while i < len(nums) - 1:
            i += 1
            elimFirstProd *= nums[i]

        elimLastProd = 1
        i = len(nums) - 1
        while (nums[i] > 0) and i >= 0:
            i -= 1
        while i > 0:
            i -= 1
            elimLastProd *= nums[i]

        return max(elimFirstProd, elimLastProd)


# Main Call
nums = [2,3,-2,4]
solution = Solution()
print(solution.maxProduct(nums))
