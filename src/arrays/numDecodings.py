"""
Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1


Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # Solution 1 - 44 ms
        """
        dp = [1, 0, 0]
        for c in s:
            dp_new = [0, 0, 0]
            dp_new[0] = (c > '0') * dp[0] + dp[1] + (c <= '6') * dp[2]
            dp_new[1] = (c == '1') * dp[0]
            dp_new[2] = (c == '2') * dp[0]
            dp = dp_new
        return dp[0]
        """
        # Solution 2 - 12 ms
        length = len(s)
        # length 0 case:
        if length == 0:
            return 0
        # length 1 case:
        if length == 1:
            if s[0] == "0":
                return 0
            else:
                return 1

        # now we assume length>=2:
        pos0 = 0
        pos1 = 1
        num0 = 1
        num1 = 0
        # initialize num1:
        if s[0] == "0":
            return 0
        else:
            num1 = 1
        for i in range(2, length + 1):
            num = 0
            if s[i - 1] != "0":
                num = num + num1
            if 26 >= int(s[i - 2:i]) >= 10:
                num = num + num0
            num0, num1 = num1, num
        return num1


# Main  Call
s = "226"
solution = Solution()
print(solution.numDecodings(s))