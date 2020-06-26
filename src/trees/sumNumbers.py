"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3372/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # depth first search + global sum
        # Solution 1 - 32 ms
        """
        self.result = 0
        self.dfs(root, 0)
        return self.result
        """
        # Solution 2 - 16 ms
        self.result = [0]
        self.cr = [0]
        if root is not None:
            self.traverse(root)
        return self.result[0]

    def dfs(self, root, summation):
        if not root:
            return

        summation = summation * 10 + root.val
        # leaf situation
        if root.left is None and root.right is None:
            self.result += summation
            return
        self.dfs(root.left, summation)
        self.dfs(root.right, summation)

    def traverse(self, node):
        if node.left is None and node.right is None:
            self.result[0] += self.cr[0] * 10 + node.val
            return
        self.cr[0] = self.cr[0] * 10 + node.val
        if node.left is not None:
            self.traverse(node.left)
        if node.right is not None:
            self.traverse(node.right)
        self.cr[0] = self.cr[0] // 10


# Main Call
tree_root = TreeNode(4)
tree_left_1 = TreeNode(9)
tree_right_1 = TreeNode(0)
tree_left_2 = TreeNode(5)
tree_left_3 = TreeNode(1)

tree_root.left = tree_left_1
tree_left_1.left = tree_left_2
tree_left_1.right = tree_left_3
tree_root.right = tree_right_1

solution = Solution()
print(solution.sumNumbers(tree_root))
