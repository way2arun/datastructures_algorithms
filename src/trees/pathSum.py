"""
Path Sum III
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3417/
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""


# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Solution 1 - 60 ms
        """
        self.result = 0
        self.count = defaultdict(int)

        self.count[sum] = 1
        self.dfs(root, sum, 0)

        return self.result
        """
        # Solution 2 -
        count = 0
        d = defaultdict(int)
        d[0] = 1

        def helper(root, currSum, k):
            nonlocal count

            if root is None:
                return

            currSum += root.val

            count += d[currSum - k]

            d[currSum] += 1

            helper(root.left, currSum, k)
            helper(root.right, currSum, k)
            d[currSum] -= 1
            currSum -= root.val

        helper(root, 0, sum)
        return count

    # Solution 1 - 60 ms
    def dfs(self, root, sum, root_sum):
        if not root:
            return None

        root_sum += root.val
        self.result += self.count[root_sum]
        self.count[root_sum + sum] += 1
        self.dfs(root.left, sum, root_sum)
        self.dfs(root.right, sum, root_sum)
        self.count[root_sum + sum] -= 1


# Main Call
# Tree Node
tree_root = TreeNode(10)
tree_root.left = TreeNode(5)
tree_root.left.left = TreeNode(3)
tree_root.left.left.left = TreeNode(3)
tree_root.left.right = TreeNode(2)
tree_root.left.right.right = TreeNode(1)
tree_root.left.left.right = TreeNode(-2)
tree_root.right = TreeNode(-3)
tree_root.right.right = TreeNode(11)

sum = 8
solution = Solution()
print(solution.pathSum(tree_root, sum))