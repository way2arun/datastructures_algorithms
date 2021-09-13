"""
Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
   Hide Hint #1
Count the frequency of letters in the given string.
   Hide Hint #2
Find the letter than can make the minimum number of instances of the word "balloon".
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Solution 1 - 36 ms
        """
        word = {'a': 0, 'b': 0, 'l': 0, 'n': 0, 'o': 0}
        double_char = ['l', 'o']
        for c in text:
            if c in word:
                word[c] += 0.5 if c in double_char else 1
        return int(min(word.values()))
        """
        # Solution 2 - 16 ms
        d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for ch in text:
            if ch in d:
                d[ch] += 1 if ch in ('l', 'o') else 2

        return min(d.values()) // 2


# Main Call
text = "loonbalxballpoon"
solution = Solution()
print(solution.maxNumberOfBalloons(text))
