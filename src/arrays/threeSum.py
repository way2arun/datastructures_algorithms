"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3384/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
   Hide Hint #1
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
   Hide Hint #2
For the two-sum problem, if we fix one of the numbers, say
x
, we have to scan the entire array to find the next number
y
which is
value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?
   Hide Hint #3
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

"""
from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 - 1284 ms
        """
        nums_length = len(nums)
        nums.sort()
        result = []

        for i in range(nums_length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, nums_length - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result
        """
        f = {}
        # counter
        for i in nums:
            f[i] = f.get(i, 0) + 1
        n = sorted(f)
        # print(f)
        a = []
        for i, I in enumerate(n):
            if not I:  # I=0
                if f[I] > 2: a.append((0, 0, 0))
            elif f[I] > 1 and -2 * I in f:
                a.append((I, I, -2 * I))
            if I < 0:
                t = -I
                # print(n,t-n[-1],i+1)
                l = bisect_left(n, t - n[-1], i + 1)  # list; value; starting p for list,default=0
                r = bisect_right(n, t // 2, l)
                # print(l,r)
                for J in n[l:r]:
                    K = t - J
                    # print("t,JandK ",t, J,K)
                    if K in f and K != J:
                        a.append((I, J, K))
        return a


# Main Call
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
