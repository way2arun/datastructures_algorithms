"""
To Lower Case
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"


Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
   Hide Hint #1
Most languages support lowercase conversion for a string data type. However, that is certainly not the purpose of the problem. Think about how the implementation of the lowercase function call can be done easily.
   Hide Hint #2
Think ASCII!
   Hide Hint #3
Think about the different capital letters and their ASCII codes and how that relates to their lowercase counterparts. Does there seem to be any pattern there? Any mathematical relationship that we can use?

"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        # Solution 1 - 24 ms
        """
        ans = ""
        for c in s:
            n = ord(c)
            ans += chr(n + 32) if 64 < n < 91 else c
        return ans
        """
        # Solution 2 - 16 ms
        """
        res = ""
        for val in s:
            if 65 <= ord(val) <= 90:
                res += chr(ord(val) + 32)
            else:
                res += val

        return res
        """
        # Solution 3 - 16 ms
        #return "".join(chr(ord(i) + 32) if "A" <= i <= "Z" else i for i in s)

        # Solution 4 - 12 ms (with in-built library)
        return s.lower()




# Main Call
s = "LOVELY"
solution = Solution()
print(solution.toLowerCase(s))
