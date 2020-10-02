"""
Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3481/
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solution 1 - 100 ms
        """
        results = []
        # at each iteration we will update the list of targets
        targets = [[target]]
        while targets:
            next_targets = []
            for cur_sequence in targets:
                cur_target = cur_sequence[0]
                for candidate in candidates:
                    # to avoid duplicates we only add the candidate sequences in ascending order
                    if len(cur_sequence) == 1 or cur_sequence[1] >= candidate:
                        if candidate < cur_target:
                            next_targets.append([cur_target - candidate, candidate] + list(cur_sequence[1:]))
                        elif candidate == cur_target:
                            results.append(cur_sequence)
            targets = next_targets
        return results
        """
        # Solution 2 - 28 ms
        self.ans = []
        self.candidates = sorted(candidates)
        self.recursor(target, [], 0)
        return self.ans

        # Solution 3 - 32 ms
        """
        candidates.sort()
        res = [set() for _ in range(target + 1)]
        res[0].add(())
        for num in candidates:
            for off in range(0, target - num + 1):
                for seq in res[off]:
                    res[num + off].add(seq + (num,))
        return res[target]
        """

    def recursor(self, target, order, index):
        for i, x in enumerate(self.candidates[index:]):
            if target >= 2 * x:
                self.recursor(target - x, order + [x], index + i)
            elif x == target:
                self.ans.append(order + [x])
            elif x > target:
                break


# Main Call
solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(solution.combinationSum(candidates, target))
