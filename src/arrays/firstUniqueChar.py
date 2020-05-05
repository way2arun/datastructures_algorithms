"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Solution 1 - 92 ms
        set_cache = {}
        for char in s:
            if char not in set_cache:
                set_cache[char] = True
            else:
                set_cache[char] = False
        for index in range(len(s)):
            if set_cache[s[index]]:
                return index
        return -1
        """
        # Solution 2 36 ms
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
        """


# Main Call
solution = Solution()
s = "leetcode"
print(solution.firstUniqChar(s))
s = "loveleetcode"
print(solution.firstUniqChar(s))
