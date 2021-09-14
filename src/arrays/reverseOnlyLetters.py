"""
Reverse Only Letters
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
   Hide Hint #1
This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.

"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Solution 1 - 44 ms
        """
        size = len(s)
        # convert into array of characters
        array = [*s]
        # two pointers, initialized with boundary index
        left, right = 0, size - 1
        #  swap english letter with two-pointers
        while left < right:
            # keep moving until we meet english letter on left hand side
            if not array[left].isalpha():
                left += 1
                continue
            # keep moving until we meet english letter on right hand side
            if not array[right].isalpha():
                right -= 1
                continue
            # swap english letters
            array[left], array[right] = array[right], array[left]
            # update index of two pointer
            left, right = left + 1, right - 1
        # convert to string and output
        return "".join(array)
        """
        # Solution 2 - 12 ms
        l, r = 0, len(s) - 1

        res = list(s)

        while l < r:
            if not res[l].isalpha():
                l += 1
            elif not res[r].isalpha():
                r -= 1
            else:
                res[l], res[r] = res[r], res[l]

                l += 1
                r -= 1

        return ''.join(res)


# Main Call
solution = Solution()
s = "a-bC-dEf-ghIj"
print(solution.reverseOnlyLetters(s))
