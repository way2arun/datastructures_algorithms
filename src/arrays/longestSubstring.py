"""
Longest Substring with At Least K Repeating Characters
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""
from typing import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Solution 1 -1300 ms
        """
        if len(s) == 0 or k > len(s):
            return 0
        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i + 1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)
        """
        # Solution 2 - 20 ms
        if len(s) < k or k == 0 or not s:
            return 0
        longest = 0
        sCount = Counter(s)
        split_index = 0
        while split_index < len(s) and k <= sCount[s[split_index]]:
            split_index += 1
        if split_index == len(s):
            return len(s)

        left = self.longestSubstring(s[:split_index], k)
        while split_index < len(s) and sCount[s[split_index]] < k:
            split_index += 1
        right = self.longestSubstring(s[split_index:], k)
        return max(left, right)



# Main Call
solution = Solution()
s = "ababbc"
k = 2
print(solution.longestSubstring(s, k))