"""
Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def dfs(self, node, num):
        if not node:
            return
        self.pathNodes.append(node.val)
        num += node.val
        if num == self.TS and not node.left and not node.right:
            self.ans.append(list(self.pathNodes))
        else:
            self.dfs(node.left, num)
            self.dfs(node.right, num)
        self.pathNodes.pop()
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # Solution 1 - 44 ms
        """
        def dfs(root, targetSum, path):
            if root is None: return None
            targetSum -= root.val
            path.append(root.val)
            if root.left is None and root.right is None:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans
        """
        # Solution 2 - 24 ms
        self.TS = targetSum
        self.pathNodes = []
        self.ans = []

        self.dfs(root, 0)

        return self.ans



# Main Call
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
targetSum = 22
solution = Solution()
print(solution.pathSum(root, targetSum))