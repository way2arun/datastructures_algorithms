"""
Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

"""
from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # Solution 1 - 312 ms
        """
        def is_subseq(main: str, sub: str) -> bool:
            i, j, m, n = 0, 0, len(main), len(sub)
            while i < m and j < n and n - j >= m - i:
                if main[i] == sub[j]:
                    i += 1
                j += 1
            return i == m

        res = ''
        helper = sorted(d, key=lambda x: len(x), reverse=True)
        for word in helper:
            if len(word) < len(res): return res
            if (not res or word < res) and is_subseq(word, s):
                res = word
        return res
        """
        # Solution 2 - 60 ms
        result = ""
        for w in d:
            diff = len(w) - len(result)
            if diff >= 0:
                if diff > 0 or w < result:
                    try:
                        pos = -1
                        for c in w:
                            pos = s.index(c, pos + 1)
                        result = w
                    except ValueError:
                        pass
        return result


# Main Call
s = "abpcplea"
d = ["ale", "apple", "monkey", "plea"]

solution = Solution()
print(solution.findLongestWord(s, d))