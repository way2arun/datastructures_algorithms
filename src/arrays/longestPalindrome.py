"""
 Longest Palindrome
 Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423/
"""
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Solution 1 - 48 ms
        """
        s_list = list(s)
        set_s_list = set(s_list)
        f = 0
        p = 0
        for x in set_s_list:
            if s_list.count(x) % 2 == 0:
                f += s_list.count(x)
            else:
                f += s_list.count(x) - 1
                p = 1
        if p:
            f += 1
        return f
        """
        # Solution 2 - 8 ms

        c = collections.Counter(s)
        res = odd = 0
        for value in c.values():
            if value % 2 == 1:
                odd = 1
            res += value // 2 * 2
        return res + 1 if odd else res

        # Solution 3 - 16 ms
        """
        dic = collections.Counter(s)
        ans = 0
        for i in dic.values():
            ans += i // 2 * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans
        """


# Main Call
solution = Solution()
s = "abccccdd"
print(solution.longestPalindrome(s))
