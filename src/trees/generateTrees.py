"""
Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 8
"""

# Definition for a binary tree node.
from itertools import product
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, result, start, end, index_to_tree_list):
        if start == end:
            return [TreeNode(start)]
        if start > end:
            return [None]
        if (start, end) in index_to_tree_list:
            return index_to_tree_list[(start, end)]

        root_trees = []
        for i in range(start, end + 1):
            left_trees = self.dfs(result, start, i - 1, index_to_tree_list)
            right_trees = self.dfs(result, i + 1, end, index_to_tree_list)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    root_trees.append(root)

        index_to_tree_list[(start, end)] = root_trees

        return root_trees

    def generateTrees(self, n: int) -> List[TreeNode]:
        # Solution 1 - 40 ms
        """
        def rec(start, end):

            if start > end:
                return [None]

            if start == end:
                return [TreeNode(start)]
            ret_list = []

            for i in range(start, end + 1):
                left = rec(start, i - 1)
                right = rec(i + 1, end)
                for pair in product(left, right):
                    ret_list.append(TreeNode(i, pair[0], pair[1]))

            return ret_list

        res = rec(1, n)
        return res
        """
        # Solution 2 - 36 ms
        result = []
        index_to_tree_list = {}
        return self.dfs(result, 1, n, index_to_tree_list)


# Main Call
n = 3
solution = Solution()
print(solution.generateTrees(n))
