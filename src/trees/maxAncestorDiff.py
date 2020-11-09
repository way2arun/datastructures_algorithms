"""
Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.



Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3


Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
   Hide Hint #1
For each subtree, find the minimum value and maximum value of its descendants.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # Solution 1 - 32 ms
        """
        self.Max = 0
        self.dfs(root, root.val, root.val)
        return self.Max
        """
        # Solution 2 - 20 ms
        if root is None:
            return 0

        stack = [(root, None, None)]
        max_diff = 0
        while len(stack) != 0:
            node, min_ancestor, max_ancestor = stack.pop()
            if min_ancestor is None:
                if node.left is not None:
                    stack.append((node.left, node, node))
                if node.right is not None:
                    stack.append((node.right, node, node))
            else:
                max_diff = max(max_diff, abs(node.val - min_ancestor.val), abs(node.val - max_ancestor.val))
                if node.left is not None:
                    stack.append((node.left,
                                  node if node.val < min_ancestor.val else min_ancestor,
                                  node if node.val > max_ancestor.val else max_ancestor))
                if node.right is not None:
                    stack.append((node.right,
                                  node if node.val < min_ancestor.val else min_ancestor,
                                  node if node.val > max_ancestor.val else max_ancestor))
        return max_diff

    def dfs(self, node, low, high):
        if not node:
            return
        self.Max = max(self.Max, abs(node.val - low), abs(node.val - high))
        low1, high1 = min(low, node.val), max(high, node.val)
        self.dfs(node.left, low1, high1)
        self.dfs(node.right, low1, high1)


# Main Call
tree_node = TreeNode(1)
tree_node.right = TreeNode(2)
tree_node.right.right = TreeNode(0)
tree_node.right.right.left = TreeNode(3)

solution = Solution()
print(solution.maxAncestorDiff(tree_node))
