"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3361/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root
        """
        # Solution 2
        if not root:
            return
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# Main Call
"""
Given the tree:
        4
       / \
      2   7
     / \
    1   3
"""
solution = Solution()
tree_root = TreeNode(4)
tree_left_1 = TreeNode(2)
tree_right_1 = TreeNode(7)
tree_left_2 = TreeNode(1)
tree_left_3 = TreeNode(3)

tree_root.left = tree_left_1
tree_left_1.left = tree_left_2
tree_left_1.right = tree_left_3
tree_root.right = tree_right_1
root = solution.searchBST(tree_root, 2)
print(root.val)
