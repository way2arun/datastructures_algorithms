"""
Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Solution 1 - 44 ms
        """
        if not root:
            return []

        res = []
        deque = collections.deque([root])

        while deque:
            size = len(deque)

            for i in range(size):
                node = deque.popleft()
                if i == size - 1:
                    res.append(node.val)

                if node.left:
                    deque.append(node.left)

                if node.right:
                    deque.append(node.right)

        return res
        """
        # Solution 2 - 12 ms
        if not root:
            return []

        curr_level = [root]
        rst = []
        while len(curr_level) > 0:
            rst.append(curr_level[-1].val)
            next_level = []
            for n in curr_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            curr_level = next_level

        return rst


# Main Call
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.rightSideView(root))
