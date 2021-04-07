"""
Determine if String Halves Are Alike
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true


Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
   Hide Hint #1
Create a function that checks if a character is a vowel, either uppercase or lowercase.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Solution 1 - 36 ms
        """
        s, n, cand = s.lower(), len(s), set("aeiou")
        return sum(i in cand for i in s[:n // 2]) == sum(i in cand for i in s[n // 2:])
        """
        # Solution 2 - 16 ms
        if not s or len(s) == 1:
            return False
        l = len(s)
        t = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        mid = l // 2
        cnt1 = sum((1 for e in s[:mid] if e in t))
        cnt2 = sum((1 for e in s[mid:] if e in t))
        return cnt1 == cnt2


# Main Call
s = "book"
solution = Solution()
print(solution.halvesAreAlike(s))