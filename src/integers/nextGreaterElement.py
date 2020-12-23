"""
Next Greater Element III
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1


Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Solution 1 - 28 ms
        """
        digits = list(str(n))
        i = len(digits) - 1
        while i - 1 >= 0 and digits[i] <= digits[i - 1]:
            i -= 1

        if i == 0: return -1

        j = i
        while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
            j += 1

        digits[i - 1], digits[j] = digits[j], digits[i - 1]
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))

        return ret if ret < 1 << 31 else -1
        """
        # Solution 2 - 16 ms
        nums = list(str(n))
        pivot = len(nums) - 2
        while pivot >= 0:
            if nums[pivot] < nums[pivot + 1]:
                break
            pivot -= 1
        if pivot < 0:
            return -1
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        num = int(''.join(nums[:pivot + 1] + nums[pivot + 1:][::-1]))
        return num if num < 2 ** 31 - 1 else -1


# Main Call
solution = Solution()
n = 12
print(solution.nextGreaterElement(n))
