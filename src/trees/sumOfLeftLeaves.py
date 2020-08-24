"""
Sum of Left Leaves
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3435/
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Solution 1 - 32 ms
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
                if node.left.left is None and node.left.right is None:
                    res += node.left.val
            if node.right:
                queue.append(node.right)
        return res
        """
        # Solution 2 - 16 ms
        self.suml = 0
        self.isleftleaves(root)
        return self.suml

    def isleftleaves(self, root):
        if root is None:
            return None
        else:
            if root.left is not None and (root.left.right is None and root.left.left is None):
                self.suml += root.left.val

        self.isleftleaves(root.right)
        self.isleftleaves(root.left)


# Main Call
# Tree Node
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.sumOfLeftLeaves(root))
