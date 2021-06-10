"""
Jump Game VI
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:

 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
   Hide Hint #1
Let dp[i] be "the maximum score to reach the end starting at index i". The answer for dp[i] is nums[i] + min{dp[i+j]} for 1 <= j <= k. That gives an O(n*k) solution.
   Hide Hint #2
Instead of checking every j for every i, keep track of the smallest dp[i] values in a heap and calculate dp[i] from right to left. When the smallest value in the heap is out of bounds of the current index, remove it and keep checking.


"""
from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Solution 1 - 964 ms
        """
        n = len(nums)
        dq = deque(
            [0])  # store index of `nums` elements, elements is in decreasing order, the front is the maximum element.
        for i in range(1, n):
            # nums[i] = max(nums[i-k], nums[i-k+1],.., nums[i-1]) + nums[i] = nums[dq.front()] + nums[i]
            nums[i] = nums[dq[0]] + nums[i]

            # Add a nums[i] to the deq
            while dq and nums[dq[-1]] <= nums[i]: dq.pop()  # Eliminate elements less or equal to nums[i]
            dq.append(i)

            # Remove if the last element is out of window size k
            if i - dq[0] >= k: dq.popleft()

        return nums[n - 1]
        """
        # Solution 2 - 864 ms
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        max_sum_pointer = 0
        for i in range(1, n):
            if max_sum_pointer >= i - k:
                if max_sum < dp[i - 1] and i > 0:
                    max_sum = dp[i - 1]
                    max_sum_pointer = i - 1
            else:
                if i - k > 0:
                    max_sum = dp[i - k]
                    max_sum_pointer = i - k
                    for p in range(i - k, i):
                        if max_sum <= dp[p]:
                            max_sum = dp[p]
                            max_sum_pointer = p

            dp[i] = max_sum + nums[i]

        dp[-1] = max_sum + nums[-1]
        return dp[-1]


# Main Call
nums = [1, -1, -2, 4, -7, 3]
k = 2
solution = Solution()
print(solution.maxResult(nums, k))
