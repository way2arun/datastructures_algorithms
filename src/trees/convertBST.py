"""
Convert BST to Greater Tree
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/



Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
Example 3:

Input: root = [1,0,2]
Output: [3,3,2]
Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]


Constraints:

The number of nodes in the tree is in the range [0, 104].
-104 <= Node.val <= 104
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.
"""

from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        # Solution 1 - 84 ms
        """
        if not root: return
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root
        """
        # Solution 2 - 64 ms
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)
        return root


# Main Call
root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

solution = Solution()
node = solution.convertBST(root)
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
