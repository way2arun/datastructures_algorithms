"""
Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
   Hide Hint #1
Use two pointers to create a window of letters in S, which would have all the characters from T.
   Hide Hint #2
Since you have to find the minimum window in S which has all the characters from T, you need to expand and contract the window using the two pointers and keep checking the window for all the characters. This approach is also called Sliding Window Approach.

L ------------------------ R , Suppose this is the window that contains all characters of T

        L----------------- R , this is the contracted window. We found a smaller window that still contains all the characters in T

When the window is no longer valid, start expanding again using the right pointer.
"""
import collections
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Solution 1  - 152 ms
        """
        beg, end = 0, 0
        ans, found = (float("inf"), 0), 0
        cnt_t, cnt_s = Counter(t), Counter()
        while end <= len(s):
            if found == len(cnt_t):
                ans = min(ans, (end - beg, beg))
                old = s[beg]
                if cnt_s[old] == cnt_t[old]: found -= 1
                cnt_s[old] -= 1
                beg += 1
            else:
                if end == len(s): break
                new = s[end]
                if cnt_s[new] == cnt_t[new] - 1: found += 1
                cnt_s[new] += 1
                end += 1

        return s[ans[1]:ans[0] + ans[1]] if ans[0] != float("inf") else ""
        """
        # Solution 2 - 56 ms
        target_count_dict = collections.defaultdict(int)
        for ch in t:
            target_count_dict[ch] += 1

        remain_missing = len(t)
        end_pos = len(s) + 1
        current_start = start_pos = 0

        for current_end, ch in enumerate(s, 1):
            remain_missing -= target_count_dict[ch] > 0
            target_count_dict[ch] -= 1

            if not remain_missing:
                while target_count_dict[s[current_start]] < 0:
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end

                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1

        return s[start_pos:end_pos] if end_pos <= len(s) else ''

# Main Call
s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))