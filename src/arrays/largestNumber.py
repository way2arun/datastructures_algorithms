"""
Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472/
"""
from functools import cmp_to_key
from typing import List


# Solution 3 - 24 ms
class Comparator(str):
    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Solution 1 - 36 ms
        """
        str_nums = []
        for num in nums:
            str_nums.append(str(num))  # turn numbers to strings

        str_nums.sort(reverse=True)  # sort by lexicographical order

        flag = False  # flag to keep track if there were swaps, if no more swaps needed - finished
        while not flag:
            flag = True
            i = 0
            while i < len(str_nums) - 1:
                if str_nums[i] + str_nums[i + 1] < str_nums[i + 1] + str_nums[i]:  # if larger when swapped - swap
                    str_nums[i], str_nums[i + 1] = str_nums[i + 1], str_nums[i]
                    flag = False
                i += 1

        res = "".join(str_nums)

        if res[0] == '0':
            return str(0)

        return res
        """

        # Solution 2 - 20 ms

        def cmp(x, y):
            u = x + y
            v = y + x
            if u == v:
                return 0
            elif u < v:
                return -1
            else:
                return 1

        v = map(str, nums)
        result = ''.join(reversed(sorted(v, key=cmp_to_key(cmp))))
        if result and result[0] == '0':
            return '0'
        else:
            return result

        # Solution 3 - 24 ms
        """
        if not nums:
            return ""
        nums = list(map(str, nums))
        nums.sort(reverse=True, key=Comparator)
        return "".join(nums) if nums[0] != "0" else "0"
        """


# Main Call
nums = [3, 30, 34, 5, 9]
solution = Solution()
print(solution.largestNumber(nums))
