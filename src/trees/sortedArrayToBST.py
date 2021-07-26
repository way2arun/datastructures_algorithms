"""
Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
from typing import List

from src.trees.printBinaryTree import PrintBinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums):
    """
    time:
    space:
    """

    def construct(l, r):
        if l > r:
            return None

        if l == r:
            return TreeNode(nums[l])

        m = (l + r) // 2
        left = construct(l, m - 1)
        right = construct(m + 1, r)

        return TreeNode(nums[m], left, right)

    return construct(0, len(nums) - 1)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Solution 1  - 64 ms
        """
        def dfs(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)
        """
        # Solution 2 - 36 ms
        return sorted_array_to_bst(nums)


# Main Call
nums = [-10, -3, 0, 5, 9]
solution = Solution()
node = solution.sortedArrayToBST(nums)
print_tree = PrintBinaryTree()
response = print_tree.print_tree(node)
