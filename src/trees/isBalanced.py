"""
 Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Solution 1 - 48 ms
        #return self.dfs(root)[1]

        # Solution 2 - 28 ms
        h, is_b = self.helper(root)
        return is_b

    def helper(self, root):
        if root is None:
            return 0, True
        hl, lb = self.helper(root.left)
        hr, rb = self.helper(root.right)
        if lb and rb and abs(hl - hr) <= 1:
            return max(hl, hr) + 1, True
        else:
            return -1, False

    def dfs(self, root):  # return (depth, isBalance)
        if root is None:
            return 0, True
        leftH, leftB = self.dfs(root.left)  # left height, left balance
        rightH, rightB = self.dfs(root.right)  # right height, right balance
        return max(leftH, rightH) + 1, abs(leftH - rightH) <= 1 and leftB and rightB


# Main Call
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.isBalanced(root))

root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.left = TreeNode(4)

print(solution.isBalanced(root))

