"""
Contains Duplicate III
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3446/
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
   Hide Hint #1
Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
   Hide Hint #2
Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.


"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Solution 1 - 52 ms
        """
        if len(nums) == 0:
            return False
        if k == 0:
            return False
        if t == 0 and len(set(nums)) == len(nums):
            return False

        if len(nums) < k:
            nums.sort()  # O(klogk)
            s = nums
            m = [abs(s[i + 1] - s[i]) for i in range(len(s) - 1)]

            if len(m) > 0:
                if min(m) <= t:
                    return True
                else:
                    return False

        s = []
        for i in range(0, len(nums)):

            if i <= k:

                # find the correct position and insert nums[i]

                key = nums[i]
                start = 0
                end = len(s) - 1
                found = -1

                while start <= end:
                    mid = (start + end) // 2
                    if key <= s[mid]:
                        if key == s[mid]:
                            found = mid
                        end = mid - 1
                    else:
                        start = mid + 1
                if found == -1:
                    found = start
                s.insert(found, key)

            elif i > k:

                # remove the element nums[i-k-1]
                s.remove(nums[i - k - 1])
                key = nums[i]

                # find the correct position and insert nums[i]
                start = 0
                end = len(s) - 1
                found = -1

                while start <= end:
                    mid = (start + end) // 2
                    if key <= s[mid]:
                        if key == s[mid]:
                            found = mid
                        end = mid - 1
                    else:
                        start = mid + 1
                if found == -1:
                    found = start

                s.insert(found, key)

            # find absolute difference of adjacent elements in sorted array of max length k
            diff = [abs(s[i + 1] - s[i]) for i in range(len(s) - 1)]

            if len(diff) > 0:
                if min(diff) <= t:
                    return True
        return False
        """
        # Solution 2 - 48 ms
        """
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, num in enumerate(nums):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(num - nums[j]) <= t:
                    return True

        return False
        """
        # Solution 3 - 44 ms
        """
        size = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, cur_val in enumerate(nums):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(cur_val - nums[j]) <= t:
                    return True

        return False
        """
        # Solution 4 - 40 ms
        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for i, n in enumerate(nums):
            buck = n // width
            if buck in buckets:
                return True
            buckets[buck] = n
            if buck + 1 in buckets and (buckets[buck + 1] - n) <= t:
                return True
            if buck - 1 in buckets and (n - buckets[buck - 1]) <= t:
                return True
            if i >= k:
                del buckets[nums[i - k] // width]
        return False


# Main Solution
nums = [1, 2, 3, 1]
k = 3
t = 0
solution = Solution()
print(solution.containsNearbyAlmostDuplicate(nums, k, t))
