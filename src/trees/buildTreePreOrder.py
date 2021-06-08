"""
Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import List
from src.trees.printBinaryTree import PrintBinaryTree

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Solution 1 - 60 ms
        """
        def helper(pr_beg, pr_end, in_beg, in_end):
            if pr_end - pr_beg <= 0:
                return None
            ind = dic[preorder[pr_beg]]
            root = TreeNode(inorder[ind])
            root.left = helper(pr_beg + 1, pr_beg + 1 + ind - in_beg, in_beg, ind)
            root.right = helper(pr_beg + ind - in_beg + 1, pr_end, ind + 1, in_end)
            return root

        dic = {elem: it for it, elem in enumerate(inorder)}
        return helper(0, len(preorder), 0, len(inorder))
        """
        # Solution 2 - 36 ms
        hashMap = {}
        for idx, val in enumerate(inorder):
            hashMap[val] = idx
        preorder_index = 0

        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right: return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, hashMap[root_value] - 1)
            root.right = array_to_tree(hashMap[root_value] + 1, right)

            return root

        return array_to_tree(0, len(preorder) - 1)


# Main Call
preorder = [3, 9, 20, 15, 7]
inorder = [9,3,15,20,7]
solution = Solution()
node = solution.buildTree(preorder, inorder)
# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
print(response)
