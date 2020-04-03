"""
Leet Code Challenge

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""


class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        length = len(nums)
        current_sum = 0

        for num in nums:
            current_sum += num
            if num > current_sum:
                current_sum = num  # this starts the new subarray
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
        # value = self.maximum_sub_array(nums, 0, len(nums) - 1)
        #value = self.maximum_sub_array_sum(nums, 0, len(nums) - 1)
        #return value

    """
    def maximum_sub_array(self, arr, start, end):
        maximumStartSum = 0
        maximumEndSum = 0
        startSum = 0
        endSum = 0

        middle = (start + end) // 2

        if start == end:
            if arr[start] > 0:
                return arr[start]
            else:
                return 0

        maxLeftSum = self.maximum_sub_array(arr, start, middle)
        maxRightSum = self.maximum_sub_array(arr, middle + 1, end)

        for i in range(middle, start - 1, -1):
            startSum = startSum + arr[i]
            if startSum > maximumStartSum:
                maximumStartSum = startSum
        for i in range(middle + 1, end + 1):
            endSum = endSum + arr[i]
            if endSum > maximumEndSum:
                maximumEndSum = endSum

        return max(maximumStartSum + maximumEndSum, maxRightSum, maxLeftSum)
    """

    # Returns sum of maxium sum subarray in aa[l..h]
    def maximum_sub_array_sum(self, arr, start, end):

        # Base Case: Only one element
        if start == end:
            return arr[start]

            # Find middle point
        middle = (start + end) // 2

        # Return maximum of following three possible cases
        # a) Maximum subarray sum in left half
        # b) Maximum subarray sum in right half
        # c) Maximum subarray sum such that the
        #     subarray crosses the midpoint
        return max(self.maximum_sub_array_sum(arr, start, middle),
                   self.maximum_sub_array_sum(arr, middle + 1, end),
                   self.maximum_crossing_sum(arr, start, middle, end))

    def maximum_crossing_sum(self, arr, start, middle, end):

        # Include elements on left of mid.
        sum = 0
        left_sum = -10000

        for i in range(middle, start - 1, -1):
            sum = sum + arr[i]

            if sum > left_sum:
                left_sum = sum

        # Include elements on right of mid
        sum = 0
        right_sum = -1000
        for i in range(middle + 1, end + 1):
            sum = sum + arr[i]

            if sum > right_sum:
                right_sum = sum

        # Return sum of elements on left and right of mid
        return left_sum + right_sum



# Main Call
solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = solution.maxSubArray(nums)
print(result)
