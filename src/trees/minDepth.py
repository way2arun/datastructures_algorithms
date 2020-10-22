"""
Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Solution 1 - 488 ms
        """
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            for child in [node.left, node.right]:
                if not child:
                    continue
                queue.append((child, depth + 1))
        """
        # Solution 2 - 20 ms
        if not root: return 0
        queue = [root]
        level = 1
        while queue:
            next_queue = []
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            level += 1
        return level


# Main Call
tree_root = TreeNode(3)
tree_root.left = TreeNode(9)
tree_root.right = TreeNode(20)
tree_root.right.left = TreeNode(15)
tree_root.right.right = TreeNode(7)

solution = Solution()
print(solution.minDepth(tree_root))
