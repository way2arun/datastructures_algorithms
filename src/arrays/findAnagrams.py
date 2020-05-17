"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/
"""
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Solution 1 - 160 ms
        s_length = len(s)
        p_length = len(p)
        p_counter = collections.Counter(p)
        response = []
        for i in range(s_length - p_length + 1):
            if i == 0:
                s_counter = collections.Counter(s[:p_length])
            else:
                s_counter[s[i - 1]] -= 1
                s_counter[s[i + p_length - 1]] += 1
                if s_counter[s[i - 1]] == 0:
                    del s_counter[s[i - 1]]
            if s_counter == p_counter:
                response.append(i)
        return response


# Main Call
solution = Solution()
s = "abab"
p = "ab"
print(solution.findAnagrams(s, p))
