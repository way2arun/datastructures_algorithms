"""
Palindromic Substrings
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.


   Hide Hint #1
How can we reuse a previously computed palindrome to compute a larger palindrome?
   Hide Hint #2
If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
   Hide Hint #3
Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation?

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
               :type s: str
               :rtype: int
        """
        # Solution 1 - 108 ms
        """
        length = len(s)

        def getPCount(b, e):
            ans = 0
            while b >= 0 and e < length and s[b] == s[e]:
                b -= 1
                e += 1
                ans += 1
            return ans

        ret = 0
        for i in range(length):
            ret += getPCount(i, i)
            if i > 0:
                ret += getPCount(i - 1, i)
        return ret
        """
        # Solution 2 - 24 ms
        count = 0
        i = 0

        while i < len(s):
            r = i
            l = i

            # Count the number of consecutive duplicates of the current character
            duplicates = 1
            # Move right pointer to the last duplicate of value, s[i]
            while r < len(s) - 1 and s[r] == s[r + 1]:
                r += 1
                duplicates += 1

            # Arithmetic sum
            # NOTE: explanation of this below
            count += duplicates * (duplicates + 1) // 2

            # Set the next starting point
            i = r + 1

            # Expand outwards to find longer palindrome
            while r < len(s) - 1 and l > 0 and s[r + 1] == s[l - 1]:
                r += 1
                l -= 1
                count += 1

        return count


# Main Call
s = "aaa"
solution = Solution()
print(solution.countSubstrings(s))

