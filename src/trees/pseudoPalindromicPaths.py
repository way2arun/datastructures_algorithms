"""
Pseudo-Palindromic Paths in a Binary Tree
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.



Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1


Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.
   Hide Hint #1
Note that the node values of a path form a palindrome if at most one digit has an odd frequency (parity).
   Hide Hint #2
Use a Depth First Search (DFS) keeping the frequency (parity) of the digits. Once you are in a leaf node check if at most one digit has an odd frequency (parity).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs2(self, node, x):
        y = x ^ (1 << node.val)
        if not node.left and not node.right:
            if y & (y - 1) == 0:
                self.ans += 1
        else:
            if node.left:
                self.dfs(node.left, y)
            if node.right:
                self.dfs(node.right, y)

    def dfs(self, root, path):
        if root is None:
            return
        path ^= (1 << root.val)
        if root.left is None and root.right is None:  # Is leaf node
            if path & (path - 1) == 0:  # If path has only 1 odd digit or path = 0
                self.ans += 1
            return
        self.dfs(root.left, path)
        self.dfs(root.right, path)

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        # Solution 1 - 332 ms
        """
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
        """
        # Solution 2 -
        self.ans = 0
        self.dfs2(root, 0)
        return self.ans


# Main Call
root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)

solution = Solution()
print(solution.pseudoPalindromicPaths(root))
