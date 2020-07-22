"""
Binary Tree Zigzag Level Order Traversal
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3398/
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # Solution 1 - 52 ms
        """
        self.zigzag_list = {}
        if root:
            self.dfs(root, 1)

        res = []
        for element in self.zigzag_list:
            if element % 2 == 0:
                self.zigzag_list[element] = self.zigzag_list[element][::-1]
            res.append(self.zigzag_list[element])
        return res
        """
        # Solution 2  - 16 ms

        q, res = [], []
        if root is not None:
            q.append(root)
        while len(q) > 0:
            curLevel = []
            for i in range(len(q)):
                node = q.pop(0)
                curLevel.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if len(res) % 2 != 0:
                for j in range(len(curLevel) // 2):
                    curLevel[j], curLevel[len(curLevel) - 1 - j] = curLevel[len(curLevel) - 1 - j], curLevel[j]
            res.append(curLevel)
        return res

        """
        # Solution 3 - 20 ms
        if root is None:
            return None

        queue = []
        ans = []
        queue.append(root)
        c = 0
        while len(queue):
            c = c + 1
            r = []
            for i in range(len(queue)):
                node = queue.pop(0)
                r.append(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
            if c % 2 == 0:
                r = r[::-1]
                ans.append(r)
            else:
                ans.append(r)
        return ans
        """

    def dfs(self, node, level):

        if level not in self.zigzag_list:
            self.zigzag_list[level] = []
        self.zigzag_list[level].append(node.val)

        if node.left:
            self.dfs(node.left, level + 1)
        if node.right:
            self.dfs(node.right, level + 1)


# Main Call
tree_root = TreeNode(3)
tree_left_1 = TreeNode(9)
tree_right_1 = TreeNode(20)
tree_right_1.left = TreeNode(15)
tree_right_1.right = TreeNode(7)

tree_root.left = tree_left_1
tree_root.right = tree_right_1

solution = Solution()
root = solution.zigzagLevelOrder(tree_root)
print(root)
