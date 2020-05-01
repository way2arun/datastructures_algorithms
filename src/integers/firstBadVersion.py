"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

"""

first_bad = 0


def isBadVersion(version):
    """Mocked external API. Obligatory camelCaseName for consistency."""
    if version >= first_bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        # 8 ms
         left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
        """
        initial = 1
        latest = n
        while initial <= latest:
            mid = (initial + latest) // 2
            if not isBadVersion(mid):
                initial = mid + 1
            else:
                latest = mid - 1
        return initial


# Main Call
number = 5
first_bad = 4
solution = Solution()
print(solution.firstBadVersion(number))
