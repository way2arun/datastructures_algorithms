"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
   Hide Hint #1
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        counter = 0
        s_length = len(s) - 1
        while counter <= s_length:
            s[counter], s[s_length] = s[s_length], s[counter]
            counter += 1
            s_length -= 1
        return s
        """
        # Solution 2
        for index in range(len(s) // 2):
            s[index], s[-index - 1] = s[-index - 1], s[index]
        return s


# Main Call
solution = Solution()
s = ["h", "e", "l", "l", "o"]
print(solution.reverseString(s))
