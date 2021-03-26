"""
Word Subsets
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.



Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from typing import List, Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # Solution 1 - 1188 ms
        """
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)

        return [a for a in A if not cnt - Counter(a)]
        """
        # Solution 2 - 444 ms
        d = {}
        for word in B:
            for letter in word:
                if letter in d:
                    if word.count(letter) > d[letter]:
                        d[letter] = word.count(letter)

                else:
                    d[letter] = word.count(letter)

        result = []
        """
        for word in a:
            for letter, count in d.items():
                if word.count(letter) < count:
                    break
            else:
                result.append(word)
        """

        for word in A:
            for ch_r in d:
                if word.count(ch_r) < d[ch_r]:
                    break
            else:
                result.append(word)

        return result

        """
        d = {}
        for word in b:
            for k,c in Counter(word).items():
                d[k] = max(d[k], c) if k in d else c

        """

        """
        result = []
        for word in a:
            a_word_map = Counter(word)
            for k,c in d.items():
                if k not in a_word_map or c > a_word_map[k]:
                    break
            else:
                result.append(word)
        return result
        """


# Main Call
A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["e", "o"]

solution = Solution()
print(solution.wordSubsets(A, B))