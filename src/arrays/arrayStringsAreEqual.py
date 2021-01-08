"""
Check If Two String Arrays are Equivalent
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.



Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true


Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
   Hide Hint #1
Concatenate all strings in the first array into a single string in the given order, the same for the second array.
   Hide Hint #2
Both arrays represent the same string if and only if the generated strings are the same.
"""
from typing import List


class Solution:
    def gen(self, word: List[str]):
        for s in word:
            for c in s:
                yield c
        # Ensure False when len(word1) != len(word2)
        yield None

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Solution 1 - 64 ms
        """
        for c1, c2 in zip(self.gen(word1), self.gen(word2)):
            if c1 != c2:
                return False
        return True
        """
        # Solution 2 - 12 ms
        return "".join(word1) == "".join(word2)

        # Want to now reduce space
        # Check each letter with loops

        i1, i2, j1, j2 = 0

        while i1 < len(word1) and i2 < len(word2):

            if word1[i1][j1] != word2[i2][j2]:
                return False

            if jl == len(word1)[i1]: j1 = 0; i1 += 1
            if j2 == len(word2)[i2]: j2 = 0; i2 += 1

            # Once we reach the end of both, i1 and i2 will be the len of the array (at the end)
            if i1 == len(word1) and i2 == len(word2): return True

        return False


# Main Call
word1 = ["ab", "c"]
word2 = ["a", "bc"]
solution = Solution()
print(solution.arrayStringsAreEqual(word1, word2))
