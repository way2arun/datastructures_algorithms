"""
Buddy Strings
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".



Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.
"""
from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # Solution 1 - 24 ms
        """
        if len(A) != len(B):
            return False
        else:
            # For small set of data, it uses 2 for loops.
            if len(A) < 1000 or len(B) < 1000:
                for i in range(len(A)):
                    for j in range(i + 1, len(A)):
                        A_changed = A[:i] + A[j] + A[i + 1:j] + A[i] + A[j + 1:]
                        if A_changed == B:
                            return True

            # For large set of data, it uses difference of characters and store them in a list and then swap.
            else:
                # check whether both the listes are made up of same character, if yes then return True.
                if A[0] * len(A) == B:
                    return True
                diff = []
                for k in range(len(A)):
                    if A[k] != B[k]:
                        diff.append(k)

                if len(diff) == 2:
                    i = diff[0]
                    j = diff[1]
                    A_changed = A[:i] + A[j] + A[i + 1:j] + A[i] + A[j + 1:]
                    if A_changed == B:
                        return True
        return False
        """
        # Solution 2 - 16 ms

        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False
        if A == B:
            cnt = Counter(A)
            return bool([v for v in cnt.values() if v > 1])
        diffs = []
        for i, a in enumerate(A):
            if a != B[i]:
                diffs.append(i)
        if len(diffs) == 2:
            i, j = diffs
            return A[i] == B[j] and A[j] == B[i]

        return False

        # Solution 3 - 20 ms
        """
        if len(A) != len(B) or set(A) != set(B): return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)
                if counter > 2:
                    return False
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]
        """



# Main Call
A = "aaaaaaabc"
B = "aaaaaaacb"
solution = Solution()
print(solution.buddyStrings(A, B))
