"""
Repeated DNA Sequences
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Solution 1 - 68 ms
        """
        d = {}
        ans = set()
        start = 0
        end = 10
        while end <= len(s):
            if s[start:end] in d:
                if s[start:end] not in ans:
                    ans.add(s[start:end])
            else:
                d[s[start:end]] = 1
            start += 1
            end += 1
        return ans
        """
        # Solution 2 - 32 ms
        seen = set()
        res = set()
        for i in range(len(s)):
            new = s[i: i + 10]
            if new in seen:
                res.add(new)
            else:
                seen.add(new)
        return res


# Main Call
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
solution = Solution()
print(solution.findRepeatedDnaSequences(s))
