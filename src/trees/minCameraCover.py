"""
Binary Tree Cameras
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Solution 2 - 28 ms
    def __init__(self):
        self.numCam = 0
        self.covered = {None}

    def dfs(self, node, par=None):
        if node:
            self.dfs(node.left, node)
            self.dfs(node.right, node)

            if ((par is None and node not in self.covered) or (
                    node.left not in self.covered or node.right not in self.covered)):
                self.numCam += 1
                self.covered.update({node, node.left, node.right, par})

        return
    def minCameraCover(self, root: TreeNode) -> int:
        # Solution 1 - 36 ms
        """
        def dfs(node):
            if not node: return float("inf"), 0, 0
            q1_l, q2_l, q3_l = dfs(node.left)
            q1_r, q2_r, q3_r = dfs(node.right)
            q1 = min(q1_l, q2_l) + min(q1_r, q2_r) + 1
            q3 = min(q1_l + q1_r, q1_l + q3_r, q3_l + q1_r)
            q2 = min(q3, q3_l + q3_r)
            return q1, q2, q3

        return min(dfs(root)[0::2])  # 0 and 2
        """
        # Solution 2 - 28 ms
        if not root:
            return 0
        self.dfs(root, None)
        return self.numCam


# Main Call
root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(0)

solution = Solution()
print(solution.minCameraCover(root))
