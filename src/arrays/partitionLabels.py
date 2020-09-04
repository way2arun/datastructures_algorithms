"""
Partition Labels
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.


   Hide Hint #1
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.

The idea of this solution is greedily construct our partition, let us consider the example
S = ababcbacdefegdehijhklij. We need to start with letter a and we can not stop, until we reach the last occurence of a: so, we need to take ababcba part at least. But if we take this part, we need to consider letters b and c as well and also traverse our string until we meet the last occurence of these letters, so we need to take ababcbac. Here we can stop, because we already take into account all symbols inside this string. So, we go to the next symbol and repeat our partition. So, what we have in my code:

First, we need to know all ends for each letter in advance, I call it ends.
Also, curr is current index and last is index we need to traverse until. For each group of symbols we need to do: last = ends[S[curr]]: we find the place we need to traverse; while we do no reach this place, we look at the next symbol and update our last. So, we stop, when curr become greater than last.
We add curr to our out result.
Note, that we need to have [8,7,8] for our example, but we get [8,15,23], places where our partitions are. So, we evaluate differences 8-0, 15-8, 23-15 and return them.
Complexity: time complexity is O(n), we traverse our string twice: one time when we evaluate ends and second time when we do partitions. Space complexity is O(26): to keep our ends (also we have answer, but it can not be greater than 26 as well).

"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Solution 1 - 40 ms
        """
        ends = {c: i for i, c in enumerate(S)}
        curr, out = 0, [0]

        while curr < len(S):
            last = ends[S[curr]]
            while curr <= last:
                symb = S[curr]
                last = max(last, ends[symb])
                curr += 1
            out.append(curr)

        return [out[i] - out[i - 1] for i in range(1, len(out))]
        """
        # Solution 2 - 20 ms
        last = {s: i for i, s in enumerate(S)}
        j, anchor = 0, 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans



# Main Call
S = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(S))
