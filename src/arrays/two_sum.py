"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# Time Complexity :- O(n^2)
# Space Complexity - O(1)


def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target - (nums[i] + nums[j]) == 0:
                return [i, j]


nums = [2, 6, 7, 11, 15]
target = 9

print(two_sums(nums, target))
