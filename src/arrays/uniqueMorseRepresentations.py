"""
Unique Morse Code Words
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Solution 1 - 24 ms
        """
        code_words = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        unique = set()
        for word in words:
            this = []
            for c in word:
                this.append(code_words[ord(c) - 97])
            unique.add(''.join(this))

        return (len(unique))
        """
        # Solution 2 - 20 ms
        """
        m = {}
        for x, y in zip(
                [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."],
                'abcdefghijklmnopqrstuvwxyz'
        ):
            m[y] = x
        result = set()
        for word in words:
            result.add(
                ''.join([m[c] for c in word])
            )
        return len(result)
        """

        # Solution 3 - 16 ms
        table = {'i': '..', 's': '...', 'd': '-..', 'h': '....', 'l': '.-..', 'b': '-...',
                 'a': '.-', 'u': '..-', 'k': '-.-', 'v': '...-', 'z': '--..', 'x': '-..-',
                 'n': '-.', 'r': '.-.', 'g': '--.', 'f': '..-.', 'p': '.--.', 'c': '-.-.',
                 'm': '--', 'w': '.--', 'o': '---', 'q': '--.-', 'j': '.---', 'y': '-.--',
                 'e': '.', 't': '-', }
        return len({"".join(table[c] for c in word) for word in words})


# Main Call
words = ["gin", "zen", "gig", "msg"]

solution = Solution()
print(solution.uniqueMorseRepresentations(words))
