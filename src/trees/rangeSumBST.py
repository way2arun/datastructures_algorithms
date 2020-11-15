"""
Range Sum of BST
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23


Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Solution 1 - 216 ms
        """
        self.sum = 0
        self.low = low
        self.high = high
        self.inorder(root)
        return self.sum
        """
        # Solution 2 - 176 ms
        """
        self.ans = 0
        self.low = low
        self.high = high
        self.dfs(root)
        return self.ans
        """
        # Solution 3 - 172 ms
        self.ans = 0

        def dfs(head):
            if head:
                if low <= head.val <= high:
                    self.ans += head.val
                if low < head.val:
                    dfs(head.left)
                if head.val < high:
                    dfs(head.right)

        dfs(root)
        return self.ans

    def dfs(self, node):
        if node:
            if self.low <= node.val <= self.high:
                self.ans += node.val
            if node.val > self.low:
                self.dfs(node.left)
            if node.val < self.high:
                self.dfs(node.right)

    def inorder(self, root):
        if root:
            if self.low < root.val:
                self.inorder(root.left)

            if self.low <= root.val <= self.high:
                self.sum += root.val

            if root.val < self.high:
                self.inorder(root.right)


# Main Call

treenode = TreeNode(10)
treenode.left = TreeNode(5)
treenode.left.left = TreeNode(3)
treenode.left.right = TreeNode(7)
treenode.right = TreeNode(15)
treenode.right.right = TreeNode(18)
low = 7
high = 15

solution = Solution()
print(solution.rangeSumBST(treenode, low, high))
