"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution 1 - 104 ms
        """
        characters = set()
        left = right = ans = 0
        length = len(s)

        while right < length:
            if s[right] in characters:
                characters.remove(s[left])
                left += 1
            else:
                characters.add(s[right])
                right += 1
                ans = max(ans, right - left)

        return ans
        """
        # Solution 2 - 24 ms
        if len(s) < 2:
            return len(s)
        long_str = ''
        len_val = 0
        for i in range(len(s)):
            if s[i] not in long_str:
                long_str += s[i]
            else:
                ref_ind = long_str.find(s[i])
                len_val = max(len_val, len(long_str))
                long_str = long_str[ref_ind + 1:] + s[i]
        return max(len_val, len(long_str))


# Main Call
s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))