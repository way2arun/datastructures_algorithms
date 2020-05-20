"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

   Hide Hint #1
Try to utilize the property of a BST.
   Hide Hint #2
Try in-order traversal. (Credits to @chan13)
   Hide Hint #3
What if you could modify the BST node's structure?
   Hide Hint #4
The optimal runtime complexity is O(height of BST).
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3335/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        52 ms
        if not root:
            return
        stack = []
        response = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            response.append(root.val)
            root = root.right

            if len(response) == k:
                return response[-1]
        """
        # Solution 2 28 ms
        self._counter = 0
        self._k = k
        self._node = None
        self._inorder_dfs(root)
        return self._node.val

    def _inorder_dfs(self, node):
        if self._counter == self._k:
            return
        if not node:
            return
        self._inorder_dfs(node.left)
        if self._counter == self._k:
            return
        self._counter += 1
        self._node = node
        self._inorder_dfs(node.right)


# Main Call
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
k = 1
solution = Solution()
print(solution.kthSmallest(root, k))
