"""
 Check If a String Contains All Binary Codes of Size K
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.



Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "00110", k = 2
Output: true
Example 3:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
Example 4:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
Example 5:

Input: s = "0000000001011100", k = 4
Output: false


Constraints:

1 <= s.length <= 5 * 10^5
s consists of 0's and 1's only.
1 <= k <= 20
   Hide Hint #1
We need only to check all sub-strings of length k.
   Hide Hint #2
The number of distinct sub-strings should be exactly 2^k.
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Solution 1 - 676 ms
        """
        last = int(s[:k], 2)
        ss = {last}
        for i in range(k, len(s)):
            last = last * 2 - (int(s[i - k]) << k) + int(s[i])
            ss.add(last)

        return len(ss) == 1 << k
        """
        # Solution 2 - 312 ms
        """
        need = 1 << k
        store = [False] * need
        hash_val = 0
        all_one = need - 1

        for i in range(len(s)):
            hash_val = ((hash_val << 1) & all_one) | int(s[i])
            if i >= k - 1 and store[hash_val] is False:
                store[hash_val] = True
                need -= 1
                if need == 0: return True
        return False
        """
        # Solution 3 - 280 ms
        res = set()
        for i in range(0, len(s) - k + 1):
            if s[i:i + k] not in res:
                res.add(s[i:i + k])
                if len(res) == 2 ** k:
                    break
        return len(res) == 2 ** k


# Main Call
s = "0110"
k = 2

solution = Solution()
print(solution.hasAllCodes(s, k))