"""
Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:
        # Solution 1 - 28 ms
        """
        st = []
        for ch in s:
            st.append(ch)
            if st[-1] == ']':
                cur = []
                st.pop()
                while not st[-1].isdigit():
                    new_ele = st.pop()
                    if new_ele != '[':
                        cur.append(new_ele)
                num = ""
                while st and st[-1].isdigit():
                    num += st.pop()
                for ele in reversed(cur * int(num[::-1])):
                    st.append(ele)
        return "".join(st)
        """
        # Solution 2 - 12 ms
        stack = []
        res = []

        for char in s:
            if char == ']':
                tmpStr = []
                k = 0
                base = 0
                while stack[-1] != '[':
                    tmpStr.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isnumeric():
                    num = stack.pop()
                    k += (ord(num) - ord('0')) * (10 ** base)
                    base += 1
                for _ in range(k):
                    for i in range(len(tmpStr) - 1, -1, -1):
                        stack.append(tmpStr[i])
            else:
                stack.append(char)

        return ''.join(stack)


# Main Call
s = "2[abc]3[cd]ef"
solution = Solution()
print(solution.decodeString(s))