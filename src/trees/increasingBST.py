"""
Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000

"""

from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Solution 1 - 28 ms
        """
        return self.dfs(root)[0]
        """
        # Solution 2 - 16 ms
        global roots
        roots = root
        global first
        global joiner
        joiner = None
        first = 1

        def helper(nde):
            global first
            global roots
            global joiner
            if nde.left:
                helper(nde.left)
            if first:
                roots = nde
                joiner = nde
                first = 0
            else:
                nde.left = None
                joiner.right = nde
                joiner = nde
            if nde.right:
                helper(nde.right)

        helper(roots)
        return roots


    def dfs(self, node):
        l1, r2 = node, node
        if node.left:
            l1, l2 = self.dfs(node.left)
            l2.right = node
        if node.right:
            r1, r2 = self.dfs(node.right)
            node.right = r1
        node.left = None
        return l1, r2


# Main Call
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)

solution = Solution()
node = solution.increasingBST(root)
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
print(response)
