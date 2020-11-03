"""
Consecutive Characters
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1


Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
   Hide Hint #1
Keep an array power where power[i] is the maximum power of the i-th character.
   Hide Hint #2
The answer is max(power[i]).
"""
from itertools import chain


class Solution:
    def maxPower(self, s: str) -> int:
        # Solution 1 - 40 ms
        """
        if len(s) == 1:
            return 1
        max_power = 0
        # starting power from first char
        curr_power = 1
        for i in range(1, len(s)):
            # reset current power if current char not equal to previous and add more power if its equal
            curr_power = 1 if s[i] != s[i - 1] else curr_power + 1
            if curr_power > max_power:
                max_power = curr_power
        return max_power
        """
        # Solution 2 - 28 ms
        """
        curr = ''
        count = 0
        mx = 0
        for i in s:
            if i == curr:
                count += 1
            else:
                curr = i
                if count > mx:
                    mx = count
                count = 0

        if count > mx:
            mx = count
        return mx + 1
        """

        # Solution 3 - 24 ms
        s = chain(s, '\n')
        res = cur = 1
        prev = next(s)
        for x in s:
            if x != prev:
                if cur > res:
                    res = cur
                cur = 1
            else:
                cur += 1
            prev = x
        return res


# Main Call
s = "hooraaaaaaaaaaay"
solution = Solution()
print(solution.maxPower(s))
