"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        # using hash method
        # 68 ms
        magazine_word_count = {}
        for word in magazine:
            if word in magazine_word_count:
                magazine_word_count[word] += 1
            else:
                magazine_word_count[word] = 1

        print(magazine_word_count)

        for word in ransomNote:
            if word in magazine_word_count and magazine_word_count[word] > 0:
                magazine_word_count[word] -= 1
            else:
                return False
        return True
        """
        # 16 ms
        count = Counter(ransomNote)
        print(count)
        for k, v in count.items():
            print(magazine.count(k))
            if magazine.count(k) < v:
                return False

        return True


# Main Call
solution = Solution()
ransomNote = "aa"
magazine = "aab"
print(solution.canConstruct(ransomNote, magazine))
ransomNote = "aa"
magazine = "ab"
print(solution.canConstruct(ransomNote, magazine))