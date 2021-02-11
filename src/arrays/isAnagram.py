"""
Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1 - 40 ms
        """
        return Counter(s) == Counter(t)
        """
        # Solution 2 - 20 ms
        return {k: s.count(k) for k in set(s)} == {
            k: t.count(k) for k in set(t)}

# Main Call
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))