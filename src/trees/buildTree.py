"""
Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3403/
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Solution 1 - 224 ms
        """
        if not inorder or not postorder:
            return

        i = inorder.index(postorder[-1])
        root = TreeNode(postorder[-1])

        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])

        return root
        """

        # Solution 2 - 36 ms

        if len(postorder) == 0:
            return None

        head = TreeNode(postorder[-1])

        stack = [head]
        i = len(postorder) - 2
        j = len(postorder) - 1
        while i >= 0:
            temp = None
            t = TreeNode(postorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j -= 1
            if temp:
                temp.left = t
            else:
                stack[-1].right = t
            stack.append(t)
            i -= 1
        return head


        # Solution 3 - 40 ms using dfs
        """
        inorder_map = {}
        for i, v in enumerate(inorder):
            inorder_map[v] = i
        k = -1

        def dfs(low, high):
            nonlocal k
            if low > high: return None
            root = TreeNode(postorder[k])
            k -= 1
            index = inorder_map[root.val]
            root.right = dfs(index + 1, high)
            root.left = dfs(low, index - 1)

            return root

        return dfs(0, len(inorder) - 1)
        """

    def preorder(self, root):
        """
        :param root:
        :return:
        """
        if root is not None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        """
        :param root:
        :return:
        """
        if root is not None:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


# Main Call
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
solution = Solution()
tree_root = solution.buildTree(inorder, postorder)
print("Pre-Order")
solution.preorder(tree_root)
print("In-Order")
solution.inorder(tree_root)
