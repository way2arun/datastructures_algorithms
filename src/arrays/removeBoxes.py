"""
Remove Boxes
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.



Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)
Example 2:

Input: boxes = [1,1,1]
Output: 9
Example 3:

Input: boxes = [1]
Output: 1


Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
"""
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # Solution 1 - 8538 ms
        """
        @lru_cache(None)
        def dp(i, j, k):
            if i > j: return 0
            indx = [m for m in range(i + 1, j + 1) if boxes[m] == boxes[i]]
            ans = (k + 1) ** 2 + dp(i + 1, j, 0)
            return max([ans] + [dp(i + 1, m - 1, 0) + dp(m, j, k + 1) for m in indx])

        return dp(0, len(boxes) - 1, 0)
        """
        # Solution 2 - 364 ms
        pairs = [(i, c) for i, c in enumerate(boxes) if i == 0 or c != boxes[i - 1]]
        length = [pairs[j + 1][0] - i if j < len(pairs) - 1 else len(boxes) - i
                  for j, (i, c) in enumerate(pairs)]
        nums = [c for i, c in pairs]

        table = defaultdict(list)
        for j, n in enumerate(nums):
            table[n] += j,

        @lru_cache(None)
        def dfs(i, j, lead):
            # if i>j:
            #     return 0
            lead += length[i]

            if (j > i) and (nums[j] == nums[i]):
                lead += length[j]
                j -= 1

            if i == j:
                return lead ** 2

            ans = lead ** 2 + dfs(i + 1, j, 0)

            n = nums[i]
            ### binary search for the next index which are same as box i
            ### replace the for loop
            ### will be faster if boxes.length is longer
            # next_i_ind = bisect.bisect_right(table[n], i)
            # while next_i_ind<len(table[n]) and table[n][next_i_ind] <= j:
            #     k = table[n][next_i_ind]
            #     ans = max( ans, dfs(i+1,k-1, 0) + dfs(k,j, lead+length[i]) )
            #     next_i_ind += 1
            for l in range(i + 1, j + 1):
                if nums[l] == n:
                    ans = max(ans, dfs(i + 1, l - 1, 0) + dfs(l, j, lead))

            # n = boxes[i]
            # k = next((k for k, x in enumerate(boxes[i+1:j+1], start=i+1) if x != n), None)
            # if k is None:
            #     return (lead+j-i+1)**2
            # ans = (lead+k-i)**2 + dfs(k,j,0)
            # for l in range(k+1,j+1):
            #     if boxes[l] == n:
            #         ans = max( ans, dfs(k,l-1, 0) + dfs(l,j, lead+k-i) )

            # ### much slower
            # if i>j: return 0
            # ans = (lead+1)**2 + dfs(i+1, j, 0)
            # for l in range(i+1, j+1):
            #     if boxes[l] == boxes[i]:
            #         ans = max( ans, dfs(i+1, l-1, 0) + dfs(l,j, lead+1) )

            return ans

        return dfs(0, len(nums) - 1, 0)


# Main Call
solution = Solution()
boxes = [1,3,2,2,2,3,4,3,1]
print(solution.removeBoxes(boxes))