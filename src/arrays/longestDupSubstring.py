"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""


Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
   Hide Hint #1
Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
   Hide Hint #2
To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3365/
"""


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def substring_search(middle, mod):
            current = 0
            for i in range(middle):
                current = (current * 26 + nums[i]) % mod
            found = {current}
            p = pow(26, middle, mod)
            for pos in range(1, S_length - middle + 1):
                current = (current * 26 - nums[pos - 1] * p + nums[pos + middle - 1]) % mod
                if current in found:
                    return pos
                found.add(current)
            return -1

        S_length = len(S)
        nums = [ord(c) - ord('a') for c in S]
        left = 1
        right = S_length
        index = -1

        mod = 2 ** 63 - 1

        while left <= right:
            middle = (left + right) // 2
            cur = substring_search(middle, mod)
            if cur != -1:
                left = middle + 1
                index = cur
            else:
                right = middle - 1
        return S[index: index + left - 1]


# Main Call
solution = Solution()
S = "banana"
print(solution.longestDupSubstring(S))
