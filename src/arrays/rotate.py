"""
Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
   Hide Hint #1
The easiest solution would use additional memory and that is perfectly fine.
   Hide Hint #2
The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
   Hide Hint #3
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.
   Hide Hint #4
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.

"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1 - 60 ms
        """
        if k == 0:
            return nums
        pos = k % len(nums)
        nums[:len(nums) - pos], nums[len(nums) - pos:] = nums[len(nums) - pos:], nums[:len(nums) - pos]
        print(nums)
        """
        # Solution 2 - 40 ms
        a = nums[len(nums) - k:]
        a += nums[0: len(nums) - k]
        nums[:] = a
        print(nums)
        # Solution 3 - 44 ms
        """
        count = 0
        n = len(nums)
        start = 0
        while count < n:
            current = start
            nxt = (current + k) % n
            prev = nums[current]
            while True:
                tmp = nums[nxt]
                nums[nxt] = prev
                count += 1
                prev = tmp
                current = nxt
                nxt = (current + k) % n
                if current == start:
                    start += 1
                    break
        print(nums)
        """





# Main Call
solution = Solution()
nums = [-1, -100, 3, 99]
k = 2
solution.rotate(nums, k)
