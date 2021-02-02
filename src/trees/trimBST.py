"""
Trim a Binary Search Tree
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.



Example 1:


Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
Example 2:


Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]
Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]


Constraints:

The number of nodes in the tree in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104
"""

from src.trees.printBinaryTree import PrintBinaryTree

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def traverseTrim(self, root: TreeNode, low, high):
        if root == None: return
        # #leaf
        # if root.left == None and root.right == None:
        #     if root.val < low or root.val > high:
        #         return None
        #     else:
        #         return root

        if root.val < low:
            return self.traverseTrim(root.right, low, high)
        elif root.val > high:
            return self.traverseTrim(root.left, low, high)
        else:
            root.left = self.traverseTrim(root.left, low, high)
            root.right = self.traverseTrim(root.right, low, high)
            return root

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # Solution 1 - 64 ms
        """
        if not root:
            return root
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
        """
        # Solution 2 - 32 ms
        return self.traverseTrim(root, low, high)



# Main call
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
low = 1
high = 2
solution = Solution()
treeroot = solution.trimBST(root, low, high)

print_tree = PrintBinaryTree()
response = print_tree.print_tree(treeroot)
print(response)

