"""
Find the Shortest Superstring
Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.



Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from functools import lru_cache
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # Solution 1 - 1064 ms
        """
        n = len(words)
        overlaps = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x, y = words[i], words[j]
                size = len(x)
                for k in range(1, size):
                    if y.startswith(x[k:]):
                        overlaps[i][j] = size - k
                        break

        @lru_cache(None)
        def helper(i, mask):
            if mask == (1 << n) - 1:
                return words[i]
            ans = '#' * 320
            for j in range(n):
                if mask & (1 << j) == 0:
                    k = overlaps[i][j]
                    string = helper(j, mask | (1 << j))
                    if len(words[i] + string[k:]) < len(ans):
                        ans = words[i] + string[k:]
            return ans

        return min([helper(i, 1 << i) for i in range(n)], key=len)
        """

        # Solution 2 -  560 ms
        def get_lps(string: str) -> List[int]:
            lps = [-1]
            i = 1
            while i < len(string):
                j = i - 1
                while lps[j] >= 0 and string[lps[j]] != string[j]:
                    j = lps[j]
                lps.append(lps[j] + 1)
                i += 1
            return lps

        def get_overlap(str1: str, str2: str) -> int:
            i = j = 0
            while i < len(str1) and j < len(str2):
                if j == -1 or str1[i] == str2[j]:
                    i += 1
                    j += 1
                else:
                    j = lps_dict[str2][j]
            return j

        n = len(words)

        lps_dict = {}
        for word in words:
            lps_dict[word] = get_lps(word)

        overlaps = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    overlaps[i][j] = get_overlap(words[i], words[j])

        dp = [[0] * n for _ in range(2 ** n)]
        p_dp = [[None for i in range(n)] for _ in range(2 ** n)]

        for mask in range(2 ** n):
            for i in range(n):
                # if ith bit (count from right to left) is set, update its value
                if mask & 1 << i:
                    parent_mask = mask ^ 1 << i
                    if not parent_mask:
                        continue
                    for j in range(n):
                        if parent_mask & 1 << j:
                            val = overlaps[j][i] + dp[parent_mask][j]
                            if val > dp[mask][i]:
                                dp[mask][i] = val
                                p_dp[mask][i] = j

        mask = 2 ** n - 1
        idx = dp[mask].index(max(dp[mask]))
        ans = ''
        while idx is not None:
            p_idx = p_dp[mask][idx]
            if p_idx is not None:
                overlap = overlaps[p_idx][idx]
                ans = words[idx][overlap:] + ans
            else:
                ans = words[idx] + ans
            mask ^= 1 << idx
            idx = p_idx

        i = 0
        while mask:
            if mask & 1 << i:
                ans = words[i] + ans
                mask ^= 1 << i
            i += 1

        return ans


# Main Call
words = ["alex", "loves", "leetcode"]
solution = Solution()
print(solution.shortestSuperstring(words))
