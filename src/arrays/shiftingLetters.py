"""
Shifting Letters
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.



Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
shifts.length == s.length
0 <= shifts[i] <= 109
"""
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Solution 1 - 1887  ms
        """
        n = len(s)
        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        ans = []
        for i, c in enumerate(s):
            idx = (ord(c) - ord('a') + shifts[i]) % 26
            ans.append(chr(idx + ord('a')))
        return "".join(ans)
        """
        # Solution 2 - 184 ms
        n = len(s)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = (suffix_sum[i + 1] + shifts[i]) % 26
        ans = ''
        # print(suffix_sum)
        for i, c in enumerate(s):
            val = (ord(c) + suffix_sum[i])
            if val > ord('z'):
                val = val - ord('z') + ord('a') - 1
            ans += chr(val)
        return ans


# Main Call
s = "abc"
shifts = [3, 5, 9]
solution = Solution()
print(solution.shiftingLetters(s, shifts))