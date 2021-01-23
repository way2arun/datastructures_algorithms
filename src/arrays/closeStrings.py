"""
Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
Example 4:

Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.


Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
   Hide Hint #1
Operation 1 allows you to freely reorder the string.
   Hide Hint #2
Operation 2 allows you to freely reassign the letters' frequencies.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Solution 1 - 304 ms
        """
        ht1 = {}
        ht2 = {}
        for word in word1:
            if word not in ht1:
                ht1[word] = 1
            else:
                ht1[word] += 1
        for word in word2:
            if word not in ht2:
                ht2[word] = 1
            else:
                ht2[word] += 1
        if ht1.keys() != ht2.keys():
            return False
        list1 = ht1.values()
        list2 = ht2.values()
        return sorted(list1) == sorted(list2)
        """
        # Solution 2 - 52 ms
        # things that are constant on both operations:
        #   len of the strings, they must be equal
        #       len(word1) must equal len(word2)
        #   the set of counts of the unique characters in the string
        #       some permutation of the keys in count_dict of word1 must be equal to that of word2
        #   the set of unique characters in the string
        #       the keys of count_dict must be equal to that of word2
        # if len(word1) != len(word2):
        #    return False
        # counts1 = {}
        # counts2 = {}
        # for x,y in zip(word1,word2):
        #    counts1[x] = counts1.get(x,0) + 1
        #    counts2[y] = counts2.get(y,0) + 1
        # if counts1.keys() != counts2.keys():
        #    return False
        # return sorted(counts1.values()) == sorted(counts2.values())
        if len(word1) != len(word2):
            return False
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        counts1 = []
        counts2 = []
        for char in alpha:
            in1, in2 = char in word1, char in word2
            if in1 and in2:
                counts1.append(word1.count(char))
                counts2.append(word2.count(char))
            elif (in2 and not in1) or (in1 and not in2):
                return False
        counts2.sort()
        counts1.sort()
        return counts1 == counts2


# Main Call
word1 = "cabbba"
word2 = "abbccc"

solution = Solution()
print(solution.closeStrings(word1, word2))