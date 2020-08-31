"""
Delete Node in a BST
https://leetcode.com/explore/featured/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3443/
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""


# Definition for a binary tree node.
from src.trees.printBinaryTree import PrintBinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # Solution 1 - 76ms
        """
        if not root:
            return None

        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
        """
        # Solution 2 - 60 ms
        if root:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                nxt = root.right
                while nxt.left:
                    nxt = nxt.left
                root.val = nxt.val
                root.right = self.deleteNode(root.right, nxt.val)
        return root


# Main Call
# Load the linked list
treeNode = TreeNode(5)
treeNode.left = TreeNode(3)
treeNode.right = TreeNode(6)
treeNode.left.left = TreeNode(2)
treeNode.left.right = TreeNode(4)
treeNode.right.right = TreeNode(7)

# Solution
solution = Solution()
treeRoot = solution.deleteNode(treeNode, key=3)
# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(treeRoot)
print(response)
