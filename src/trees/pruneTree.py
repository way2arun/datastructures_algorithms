"""
Binary Tree Pruning
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.



Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]


Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
"""
from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # Solution 1 - 32 ms
        """
        if root == None: return root
        root.left = self.pruneTree(root.left)  # Set new root.left
        root.right = self.pruneTree(root.right)  # Set new root.right
        if root.left is not None or root.right is not None or root.val == 1:  # Check if current subtree contain 1 or not?
            return root
        return None  # If not, return None
        """
        # Solution 2 - 12 ms
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root


# Main Call
root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

solution = Solution()
result = solution.pruneTree(root)

# Lets print the binary tree
print_tree = PrintBinaryTree()
response = print_tree.print_tree(result)
print(response)
