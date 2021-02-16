"""
Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.



Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # Solution 1 - 256 ms
        """
        letter_indexes = [i for i in range(len(S)) if not S[i].isdigit()]
        my_set = set()
        res = [S]
        for index in letter_indexes:
            for word in res:
                i = index
                for i in range(index, len(word)):
                    if not word[i].isdigit():
                        my_set.add(word[:i] + word[i].upper() + word[i + 1:])
                        my_set.add(word[:i] + word[i].lower() + word[i + 1:])

            res += list(my_set)
            res = list(set(res))
        return res
        """
        # Solution 2 - 32 ms
        results = [S]
        for i in range(len(S)):
            c = S[i]
            if '0' <= c <= '9':
                continue
            n = len(results)
            for j in range(n):
                s = results[j]
                if 'a' <= c <= 'z':
                    new_C = c.upper()
                else:
                    new_C = c.lower()
                results.append(s[:i] + new_C + s[i + 1:])
        return results


# Main Call
S = "a1b2"
solution = Solution()
print(solution.letterCasePermutation(S))