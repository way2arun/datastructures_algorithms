"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maximum_sum = float('-inf')
        self.result = [float('-inf')]

    def maxPathSum(self, root: TreeNode) -> int:
        """
        # 96 ms
        self.find_max_sum(root)
        return self.maximum_sum
        """
        # 60 ms
        self.find_max_sum_dfs(root, self.result)
        return self.result[0]

    def find_max_sum_dfs(self, root, res):
        if not root:
            return 0
        left = self.find_max_sum_dfs(root.left, res)
        right = self.find_max_sum_dfs(root.right, res)
        res[0] = max(res[0], left + right + root.val)
        return max(left + root.val, right + root.val, 0)

    def find_max_sum(self, root):
        # 96 ms
        if not root:
            return 0
        # Traverse through left then right
        left_nodes = self.find_max_sum(root.left)
        right_nodes = self.find_max_sum(root.right)
        if left_nodes > 0:
            left_nodes = left_nodes
        else:
            left_nodes = 0
        if right_nodes > 0:
            right_nodes = right_nodes
        else:
            right_nodes = 0
        # left_nodes = left_nodes if left_nodes > 0 else 0
        # right_nodes = right_nodes if right_nodes > 0 else 0
        self.maximum_sum = max(self.maximum_sum, root.val + left_nodes + right_nodes)
        return max(left_nodes, right_nodes) + root.val


# Main Call
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

solution = Solution()
print(solution.maxPathSum(root))
