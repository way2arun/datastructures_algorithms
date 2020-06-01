"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3347/
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

"""

# Definition for a binary tree node.
from typing import List
from src.trees.printBinaryTree import PrintBinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Solution 1 - 28 ms
        """
        if root:
            # Start the invert here,
            root.left, root.right = root.right, root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            return root
        else:
            return None
        """
        # Solution 2 - 8 ms
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


# Main Call
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
root.right.left = TreeNode(6)

solution = Solution()
treeroot = solution.invertTree(root)
# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(treeroot)
print(response)
