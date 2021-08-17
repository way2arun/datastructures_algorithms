"""
Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.



Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
   Hide Hint #1
Use DFS (Depth First Search) to traverse the tree, and constantly keep track of the current path maximum.
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Solution 1 - 322 ms
        """
        def helper(node, curr_max):
            if node is None:
                return 0
            elif node.val >= curr_max:  # add 1 if current node value is greater or equal to the max generated from this path also update the max till now
                curr_max = node.val
                return 1 + helper(node.left, curr_max) + helper(node.right, curr_max)
            else:
                return helper(node.left, curr_max) + helper(node.right, curr_max)

        return helper(root, float('-inf'))
        """
        # Solution 2 - 204 ms
        if root is None:
            return 0
        self.res = 0

        def dfs(node, cm):
            if node.val >= cm:
                # print(node.val)
                self.res += 1
                cm = node.val
            if node.left is not None:
                dfs(node.left, cm)
            if node.right is not None:
                dfs(node.right, cm)

        dfs(root, -int(1e9) + 7)
        return self.res


# Main Call
root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

solution = Solution()
print(solution.goodNodes(root))