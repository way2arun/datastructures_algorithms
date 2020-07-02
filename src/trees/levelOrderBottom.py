"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        if not root:
            return self.levels

        self.helper(root, 0)
        return self.levels[::-1]

    def helper(self, node, level):
        if len(self.levels) == level:
            self.levels.append([])

        self.levels[level].append(node.val)

        if node.left:
            self.helper(node.left, level + 1)
        if node.right:
            self.helper(node.right, level + 1)


# Main Call
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

solution = Solution()
print(solution.levelOrderBottom(root))
