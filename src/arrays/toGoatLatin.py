"""
Goat Latin
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429/
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        # Solution 1 - 36 ms
        """
        ans = ''
        append = 'a'
        vowels = set('aeiouAEIOU')
        for word in S.split():
            if word[0] in vowels:
                word += 'ma'
            else:
                word += word[0] + 'ma'
                word = word.replace(word[0], '', 1)
            word += append
            append += 'a'
            if ans == '':
                ans += word
            else:
                ans += ' ' + word
        return ans
        """
        # Solution 2 - 12 ms

        W = S.split(" ")
        out = ''

        for i, s in enumerate(W):
            if s[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                s = s + "ma"
            else:
                s = s[1:] + s[0]
                s = s + "ma"
            while i >= 0:
                s = s + 'a'
                i = i - 1
            out = out + s + " "

        print(W)
        return out[0:len(out) - 1]

        # Solution 3  - 16 ms
        """
        S += " "
        vowels = set(list("aeiouAEIOU"))
        words = [""]
        for char in S:
            if char == " ":
                if words[-1][0] not in vowels:
                    words[-1] = words[-1][1:] + words[-1][0]
                words[-1] += "ma" + ("a" * len(words))
                words.append("")
            else:
                words[-1] += char
        return " ".join(words)[:-1]
        """


# Main Call
solution = Solution()
S = "I speak Goat Latin"
print(solution.toGoatLatin(S))
