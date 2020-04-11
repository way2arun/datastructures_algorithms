"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


"""
from idlelib.tree import TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # For solution 1
        self.number_of_nodes = 1
        # For solution 2
        self.result = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Solution 1 - 24ms
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # path
            self.number_of_nodes = max(self.number_of_nodes, left + right + 1)
            return max(left, right) + 1
        # Call the function depth (this is like function inside function)
        depth(root)
        return self.number_of_nodes - 1

        # Solution 2 - 44 ms
        # self.get_max_depth(root)
        # return self.result

    def get_max_depth(self, root):
        if root is None:
            return 0
        left = self.get_max_depth(root.left)
        right = self.get_max_depth(root.right)
        self.result = max(self.result, right + left)
        return max(left + 1, right + 1)


# Main Call
# Initialize the Tree First

tree_root = TreeNode(1)
tree_left_1 = TreeNode(2)
tree_right_1 = TreeNode(3)
tree_left_2 = TreeNode(4)
tree_left_3 = TreeNode(5)
tree_root.left = tree_left_1
tree_left_1.left = tree_left_2
tree_left_1.right = tree_left_3
tree_root.right = tree_right_1

tree_right_1.left = None
tree_right_1.right = None
tree_left_2.left = None
tree_left_2.right = None
tree_left_3.left = None
tree_left_3.right = None

print(tree_root.val)
print(tree_root.left.val)
print(tree_root.left.left.val)
print(tree_root.left.right.val)

print(tree_root.right.val)

solution = Solution()
response = solution.diameterOfBinaryTree(tree_root)
print(response)
