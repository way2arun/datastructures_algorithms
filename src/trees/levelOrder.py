"""
Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
from collections import deque, defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Solution 1 - 40 ms
        """
        queue, ans = deque([root] if root else []), []
        while len(queue):
            qlen, row = len(queue), []
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(row)
        return ans
        """
        # Solution 2 - 8 ms
        if not root:
            return []
        di = defaultdict(list)

        def solve(root, level, di):
            if not root:
                return
            di[level].append(root.val)
            if root.left: solve(root.left, level + 1, di)
            if root.right: solve(root.right, level + 1, di)

        solve(root, 0, di)
        lis = list(di.keys())
        lis.sort()
        ans = []
        for i in lis:
            ans.append(di[i])
        return ans


# Main Call
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.levelOrder(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

solution = Solution()
print(solution.levelOrder(root))

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(1)

solution = Solution()
print(solution.levelOrder(root))